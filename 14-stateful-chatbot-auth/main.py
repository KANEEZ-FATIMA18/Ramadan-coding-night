# Import required libraries
import os                                # Import os for environment variables
import chainlit as cl                     # Import ChainLit
import google.generativeai as genai     # Import GenerativeAI for Gemini model 
from dotenv import load_dotenv           # Import load_dotenv for environment variables
from typing import Optional, Dict


load_dotenv()                            # Load environment variables from .env file

# Setup API key for Gemini
gemini_api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key = gemini_api_key)   # Configure Gemini API key

# Create Gemini model instance
model = genai.GenerativeModel(model_name = "gemini-2.0-flash")


# Handle GitHub login callback
@cl.oauth_callback                                     # Decorator for login callback
def oauth_callback(                                    
    provider_id: str,                                  # Which login service was used
    token: str,                                        # Login token
    raw_user_data: Dict[str,str],                      # User info from login
    default_user: cl.User,                             # Basic user details
) -> Optional[cl.User]:                                # Returns user info or nothing
   
   """
    Processes the login response from GitHub
    Sends back user info if login works
    """
   
   print(f"Provider: {provider_id}")                    # Show login service name
   print(f"User Data: {raw_user_data}")                # Show user details
   return default_user                                  # Send back user info


# Start new chat session
@cl.on_chat_start
async def handle_chat_start():
    # Initialize empty chat history
    cl.user_session.set("history", [])
    
    await cl.Message(content= "Hello! I am a chatbot. How can I help you today?").send()    # Send welcome message to user


# Handle incoming messages
@cl.on_message
async def handle_message(message :cl.Message):
    # Get chat history
    history= cl.user_session.get("history")

    # Add user message to history
    history.append({"role" : "user" , "content": message.content })


    # Format history for Gemini model
    formatted_history =[]                              # Create empty list for formatted messages
    for msg in history:                               # Loop through each message in history
        role ="user" if msg["role"] == "user" else "model"       # Set role as user or model
        formatted_history.append({"role": role, "parts": [{"text": msg["content"]}]})       # Add formatted message to list



    # Get response from Gemini
    response = model.generate_content(formatted_history)         # Get AI response using chat history
    response_text = response.text if hasattr(response, "text") else ""    # Extract text from response or use empty string



    # Add bot response to history
    history.append({"role": "assistant", "content": response_text})    # Add AI response to chat history
    cl.user_session.set("history",history)                            # Update session with new history



    # Send response back to user
    await cl.Message(content= response_text).send()                # Send AI response to user
