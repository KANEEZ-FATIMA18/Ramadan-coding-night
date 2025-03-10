import streamlit as st
import random
import time
import requests

# Main title of the web application
st.title('Money Making Machine')

# Function to generate random amount of money between 1 and 800
def Generate_Money():
    return random.randint(1,800)

# Section for generating instant money
st.subheader("Instant money making")

# Button to trigger money generation
if st.button("Generate Money"):
    st.write("Generating your money")
    time.sleep(3)    # Adding delay for better user experience
    
    # Generate and display random amount
    amount = Generate_Money()
    st.success(f"You Made ${amount}!")

# API integration for side hustles
def fetch_side_hustles():
    try:
        # Attempt to fetch side hustles from local API
        response = requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:
            hustle = response.json()
            return hustle["side_hustle"]
        else:
            return("marketing")      # Return default value if API call fails
    except:
        return('something went wrong')     # Handle any API connection errors

# Section for generating random side hustles
st.subheader("Generate Hustle")
if st.button("Side Hustle Ideas"):
    st.write("Generating your Hustle")
    time.sleep(3)      # Adding delay for better user experience
    idea = fetch_side_hustles()
    st.info(idea)         

# API integration for motivational quotes
def fetch_money_quotes():
    try:
        # Attempt to fetch quotes from local API
        response = requests.get('http://127.0.0.1:8000/money_qoutes')
        if response.status_code == 200:
            quote = response.json()
            return quote["money_qoute"]
        else:
            return("practice makes man perfect")   # Return default quote if API call fails
    except:
        return("something went wrong")  # Handle any API connection errors  

# Section for displaying motivational quotes
st.subheader('Motivational Quotes')
if st.button("Generate Quote"):
    st.write("Generating your Hustle")
    time.sleep(3)   # Adding delay for better user experience
    quote = fetch_money_quotes()
    st.warning(quote)

