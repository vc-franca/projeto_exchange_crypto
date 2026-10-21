from banco import banco

dados_login = (banco['investidor']['cpf'], banco['investidor']['senha'])

entrada_investidor = input('Digite o CPF: ')
entrada_senha = input('Digite a senha: ')

def logar():        
    if entrada_investidor != dados_login[0]:
        return print('CPF não encontrado')

    if entrada_senha != dados_login[1]:
        return print('senha incorreta')

    print('logado com sucesso!\n')

    return True