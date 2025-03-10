# Import required libraries
import streamlit as st
from datetime import datetime 
from zoneinfo import ZoneInfo

# List of available time zones
TIME_ZONE =[
    "UTC",
    "Asia/Karachi",
    "Asia/Dhaka",
    "America/New_York",
    "Europe/London", 
    "Asia/Dubai",
    "Asia/Tokyo",
    "Europe/Paris",
    "Europe/Berlin",
    "Australia/Sydney",
    "Pacific/Auckland",
    "America/Los_Angeles",
    "America/Chicago",
    "Asia/Singapore",
    "Asia/Shanghai",
    "Asia/Jerusalem",
    "Asia/Bangkok",
    "America/Toronto",
    "Europe/Moscow",
    "Asia/Seoul",
    "Europe/Rome",
    "Africa/Cairo",
    "Asia/Hong_Kong",
    "Europe/Madrid",
    "Asia/Jakarta",
    "Europe/Amsterdam",
    "Asia/Kolkata",
    "Pacific/Honolulu",
    "Africa/Lagos",
    "America/Mexico_City",
    "Europe/Stockholm",
    "Asia/Manila",
    "Europe/Istanbul",
    "America/Sao_Paulo",
    "Africa/Johannesburg"
]

# Main app title
st.title("Time Zone App")

# Allow users to select multiple time zones
selected_timezone = st.multiselect('Select Time Zone', TIME_ZONE , default=["Asia/Karachi"])

# Display current time for selected time zones
st.subheader("Selected Time Zone")
for tz in selected_timezone:

    # Get and format current time for each selected zone
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d  %I  %H:%M:%S %p")

    st.write(f"{tz} : {current_time}")

# Time Zone Converter Section
st.subheader("Convert Time Between Time Zones")

# Input for time to convert
current_time =st.time_input("Current Time", datetime.now().time())


# create a selectbox for selecting the timezone to convert from
from_tz =st.selectbox("From TimeZone", TIME_ZONE , index=0)

#create a selectbox for selecting the timezone to convert to
to_tz =st.selectbox("To TimeZone", TIME_ZONE , index=1)

# Convert time when button is clicked
if st.button("Convert Time"):

    # Combine date and time with selected timezone
    dt =datetime.combine(datetime.today(), current_time ,tzinfo=ZoneInfo(from_tz))

    # Convert the time to the selected timezone
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d   %I   %H:%M:%S %p")

    # Display result
    st.success(f"Converted Time in {to_tz} is {converted_time}")
