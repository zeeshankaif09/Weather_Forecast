import streamlit as st
import plotly.express as px
from backend import get_data

# add title text_input slider select_box and sub_header
st.title("Weather forecast for the next days")
place = st.text_input("Place : ")
days = st.slider("Forcast days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("select data to view", ("Temperature", "sky"))
st.subheader(f"{option}for the next {days} days in {place}")

if place:
    # Get the temperature sky data
    filtered_data = get_data(place, days)


    # create temperature plot
    if option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)



    if option == "sky":
        images = {"Clear": "images/clear.png", "clouds": "images/cloud.png", "rain": " images/rain.png",
                  "snow": "images/snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        print(sky_conditions)
        st.image(image_paths, width=115)

