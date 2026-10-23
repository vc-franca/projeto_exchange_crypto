from banco import banco

from funcionalidades.senha_numerica import senha_numerica

def consultar_saldo():
    entrada_senha_numerica = int(input('Digite sua senha numérica: '))

    if entrada_senha_numerica != senha_numerica:
        return print('Senha incorreta. Acesso negado.')

    return print(f'''
    Nome: {banco['investidor']['nome']}
    CPF: {banco['investidor']['cpf']}
    
    Reais: {float(banco['investidor']['saldo']['reais']):.2f}
    Bitcoin: {float(banco['investidor']['saldo']['bitcoin']):.2f}
    Ethereum: {float(banco['investidor']['saldo']['ethereum']):.2f}
    Ripple: {float(banco['investidor']['saldo']['ripple']):.2f}
    ''')