import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import datetime
import sqlite3

st.title("Average world temperatures")


def custom_date_parser(x):
    return datetime.strptime(x, "%Y-%m-%d-%H-%M-%S")


connection = sqlite3.connect('data.db')
cursor = connection.cursor()
cursor.execute("SELECT * FROM temperatures")
rows = cursor.fetchall()

df = pd.DataFrame.from_records(rows, columns=["date", "temperature"])
df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d-%H-%M-%S")
temps = px.line(x=df['date'], y=df['temperature'], labels={"x": "date", "y": "temperature"})

st.plotly_chart(temps)
