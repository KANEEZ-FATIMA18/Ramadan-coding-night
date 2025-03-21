# Import required libraries
import google.generativeai as genai
from dotenv import load_dotenv
import os 

# Load environment variables from .env file
load_dotenv()

# Configure Gemini API with key from environment variables
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Initialize the Gemini model
model = genai.GenerativeModel(model_name ="gemini-2.0-flash")

# Start infinite loop for chat interaction
while True:
    # Get user input from terminal
    user_input = input("Enter your question (or 'quit' to exit): ")
    
    # Exit loop if user types 'quit'
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
    
    # Send user input to Gemini and get AI response
    response = model.generate_content(user_input)
    print("\nResponse:",response.text)