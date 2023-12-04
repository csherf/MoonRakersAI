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
    number = re.search(r"Task:\s*(\d+\.\d+)", text)

    number = number.group(1) if number else None
    return number