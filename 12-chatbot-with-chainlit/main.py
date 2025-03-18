# Import the chainlit library for building chat applications
import chainlit as cl


# Decorator to handle incoming chat messages
@cl.on_message
async def main(message : cl.Message):
     # Create a simple response by echoing back the user's message
     response =f"You said: {message.content}"

     # Send the response back to the chat interface
     # Using await since this is an asynchronous operation
     await cl.Message(content=response).send()
