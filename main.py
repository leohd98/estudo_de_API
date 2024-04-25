from drink_por_nome import *
from lista_categorias import *


def fechar_programa():
    print('END OF PROGRAM')


def voltar_ao_menu():
    print()
    input('Digite qualquer tecla para voltar ao menu: ')
    for linha in range(90):
        print()
    main()


def define_escolha(escolha):

    # Escolha 1
    if escolha == '1':
        print('--------------------------------------------------')
        print('Opção escolhida: Listar todos os drinks da api.')
        print()
        drink_por_nome()
        voltar_ao_menu()

    # Escolha 2
    elif escolha == '2':
        print('--------------------------------------------------')
        print('Opção escolhida: Listar drinks por primeira letra.')
        while True:  # Loop infinito até que a escolha seja válida
            letra = input('Digite a letra que deseja: ')
            if letra.isalpha() and len(letra) == 1:
                print()
                drink_por_letra(letra.lower())
                voltar_ao_menu()
            else:
                print()
                print("Escolha inválida! Por favor, escolha apenas uma letra.")

    # Escolha 3
    elif escolha == '3':
        print('--------------------------------------------------')
        print('Opção escolhida: Listar categorias de drink.')
        lista_categorias()
        voltar_ao_menu()

    # Escolha 4
    elif escolha == '4':
        print('Opção 4 selecionada: Fechar Programa.')
        fechar_programa()

    else:
        print('ERROR X_X')
        voltar_ao_menu()


def exibir_menu():
    # Printa o menu no terminal.
    print('''
    MENU BOATE FLOOR
    ----------------
    1. Listar todos os drinks da api.
    2. Listar drinks por primeira letra.
    3. Listar categorias de drink.
    4. Fechar Programa.
    ''')
    # Faz um teste para determinar se a escolha é válida ou não.
    while True:  # Loop infinito até que a escolha seja válida
        escolha = input('Escolha: ')
        if escolha.isdigit() and 1 <= int(escolha) <= 4:
            return escolha
        else:
            print("Escolha inválida! Por favor, escolha um número de 1 a 4.")


# Determina a ordem que as funções do programa executam.
def main():
    escolha = exibir_menu()  # Armazena na variável 'escolha' o valor retornado da função exibir_menu().
    define_escolha(escolha)  # Usa o valor retornado da função exibir_menu() como parâmetro na função define_escolha().


# Determina que esse script está sendo executado como o programa principal.
if __name__ == '__main__':
    main()
