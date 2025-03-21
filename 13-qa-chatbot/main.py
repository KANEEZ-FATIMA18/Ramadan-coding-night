# Import required libraries
import os
import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Gemini API key from environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini AI with the API key
genai.configure(api_key=gemini_api_key)

# Initialize the Gemini model
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# Handler function when a chat session starts
@cl.on_chat_start
async def handle_chat_start():
    # Send welcome message to user
    await cl.Message(content="Hi, I am your AI assistant! How can I help you today?").send()

# Handler function for each user message
@cl.on_message
async def handle_message(message:cl.Message):
    # Get the user's input
    prompt = message.content

    # Generate response using Gemini model
    response = model.generate_content(prompt)

    # Extract text from response, or empty string if no text attribute
    response_text= response.text if hasattr(response,"text") else ""

    # Send the response back to the user
    await cl.Message(content = response_text).send()    