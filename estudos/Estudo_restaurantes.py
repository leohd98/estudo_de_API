# Importa a library requests
import requests

# Efetua a requisição de acesso da API em arquivo JSON usando requests.get
url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
requisicao = requests.get(url)

# Passa por um filtro que determina duas respostas diferentes, caso a requisição tenha sucesso ou não.
if requisicao.status_code == 200:

    # poe o jason dentro da variavel lista_de_dicionarios que é uma lista contendo diversos dicionários nesse caso.
    lista_de_dicionarios = requisicao.json()

    # cria uma lista vazia na variável restaurantes
    restaurantes = []

    # faz um loop através dos dicionários que estão dentro de uma lista em lista_de_dicionários.
    for dicionarios in lista_de_dicionarios:

        # coloca o conteúdo da chave Company que retém o nome do restaurante dentro da variável nome_do_restaurante a cada loop do for.
        nome_do_restaurante = dicionarios['Company']

        # faz o teste a cada loop, se o nome_do_restaurante não estiver dentro da lista vazia restaurantes ele faz algo.
        # caso o nome_do_restaurante já esteja na lista restaurantes, então nao acontece nada, e pula pro próximo.
        if nome_do_restaurante not in restaurantes:

            #adiciona na lista vazia o conteúdo da chave company, que é o nome dos restaurantes.
            restaurantes.append(nome_do_restaurante)

    print(restaurantes)
else:
    print(f'Deu RUIM, código de erro: {requisicao.status_code}')
