import chromadb
from agents import guide
from agents import gptf
from agents import df
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

# chromaDB setup
client = chromadb.PersistentClient(path = "G:\My Drive\Moonrakers\MoonRakersAI\data")
embedding_function = OpenAIEmbeddingFunction(api_key = gptf.OPENAI_KEY, model_name = gptf.EMBEDDING_MODEL)
gsCollection = client.get_or_create_collection(name = "game_state", embedding_function = embedding_function)
csCollection = client.get_or_create_collection(name = "contract_state", embedding_function = embedding_function)

def main():
    print(gsCollection.count())
    gsid = str(gsCollection.count() + 1)
    csid = str(csCollection.count() + 1)


    # while 1 == 1: all of this would be in game loop
    replace_ability = 1
    response = guide.guide_run(gsCollection, gsid)
    print(response)

    guide_choice = df.data_number(response)

    #if guide_choice == 1:
        # player 
    #elif guide_choice == 2.1:
        # stay at base +1 credit +2 objectives
    #elif guide_choice == 2.2:
        # replace a contract, along with +1 credit +2 objectives
    #elif guide_choice == 3.1 & replace_ability == 1:
        # pay 1 gold to replace any 1 contract from the dispatch abd you will then have the ability to attempt contracts afterwards or stay at base
    #elif guide_choice == 3.2 & replace_ability == 1:
        # pay 1 gold to replace any 1 ship part from the dispatch abd you will then have the ability to attempt contracts afterwards or stay at base
    #elif guide_choice == 3.3 & replace_ability == 1:
        # pay 1 gold to replace any 1 crew from the dispatch abd you will then have the ability to attempt contracts afterwards or stay at base
    #else:
        # guide fucked up redo guide with same game state



if __name__ == "__main__":
    main()
    #gsCollection.delete(
    #    where = {"strength": "0.5"}    # this will delete all of the data and used for reset 
    #)