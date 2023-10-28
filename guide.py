import csv
import os
import numpy as np
import openai
import pprint
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from dotenv import load_dotenv

#dotenv initialization
load_dotenv()
pp = pprint.PrettyPrinter(indent=4)
project_folder = os.path.expanduser("G:\My Drive\Moonrakers")
os.path.join(project_folder, 'setup.env')

# variables
DATABASE_NAME = "vectorDB_guide"
OPENAI_KEY = "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"
MODEL_NAME = "gpt-3.5-turbo-0301"
EMBEDDING_MODEL = "text-embedding-ada-002"
EMBEDDING_ENCODING = "cl100k_base"
MAX_TOKENS = 8000

# chromaDB setup
client = chromadb.PersistentClient(path = "G:\My Drive\Moonrakers\Data")
embedding_function = OpenAIEmbeddingFunction(api_key = OPENAI_KEY, model_name = EMBEDDING_MODEL)
collection = client.get_or_create_collection(name = DATABASE_NAME, embedding_function = embedding_function)

def generate_response(input):
    openai.api_key = OPENAI_KEY
    message = input
    messages = []
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
            model = MODEL_NAME,
            max_tokens = 128,
            messages = messages)
    reply = response["choices"][0]["message"]["content"]
    return reply

def get_embedding(text):
   openai.api_key = OPENAI_KEY
   text = text.replace("\n", " ")
   return openai.Embedding.create(input = [text], model = EMBEDDING_MODEL)['data'][0]['embedding']

def add_data(text, id, strength, result):
    collection.upsert(
        documents=[text],
        metadatas=[{"strength": strength, "result": result}],
        ids=[id],
    )

def main():
    while True:
        print(collection.count())
        data_id = collection.count() + 1

        block_text = ""
        csv_data = []

        input_text = input("You: ")
        if input_text.lower() == "quit":
            break
        id = str(data_id)
        add_data(input_text, id, "0.5", "unknown")
        response = generate_response(input_text)

        block_text = "System response: " + response
        print(block_text)

        collection.get()

if __name__ == "__main__":
    # main()
    print(collection.get(
        ids = ["1"],
        include = [ "metadatas" ]
        )
    )