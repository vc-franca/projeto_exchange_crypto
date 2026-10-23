from funcionalidades.login import logar
from funcionalidades.consultar_saldo import consultar_saldo
from funcionalidades.depositar_reais import depositar_reais

# print(banco['moedas']['ethereum']['cotacao']) formato pra acessar dados do JSON
# não sei que sentido faz ter um formato de lista, seria mais fácil com pontos

while True:
    # ---------------------------------------------------------------------------- #
    #                                     LOGIN                                    #
    # ---------------------------------------------------------------------------- #
    if not logar():
        break

    # ---------------------------------------------------------------------------- #
    #                                     MENU                                     #
    # ---------------------------------------------------------------------------- #
    print('''
1- consultar saldo
2- consultar extrato
3- depositar reais
4- sacar reais
5- comprar criptomoedas
6- vender criptomoedas
7- atualizar cotação
0- sair
''')

    entrada_opcao = input()

    match entrada_opcao:
        case '1':
            consultar_saldo()
        case '2':
            print('consultar extrato')
            break
        case '3':
            depositar_reais()
            break
        case '4':
            print('sacar reais')
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
        case '0':
            print('sair')
            break