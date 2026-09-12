import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect("weather_words.db")
df = pd.read_sql_query("SELECT * FROM weather_words",conn)
st.title("Weather Words Dashboard")
st.write("Explore weather terms and their defintions")
st.dataframe(df)
st.subheader("Weather Words by First Letter")
df["first_letter"] = df["word"].str[0]
letter_counts = df["first_letter"].value_counts().sort_index()
st.bar_chart(letter_counts)

st.subheader("Defintion Length")
df["definition_length"] = df["definition"].str.len()
st.line_chart(df["definition_length"])

st.subheader("Filter Weather Words")
selected_letter = st.selectbox(
    "Choose a first letter:",
    sorted(df["first_letter"].unique()))
filtered_df = df[df["first_letter"]== selected_letter]
st.write(f"Words that start with {selected_letter}:")
st.dataframe(filtered_df)
st.bar_chart(filtered_df["definition_length"])