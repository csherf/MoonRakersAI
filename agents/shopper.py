import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ['OPENAI_KEY']

file1 = open('agents\\rules\\shopper_rules.txt')
file2 = open('game_state.txt')
shopper_rules = file1.read()
game_state = file2.read()

messages = []
messages.append({"role": "system", "content": shopper_rules})
messages.append({"role": "user", "content": game_state})
completion = openai.ChatCompletion.create( 
    model="gpt-3.5-turbo",
    messages=messages)
reply = completion["choices"][0]["message"]["content"]
messages.append({"role": "assistant", "content": reply})
print("\n" + reply + "\n")