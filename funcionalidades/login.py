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