import openai

openai.api_key = "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"


game_rules = """
You are an AI designed to tell me the next move to make in a card game called Moonrakers. 
Your ultimate goal is to win the game in the least amount of turns possible.
I will give you the state of the game, and you will have to give me possible options that can be made next

The state of the game will be given in this format.


Deck: x cards, x damage, x energy, x thruster, x shield, x miss, x crew
Gold: x
Prestige: x

Game turn: x

Objectives: objective1, objective 2, ...

Ship Parts: part1, part2, part3, ...
Crew Members: crew1, crew2, crew3, ...

Current hand:   x cards, x damage, x energy, x thruster, x shield, x miss, x crew1/2/3 ...
Discard:        x cards, x damage, x energy, x thruster, x shield, x miss, x crew1/2/3 ...
Draw:           x cards, x damage, x energy, x thruster, x shield, x miss, x crew1/2/3 ...


Avaliable crew to buy: Myla Dystra, AT-0k, Ryle al Wren
Avaliable ship parts to buy: Duo 1000, Predator mk1, Symbiote 9000, Flash, The Persuer, Swarm mk1
Avaliable contracts: Fuel Shortage, Stim Run, Pirate Treasure, Darelict Planet, Core World Ace, Negotiation Insurance, Abandoned Vessel, Icarus Run

You must follow the following criteria :
1. You should act as a guide and lead me to make the best possible decisions in order to reach 10 prestige as fast as possible.
2. You need to imagine the scope of the entire game, not just the current move. 
3. Weight the values of taking risks, going for money based on current wealth, or going for prestige.
4. Every turn you have two possible moves you can take. 
    Option 1: Contract. In this option, you will take a contract and attempt it.
    Option 2: Stay at Base: In this option, you will take 1 credit and draw 2 objectives.
    Option 2.5: The same as option 2, but you can also replace a contract for free.

4. The response should follow a specific format, "Option 1 [contract_choice]" or "Option 2" or "Option 2.5 [contract_replace]"
5. Do not propose multiple tasks at the same time, and do not mention anything else.


You should only respond in the format as described below :
RESPONSE FORMAT:
Reasoning: Based on the information I listed above , do reasoning about what the next task should be should be around 1 paragraph of reasoning.
Task: The next task.

Here’s an example response:
Reasoning: I have no money, therefore I cannot buy anything and must do a contract. This contract has the highest probability of success. I do not have any ship parts or crewmembers to help in my contract. Therefore I cannot attempt high difficulty contracts.
Task: Option 1 [Stim Run]
"""

game_state = """
This is the State of the current game:

Deck: 10 cards, 2 damage, 3 energy, 2 thruster, 2 shield, 1 miss, 0 crew
Gold: 2
Prestige: 0

Game turn: 1

Objectives: Tinker, Utopia

Ship Parts: nil
Crew Members: nil

Current hand:   5 cards, 1 damage, 2 energy, 1 thruster, 2 shield, 0 miss, 0 crew
Discard:        3 cards, 1 damage, 0 energy, 1 thruster, 1 shield, 0 miss, 0 crew
Draw:           2 cards, 0 damage, 1 energy, 0 thruster, 0 shield, 1 miss, 0 crew


Avaliable crew to buy: Myla Dystra, AT-0k, Ryle al Wren
Avaliable ship parts to buy: Duo 1000, Predator mk1, Symbiote 9000, Flash, The Persuer, Swarm mk1
Avaliable contracts: Fuel Shortage, Stim Run, Pirate Treasure, Darelict Planet, Core World Ace, Negotiation Insurance, Abandoned Vessel, Icarus Run
"""

print(game_state)
messages = []
messages.append({"role": "system", "content": game_rules})
messages.append({"role": "user", "content": game_state})
completion = openai.ChatCompletion.create( 
    model="gpt-3.5-turbo",
    messages=messages)
reply = completion["choices"][0]["message"]["content"]
messages.append({"role": "assistant", "content": reply})
print("\n" + reply + "\n")