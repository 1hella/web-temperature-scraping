import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.title("Average world temperatures")


def custom_date_parser(x):
    return datetime.strptime(x, "%Y-%m-%d-%H-%M-%S")


df = pd.read_csv("data.txt", parse_dates=['date'], date_parser=custom_date_parser)
temps = px.line(x=df['date'], y=df['temperature'], labels={"x": "date", "y": "temperature"})

st.plotly_chart(temps)
