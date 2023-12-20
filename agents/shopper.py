from agents import df
from agents import gptf

def shopper_run(collection, id):

    file1 = open('agents\\rules\\agent_rules\\shopper_rules.txt')
    file2 = open('states\\live\\shop_state.txt')
    file3 = open('agents\\rules\\game_rules\\game_rules.txt')
    file4 = open('states\\formats\\shop_state_format.txt')
    shopper_rules = file1.read()
    shop_state = file2.read()
    game_rules = file3.read()
    shop_state_format = file4.read()

    query_raw = df.data_query(shop_state, 2, collection)
    query_input = str(query_raw["metadatas"])

    input_text = []
    #input_text.append({"role": "system", "content": shop_state_format})
    input_text.append({"role": "system", "content": shopper_rules})
    input_text.append({"role": "system", "content": game_rules})
    input_text.append({"role": "user", "content": shop_state})
    #input_text.append({"role": "user", "content": query_input})

    output_text = gptf.gpt_response(input_text)
    df.data_add(shop_state, id, "0.5", output_text, collection)

    print(input_text, file = open('agents\\previous_runthrough\\shopper.txt', 'w'))
    print(output_text, file = open('agents\\previous_runthrough\\shopper.txt', 'a'))

    return output_text