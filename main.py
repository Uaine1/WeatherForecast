import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather for the next days")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecast days")
option = st.selectbox("Select data to view",("Temparature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

d, t = get_data(place, days, option)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature  (C)"})
st.plotly_chart(figure)
