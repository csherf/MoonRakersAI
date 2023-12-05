import chromadb
from agents import guide
from agents import gptf
from agents import df
from agents import player
from agents import shopper
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

# chromaDB setup
client = chromadb.PersistentClient(path = "G:\My Drive\Moonrakers\MoonRakersAI\data")
embedding_function = OpenAIEmbeddingFunction(api_key = gptf.OPENAI_KEY, model_name = gptf.EMBEDDING_MODEL)
gsCollection = client.get_or_create_collection(name = "game_state", embedding_function = embedding_function)
csCollection = client.get_or_create_collection(name = "contract_state", embedding_function = embedding_function)
ssCollection = client.get_or_create_collection(name = "shop_state", embedding_function = embedding_function)

def main():
    print("gs collection count:" + str(gsCollection.count()))
    print("cs collection count:" + str(csCollection.count()))
    print("ss collection count:" + str(ssCollection.count()))
    gsid = str(gsCollection.count() + 1)
    csid = str(csCollection.count() + 1)
    ssid = str(ssCollection.count() + 1)


    # while 1 == 1: all of this would be in game loop
    replace_ability = 1

    #guide_response = guide.guide_run(gsCollection, gsid) #these are commented because I dont want to waste tokens and im testing other things
    #guide_choice = df.data_number(guide_response)
    #print(guide_response)
    #print(guide_choice) 

    guide_choice = 5

    if guide_choice == 1:
        # need to start off by using the script to play the contract, then roll the hazzard die

        #contract_choice = df.data_contract(guide_response)
        #print(contract_choice)
        player_response = player.player_run(csCollection, csid)
        print(player_response)
        player_choice = df.data_card(player_response)
        print(player_choice) # displays the chosen card to play (proof it works)

    elif guide_choice == 2.1:
        # stay at base +1 credit +2 objectives
        print("my bum ass chose number 2.1") # put in a script to update game state

    elif guide_choice == 2.2:
        # replace a contract, along with +1 credit +2 objectives
        print("my bum ass chose number 2.2")
        #contract_choice = df.data_contract(guide_response)
        #print(contract_choice)
        # use contract_choice to update game state

    elif guide_choice == 3.1 and replace_ability == 1:
        # pay 1 gold to replace any 1 contract from the dispatch abd you will then have the ability to attempt contracts afterwards or stay at base
        print("my bum ass chose number 3.1")
        #contract_choice = df.data_contract(guide_response)
        #print(contract_choice)
        replace_ability = 0
        #use contract_choice to update game state


    elif guide_choice == 3.2 and replace_ability == 1:
        # pay 1 gold to replace any 1 ship part from the dispatch abd you will then have the ability to attempt contracts afterwards or stay at base
        print("my bum ass chose number 3.2")
        #ship_choice = df.data_ship(guide_response)
        #print(ship_choice)
        replace_ability = 0
        #use ship_choice to update game state

    elif guide_choice == 3.3 and replace_ability == 1:
        # pay 1 gold to replace any 1 crew from the dispatch abd you will then have the ability to attempt contracts afterwards or stay at base
        print("my bum ass chose number 3.3")
        #crew_choice = df.data_crew(guide_response)
        #print(crew_choice)
        replace_ability = 0
        #use crew_choice to update game state

    else:
        print("my bum ass messed this up gimme redo")

    shopper_response = shopper.shopper_run(ssCollection,ssid)
    print(shopper_response)




if __name__ == "__main__":
    main()
    #gsCollection.delete(
    #    where = {"strength": "0.5"}    # this will delete all of the data and used for reset 
    #)