
def search_book(query = None):
    queries_list = []
    queries = query.split(" ")
    for q in queries:
        queries_list.append(q)
    return list(set(queries_list))


a =search_book("isaac is a chinue")
print(a)