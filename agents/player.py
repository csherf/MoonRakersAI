from agents import df
from agents import gptf

def player_run(collection, id):

    file1 = open('agents\\rules\\agent_rules\\player_rules.txt')
    file2 = open('contract_state.txt')
    file3 = open('agents\\rules\\game_rules\\contract_rules.txt')
    player_rules = file1.read()
    contract_state = file2.read()
    contract_rules = file3.read()

    query_raw = df.data_query(contract_state, 2, collection)
    query_input = str(query_raw["metadatas"])

    input_text = []
    input_text.append({"role": "system", "content": player_rules})
    input_text.append({"role": "system", "content": contract_rules})
    input_text.append({"role": "user", "content": contract_state})
    input_text.append({"role": "user", "content": query_input})

    output_text = gptf.gpt_response(input_text)
    df.data_add(contract_state, id, "0.5", output_text, collection)

    print(input_text, file = open('agents\\previous_runthrough\\player.txt', 'w'))
    print(output_text, file = open('agents\\previous_runthrough\\player.txt', 'a'))

    return output_text