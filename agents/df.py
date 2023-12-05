import re

def data_add(text, id, strength, result, collection):
    collection.upsert(
        documents = [text],
        metadatas = [{"strength": strength, "result": result}],
        ids = [id],
    )

def data_add_response(id, result, collection):
    collection.update(
        ids = [id],
        metadatas = [{"result": result}]
    )

def data_query(text, num_results, collection):
    query = collection.query(
        query_texts = [text],
        n_results = num_results,
        include = ["metadatas"]
    )
    return query

def data_number(text):
    number = re.search(r"Task:\s*(\d+(?:\.\d+)?)", text)


    number = number.group(1) if number else None
    return number

def data_contract(text):
    contract = re.search(r"Contract:\s*(.+)", text)

    # Extracting the words
    contract = contract.group(1).strip() if contract else None
    return contract

def data_ship(text):
    ship_part = re.search(r"Ship:\s*(.+)", text)

    # Extracting the words
    ship_part = ship_part.group(1).strip() if ship_part else None
    return ship_part

def data_crew(text):
    crew = re.search(r"Crew:\s*(.+)", text)

    # Extracting the words
    crew = crew.group(1).strip() if crew else None
    return crew

def data_card(text):
    card = re.search(r"Card:\s*(.+)", text)

    # Extracting the words
    card = card.group(1).strip() if card else None
    return card