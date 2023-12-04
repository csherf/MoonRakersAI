import os
import openai
from dotenv import load_dotenv

#dotenv initialization
load_dotenv()
project_folder = os.path.expanduser("G:\My Drive\MoonRakersAI\data")
os.path.join(project_folder, 'setup.env')

# variables
OPENAI_KEY = os.environ['OPENAI_KEY']
MODEL_NAME = os.environ['MODEL_NAME']
EMBEDDING_MODEL = os.environ['EMBEDDING_MODEL']
MAX_TOKENS = 8000


def gpt_response(input):
    openai.api_key = OPENAI_KEY
    message = input
    response = openai.ChatCompletion.create(
            model = MODEL_NAME,
            max_tokens = 128,
            messages = message)
    reply = response["choices"][0]["message"]["content"]
    return reply