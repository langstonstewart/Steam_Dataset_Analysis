import requests, json, time

def init_appids():
    with open("py\\steam_appids.json", "r+") as id_file:
        return json.load(id_file)

app_id_data = init_appids()

APP_IDS = app_id_data["appids"]

params = {
    "cc": "US",     
    "l": "english",
    "cursor": "*",
}

review_params = {
    "json": 1,
    "language": "english",   
    "purchase_type": "all",  
    "day_range": "all",    
    "cursor": "*",
    "num_per_page": 1
    }

class SteamScraper:
    def __init__(self, params, review_params, debug=False) -> None:
        
        self.debug = debug
        self.params = params
        self.review_params = review_params
        self.session = requests.Session()
        self.game_data_list = self.init_db_data() # type: list

    def init_db_data(self):
        try:
            with open("steam_app_database.json", "r", encoding="utf-8") as data_file:
                return json.load(data_file)
            
        except (FileNotFoundError, json.JSONDecodeError):
          
            return []


    def create_parser(self, url, params):
        try:
            res = self.session.get(url, params=params)
            res.raise_for_status()
            return res.json()
        
        except Exception as e:

            print(f"An error occurred: {e}")
            return None
        


    def scrape_basic_data(self, app_id):
        game_data = self.create_parser(f"https://store.steampowered.com/api/appdetails?appids={app_id}", self.params)
        if game_data and str(app_id) in game_data and game_data[str(app_id)].get("success"):

            app_data = game_data[str(app_id)]["data"] # type: dict

            self.game_dict["appid"] = app_id

            self.game_dict["name"] = app_data.get("name", None)

            self.game_dict["releasedate"] = app_data.get("release_date", {}).get("date", None)

            self.game_dict["is_free"] = app_data.get("is_free", None)

            raw_price = app_data.get("price_overview", {}).get("initial", None) 

            if raw_price:
                self.game_dict["price_usd"] = raw_price / 100
            else:
                self.game_dict["price_usd"] = None

            genre_list = app_data.get("genres", None)

            self.game_dict["genre"] = genre_list[-1]["description"] if genre_list else None

            self.game_dict["achievement_count"] = app_data.get("achievements", {}).get("total", None)

            dev_list = app_data.get("developers", None)

            self.game_dict["developer"] = dev_list[0] if dev_list else None

            pub_list = app_data.get("publishers", None)

            self.game_dict["publisher"] = pub_list[0] if pub_list else None

            if self.debug:
                with open("game_data.json", "w", encoding="utf-8") as data_file:
                    json.dump(game_data, data_file, indent=4, ensure_ascii=False)

        else:
            raise Exception
            

    def scrape_concurrent(self, app_id):
        player_res = self.create_parser(f"https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={app_id}", self.params)
        if player_res:

            player_count_data = player_res["response"] # type: dict

            self.game_dict["player_count"] = player_count_data.get("player_count", None)

            if self.debug:
                with open("player_count_data.json", "w", encoding="utf-8") as data_file:
                    json.dump(player_count_data, data_file, indent=4, ensure_ascii=False)

    def scrape_reviews(self, app_id):
        review_res = self.create_parser(f"https://store.steampowered.com/appreviews/{app_id}?json=1&cursor=*&num_per_page=0", self.review_params)
        if review_res:

            review_data = review_res["query_summary"]

            self.game_dict["review_score"] = review_data.get("review_score", None)

            self.game_dict["review_score_desc"] = review_data.get("review_score_desc", None)

            self.game_dict["total_positive"] = review_data.get("total_positive", None)

            self.game_dict["total_negative"] = review_data.get("total_negative", None)

            self.game_dict["total_reviews"] = review_data.get("total_reviews", None)

            if self.debug:
                with open("review_data.json", "w", encoding="utf-8") as data_file:
                    json.dump(review_data, data_file, indent=4, ensure_ascii=False)


    def scrape_game(self, app_id):
        self.game_dict = {}

        try:
            self.scrape_basic_data(app_id)

            self.scrape_concurrent(app_id)

            self.scrape_reviews(app_id)

            self.game_data_list.append(self.game_dict)

            print(f"-\n🗹 Collected Data for APPID {self.game_dict["appid"]}: {self.game_dict["name"]}")

        except Exception:
            print(f"APP {app_id} could not be scraped (possibly delisted?); continuing...")


    def save_data(self):
        with open("steam_app_database.json", "w", encoding="utf-8") as data_file:
            json.dump(self.game_data_list, data_file, indent=4, ensure_ascii=False)

        if len(self.game_data_list) == 1000:
            print(f"Game list has populated ({len(self.game_data_list)}).")
            return True
        return False



steam_scraper = SteamScraper(params, review_params, False)

processed_ids = {game["appid"] for game in steam_scraper.game_data_list if "appid" in game}

remaining_ids = [uid for uid in APP_IDS if uid not in processed_ids]

for i in range(len(remaining_ids)):
    print(f"{"=" * 100}\n◔ APP {i + 1} of {len(remaining_ids) + 1}")

    steam_scraper.scrape_game(remaining_ids[i])

    if steam_scraper.save_data():
        break

    time.sleep(1.5)
    



