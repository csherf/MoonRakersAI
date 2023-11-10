import openai

openai.api_key = "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"

file1 = open('rules\\guide_rules.txt')
file2 = open('..\\game_state.txt')
guide_rules = file1.read()
game_state = file2.read()

messages = []
messages.append({"role": "system", "content": guide_rules})
messages.append({"role": "user", "content": game_state})
completion = openai.ChatCompletion.create( 
    model="gpt-3.5-turbo",
    messages=messages)
reply = completion["choices"][0]["message"]["content"]
messages.append({"role": "assistant", "content": reply})
print("\n" + reply + "\n")