import requests
import ollama
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
from openai import OpenAI
ollama_via_openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
# Constants
OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}

MODEL = "llama3.2"


# Some websites need you to use proper headers when fetching them:
headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

        
# Define our system prompt - you can experiment with this later, changing the last sentence to 'Respond in markdown in Spanish."

system_prompt_for_life_saving = "You are a life saving assistant to teen age kids. Your task is to analyze the user's emotional state based on their text input."\
"Look for signs of suicidal thoughts but avoid mentioning suicide word in response"\
"Suggest small steps that help to get out of this situation and answer them like a friend does\n"
how_was_your_day = input("How are you? How is your day? What went well? What did not go well? :\n")

def get_feelings(how_was_day):
    ollama_via_openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
    print("Calling your best companion BAYMAX");
    response = ollama_via_openai.chat.completions.create(
        model=MODEL,
        messages = [
            {'role':'system','content': system_prompt_for_life_saving},
            {'role':'user', 'content': how_was_day}
        ]
    )
    result = response.choices[0].message.content
    return result
    
print(get_feelings(how_was_your_day))

