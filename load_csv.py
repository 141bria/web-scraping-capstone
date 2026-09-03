import pandas as pd
raw_data = pd.read_csv("weather_words.csv")
print(raw_data.head())

print(raw_data.isnull().sum())
print(raw_data.duplicated().sum)
print(raw_data[raw_data["Word"].str.len() < 2])
print(raw_data[raw_data["Definition"].str.len() < 10])

clean_data = raw_data.sort_values("Word")
clean_data["First Letter"] = clean_data["Word"].str[0]
print(clean_data.groupby("First Letter").size())
import sqlite3
with sqlite3.connect("weather_words.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Weather_words(
        word TEXT NOT NULL UNIQUE,
        definition TEXT
        )
        """)
        clean_data[["Word", "Definition"]].to_sql("Weather_words", conn, if_exists="append", index=False)