# Load needed tools
import streamlit as st
import requests

def get_random_joke():
    """Get a joke from the internet"""
    try:
        # Ask the joke website for a joke
        response = requests.get("https://official-joke-api.appspot.com/random_joke")

        if response.status_code == 200:
            # Turn the website's answer into usable data
            joke_data = response.json()
            # Put the joke together
            return f"{joke_data['setup']}\n\n{joke_data['punchline']}"
        
        else:
            # Show error if we can't get a joke
            return "Failed to fecth a Joke.  Please try again later!"
        
    except:
        # Use this backup joke if something goes wrong
        return "Why do programmers prefer Dark Mode? Because light attracts bugs!"    
    
def main():
    # Make the webpage title and description
    st.title('🎯 RANDOM JOKE GENERATOR 😂')
    st.write('Click the button below to get a random joke! 😄') 

    # Make a button to show jokes
    if st.button("Generate Joke"):
        joke = get_random_joke()
        st.success(joke)

    st.divider()

    # Add information at the bottom of the page
    st.markdown(
        """
    <div style='text-align:center;'>
        <p> Joke from official API </p>
        <p>Build with  ❤ by <a href="https://github.com/KANEEZ-FATIMA18"> Kaneez Fatima </a> with streamlit App</p>
    </div>
""", unsafe_allow_html=True) 

# Start the program
if __name__ == "__main__":
    main()   