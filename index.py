import json
from funcionalidades.login import logar

with open('banco.json', 'r', encoding='utf-8') as file:
    banco = json.load(file)

# print(banco['moedas']['ethereum']['cotacao']) formato pra acessar dados do JSON
# não sei que sentido faz ter um formato de lista, seria mais fácil com pontos

while True:
    # ---------------------------------------------------------------------------- #
    #                                     LOGIN                                    #
    # ---------------------------------------------------------------------------- #
    logar()

    # ---------------------------------------------------------------------------- #
    #                                     MENU                                     #
    # ---------------------------------------------------------------------------- #
    entrada_opcao = input()

    match entrada_opcao:
        case '1':
            print('consultar saldo')
            break
        case '2':
            print('consultar extrato')
            break
        case '3':
            print('depositar')
            break
        case '4':
            print('sacar')
            break
        case '5':
            print('comprar criptomoedas')
            break
        case '6':
            print('vender criptomoedas')
            break
        case '7':
            print('atualizar cotação')
            break
        case '8':
            print('sair')
            break