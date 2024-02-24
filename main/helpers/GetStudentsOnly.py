def Get_Students_only(collection):
    try:
        query = {"selected_role": 'student'}
        documents = collection.find(query)
        documents_list = [doc for doc in documents]
        return documents_list
    except Exception as e:
        return []