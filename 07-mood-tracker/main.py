# Import required libraries
import streamlit as st            # Web app framework
import pandas as pd              # Data manipulation library
import datetime                  # Date and time operations
import os                       # File and directory operations
import csv                      # CSV file handling

# Define file path for storing mood data
MOOD_FILE = "mood_log.csv"      # Constant for data storage file name

# Load existing mood data from CSV file
def load_mood_data():           # Function to read saved mood data
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood"])  # Create empty DataFrame if file doesn't exist
    return pd.read_csv(MOOD_FILE)                     # Read existing data

# Save new mood entry to CSV file
def save_mood_data(date, mood): # Function to save new mood entries
    with open(MOOD_FILE, "a" , encoding='utf-8') as file: 
        writer = csv.writer(file) # Create CSV writer object
        writer.writerow([date, mood])  # Append new entry to file

# App title
st.title("Mood Tracker 📝")        # Display main title with emoji

# Get current date
today = datetime.date.today()   # Get today's date for logging

# Mood selection interface
st.subheader("How are you feeling today? 💭")  # subheader
mood = st.selectbox("Select mood", ["Happy 😊", "Excited 🤩", "Peaceful 😌", "Neutral 😐", "Tired 😫", "Sad 😢", "Angry 😠", "Stressed 😩", "Anxious 😰", "Grateful 🙏"])  # Dropdown for mood selection with emojis

# Save mood when button is clicked
if st.button("Log Mood"):       # Button to save mood
    save_mood_data(today, mood) # Save mood data
    st.success("Mood successfully logged! ✅")  # Show success message

# Load mood data for analysis and visualization
data = load_mood_data()         # Load saved data for display

# Show mood trend visualization
if not data.empty:              # Check if there's data to display
    st.subheader('Mood Trends Over Time')  # Subtitle for visualization
    data["Date"] = pd.to_datetime(data["Date"])  # Convert dates to datetime
    mood_counts = data.groupby("Mood").count()["Date"]  # Count moods
    st.bar_chart(mood_counts)   # Display bar chart of mood frequencies

# Footer 
st.write("Build with ❤️ by [Kaneez Fatima](https://github.com/KANEEZ-FATIMA18)")  # Author credit


    