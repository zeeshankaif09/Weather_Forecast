import streamlit as st

st.title("Weather forecast for the next days")
place = st.text_input("Place : ")
days = st.slider("Forcast days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("select data to view", ("Temperature", "sky"))
st.subheader(f"{option}for the next {days} days in {place}")
