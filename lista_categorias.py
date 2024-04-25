import requests


def lista_categorias():
    url = "https://www.thecocktaildb.com/api/json/v1/1/list.php?c=list"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for categorias in data["drinks"]:
            print(categorias["strCategory"])
    else:
        print("Erro ao acessar a API:", response.status_code)
