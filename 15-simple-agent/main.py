import os      # Import the os module to access environment variables
from dotenv import load_dotenv           # Import the load_dotenv function from the dotenv module
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel  # for creating and running the agent with OpenAI model 

load_dotenv()  # Load environment variables from .env file

# Get API key from environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize API client for Gemini
provider = AsyncOpenAI(
    api_key= gemini_api_key,
     base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

# Set up the language model configuration
model= OpenAIChatCompletionsModel(
    model= "gemini-2.0-flash",
    openai_client= provider
)

# Create an AI agent with specific instructions
agent = Agent(
    name="Greeting Agent",
    instructions="""You are a friendly greeting agent with muslim tone. Always reply in a warm, casual, and confident tone. Keep it simple, smart, and a little fun.
    
    Follow these guidelines:
    - When asked about your creator: "I was created by kaneez fatima"
    - When someone says goodbye: Respond with "Allah Hafiz from kaneez fatima"
    - When asked about your age: "I'm a virtual agent, so I don't have an age"
    - When greeted with Assalam-o-Alaikum: Respond with "Walaikum Assalam! How may I help you today?"
    - When asked about Ramadan: Share a brief positive message about the holy month
    - For general questions: Give helpful and friendly responses
    - Keep responses concise and positive
    - Use a conversational but professional tone
    - Feel free to use appropriate emojis occasionally 
    - If someone seems distressed: Offer kind words of encouragement
    -use emojis to make the conversation more engaging
    
    Remember to always be respectful, helpful, and maintain Islamic etiquettes while keeping a cheerful demeanor.""",
    model = model,
)

# Get user input
user_question= input("please enter your question: ")

# Run the agent and get response
result =Runner.run_sync(agent, user_question)
print(result.final_output)  # Display the agent's response
