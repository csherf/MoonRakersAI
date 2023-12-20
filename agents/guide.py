from agents import df
from agents import gptf

def guide_run(collection, id):

    file1 = open('agents\\rules\\agent_rules\\guide_rules.txt')
    file2 = open('states\\live\\game_state.txt')
    file3 = open('agents\\rules\\game_rules\\game_rules.txt')
    file4 = open('states\\formats\\game_state_format.txt')
    guide_rules = file1.read()
    game_state = file2.read()
    game_rules = file3.read()
    game_state_format = file4.read()

    query_raw = df.data_query(game_state, 2, collection)
    query_input = str(query_raw["metadatas"])
    question = "Tell me what move to do next."

    input_text = []
    #input_text.append({"role": "system", "content": game_state_format})
    input_text.append({"role": "system", "content": guide_rules})
    input_text.append({"role": "user", "content": game_rules})
    input_text.append({"role": "user", "content": game_state})
    input_text.append({"role": "user", "content": question})
    #input_text.append({"role": "user", "content": query_input})

    output_text = gptf.gpt_response(input_text)
    df.data_add(game_state, id, "0.5", output_text, collection)

    print(input_text, file = open('agents\\previous_runthrough\\guide.txt', 'w'))
    print(output_text, file = open('agents\\previous_runthrough\\guide.txt', 'a'))

    return output_text