import requests

url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita"
response = requests.get(url)

if response.status_code == 200:
    dados_thecocktaildb = response.json()
    for drinks in dados_thecocktaildb['drinks']:
        print(drinks)
else:
    print(f'código de erro: {response.status_code}')
