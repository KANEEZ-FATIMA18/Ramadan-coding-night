import streamlit as st
import random
import string


#password generator function
def password_generator(length, use_digits, use_special):
    characters =string.ascii_letters  #string,ascii-letters is a string of all the letters in the alphabet

    #if use_digits is true, add the digits to the characters string
    if use_digits:
        characters += string.digits  #string.digits is a string of all the digits 0-9

    #if use_special is true, add the special characters to the characters string
    if use_special:
        characters += string.punctuation  #string.punctuation is a string of all the special characters

     #generate password using random.choice to choose a random character from the characters string
    return ''.join(random.choice(characters) for _ in range(length))       

#streamlit app
st.title("Password Generator")
 
#input fields
length =st.slider('Select the lenght of the password',min_value=5,max_value=25,value=10)
use_digits =st.checkbox('Select Digits')
use_special =st.checkbox('Select Special Characters')

#if the button is clicked, generate the password
if st.button('Generate Password'):
    password =password_generator(length, use_digits, use_special)
    st.write(f"Generated Password:`{password}")

st.write("Thank you for using the Password Generator!")
st.write("Made with ❤️ by [Kaneez Fatima](https://github.com/KANEEZ-FATIMA18)")

