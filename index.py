import json

with open('banco.json', 'r', encoding='utf-8') as file:
    banco = json.load(file)

# print(banco['moedas']['ethereum']['cotacao']) formato pra acessar dados do JSON
# não sei que sentido faz ter um formato de lista, seria mais fácil com pontos

while True:
    # ---------------------------------------------------------------------------- #
    #                                     LOGIN                                    #
    # ---------------------------------------------------------------------------- #
    dados_login = ('12345678900', 'senhasenha')

    entrada_investidor = input('Digite o CPF: ')
    entrada_senha = input('Digite a senha: ')

    def logar():        
        if entrada_investidor != dados_login[0]:
            return print('CPF não encontrado')

        if entrada_senha != dados_login[1]:
            return print('senha incorreta')

        print('logado com sucesso\n')

        print("""
        1- consultar saldo
        2- consultar extrato
        3- depositar
        4- sacar
        5- comprar criptomoedas
        6- vender criptomoedas
        7- atualizar cotação
        8- sair
        """)

    logar()

    # ---------------------------------------------------------------------------- #
    #                                     MENU                                     #
    # ---------------------------------------------------------------------------- #
    entrada_opcao = input()

    match entrada_opcao:
        case '1':
            print('consultar saldo')
        case '2':
            print('consultar extrato')
        case '3':
            print('depositar')
        case '4':
            print('sacar')
        case '5':
            print('comprar criptomoedas')
        case '6':
            print('vender criptomoedas')
        case '7':
            print('atualizar cotação')
        case '8':
            print('sair')
            break