import pandas as pd


df = pd.read_json("steam_app_database.json")

int_columns = [
    "appid",
    "achievement_count",
    "player_count",
    "review_score",
    "total_positive",
    "total_negative",
    "total_reviews",
]


for col in int_columns:
    if col in df.columns:
        
        df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")


if "price_usd" in df.columns:
    df["price_usd"] = pd.to_numeric(df["price_usd"], errors="coerce").apply(
        lambda x: f"{x:.2f}" if pd.notnull(x) else ""
    )


if "is_free" in df.columns:
    df["is_free"] = df["is_free"].astype(bool)


df.to_csv("steam_app_database.csv", index=False)
