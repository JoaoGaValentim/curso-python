def add_peoples(name, data=None):
    # criamos listas independentes
    # assim não mudamos o valor
    if data is None:
        data = []
    data.append(name)
    return data


peoples = add_peoples("João")
add_peoples("Clara", peoples)
print(peoples)

peoples_shop = add_peoples("Ana")
add_peoples("Laura", peoples_shop)
print(peoples_shop)
