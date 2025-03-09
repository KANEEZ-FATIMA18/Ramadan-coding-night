import streamlit as st

def unit_converter(value, unit_from, unit_to): # function to convert the units
    conversion ={
       "km_m": 1000,
       "km_cm": 100000,
       "km_mm": 1000000,
       "mm_km": 0.000001,
       "mm_m": 0.001,
       "mm_cm": 0.1,
       "m_km": 0.001,
       "m_mm": 1000,
       "m_cm": 100,
       "cm_km": 0.00001,
       "cm_m": 0.01,
       "cm_mm": 10,
    }

    key = f"{unit_from}_{unit_to}" # key to get the conversion value

    # check if the key is in the conversion dictionary
    if key in conversion:
        conversion = conversion[key] # get the conversion value
        return value* conversion # return the converted value
    else:
        return "Not a valid conversion" # return if the conversion is not valid
    
    # streamlit for the user interface
st.title("Unit Converter") # title of the app
value = st.number_input("Enter the value:")  # input field for the value
unit_from = st.selectbox("Convert From:", ["km", "m", "cm", "mm"])  # dropdown for the unit to convert from
unit_to = st.selectbox("Convert To:", ["km", "m", "cm", "mm"]) # dropdown for the unit to convert to

if st.button("Convert"): # button to convert the units
    result = unit_converter(value, unit_from, unit_to) # call the unit_converter function
    st.write(f"converted value: {result}") # display the converted value