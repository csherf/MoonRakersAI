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
project_folder = os.path.expanduser("G:\My Drive\MoonRakersAI\data")
os.path.join(project_folder, 'setup.env')

# variables
DATABASE_NAME = "vectorDB_guide"
OPENAI_KEY = "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"
MODEL_NAME = "gpt-3.5-turbo-0301"
EMBEDDING_MODEL = "text-embedding-ada-002"
MAX_TOKENS = 8000

# chromaDB setup
client = chromadb.PersistentClient(path = "G:\My Drive\MoonRakersAI\data")
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

def data_add(text, id, strength, result):
    collection.upsert(
        documents = [text],
        metadatas = [{"strength": strength, "result": result}],
        ids = [id],
    )

def data_add_response(id, result):
    collection.update(
        ids = [id],
        metadatas = [{"result": result}]
    )

def data_query(text, num_results):
    collection.query(
        query_texts = [text],
        n_results = num_results,
    )

def main():
    while True:
        print(collection.count())
        id = str(collection.count() + 1)

        block_text = ""
        csv_data = []

        input_text = input("You: ")
        if input_text.lower() == "quit":
            break

        data_add(input_text, id, "0.5", "unknown")

        relevant_query = data_query(input_text, 2)
        print(relevant_query)

        response = generate_response(input_text)
        data_add_response(id, response)

        block_text = "System response: " + response
        print(block_text)

if __name__ == "__main__":
    main()
    temp_id = str(collection.count())
    print(collection.get(
        ids = [temp_id],
        include = ["metadatas", "documents"] # shows first 5 data points
        )
    )
    collection.delete(
        where = {"strength": "0.5"}    # this will delete all of the data
    )