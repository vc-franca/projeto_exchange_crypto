from funcionalidades.login import logar

from funcionalidades.consultar_saldo import consultar_saldo
from funcionalidades.depositar_reais import depositar_reais
from funcionalidades.sacar_reais import sacar_reais
from funcionalidades.comprar_cripto import comprar_cripto
from funcionalidades.vender_cripto import vender_cripto
from funcionalidades.atualizar_cotacao import atualizar_cotacao
from funcionalidades.consultar_extrato import consultar_extrato

# print(banco['moedas']['ethereum']['cotacao']) formato pra acessar dados do JSON
# não sei que sentido faz ter um formato de lista, seria mais fácil com pontos

def menu():
    # ---------------------------------------------------------------------------- #
    #                                     LOGIN                                    #
    # ---------------------------------------------------------------------------- #
    if not logar():
        return

    while True:

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
                consultar_extrato()
            case '3':
                depositar_reais()
            case '4':
                sacar_reais()
            case '5':
                comprar_cripto()
            case '6':
                vender_cripto()
            case '7':
                atualizar_cotacao()
            case '0':
                print('sair')
                break

menu()