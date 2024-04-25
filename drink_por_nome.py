import requests


# Essa função percorre letra por letra, num range de a até z e usa cada letra como parâmetro para a função abaixo.
def drink_por_nome():
    for letra in range(ord('a'), ord('z')+1):  # Percorre de 'a' a 'z'
        letra = chr(letra)  # Converte o número ASCII de volta para a letra
        drink_por_letra(letra)


# Recebe letra por letra como parâmetro e adiciona na url de pesquisa numa API de bebidas e drinks.
def drink_por_letra(letra):
    url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?f={letra}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Caso a chave drinks esteja em data, e a chave drinks não é NONE ou NULL, ele efetua o script.
        # Caso contrário ele vai para o else, e printa a mensagem que nenhum drink foi encontrado.
        if "drinks" in data and data["drinks"] is not None:  # Verifica se a chave "drinks" existe e não é None
            drinks = []
            for drink in data["drinks"]:
                drinks.append(drink["strDrink"])

            # Nessa parte é onde se decide o que fazer com os dados de nomes retirados de todos os drinks.
            # Nesse caso apenas imprime a lista drinks a cada loop.
            # --------------------------------------------------
            print(f"Drinks com a letra '{letra}':\n", drinks)
            print()
            # --------------------------------------------------

        else:
            print(f"Nenhum drink encontrado com a letra '{letra}'.")
            print()
    else:
        print("Erro ao acessar a API:", response.status_code)
