import streamlit as st
import plotly.express as px
from backend import get_data

# Adds title, text input, slider, selectbox and subheader to the page
st.title("Weather for the next days")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecast days")
option = st.selectbox("Select data to view",("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get the temperature/sky data
    filtered_data = get_data(place, days)

    if filtered_data:
        
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data] 
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Creates a plot
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature  (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear":"images/clear.png", "Clouds":"images/cloud.png", "Rain":"images/rain.png", "Snow":"images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_path = [images[condition] for condition in sky_conditions]
            # Shows temperatures with images
            st.image(image_path, width=115)

    else:
        st.error(f"The city {place} doesn't exist")