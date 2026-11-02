import json
from banco import banco

from funcionalidades.senha_numerica import senha_numerica

def comprar_cripto():
    entrada_senha_numerica = int(input('Digite sua senha numérica: '))

    if entrada_senha_numerica != senha_numerica:
        return print('Senha incorreta. Acesso negado.')
    
    print(f'''
    Cotações das criptomoedas: 

    Bitcoin: R$ {float(banco['moedas']['bitcoin']['cotacao']):.2f}
    Ethereum: R$ {float(banco['moedas']['ethereum']['cotacao']):.2f}
    Ripple: R$ {float(banco['moedas']['ripple']['cotacao']):.2f}
''')

    entrada_moeda = input('Digite qual criptomoeda desejas comprar em letras minúsculas: ')

    entrada_quantidade = int(input(f'Digite a quantidade de {entrada_moeda} a ser comprada: '))

    if entrada_quantidade <= 0:
        return print('Quantidade inválida')

    banco['investidor']['saldo'][entrada_moeda] += entrada_quantidade

    with open('banco.json', 'w', encoding='utf-8') as file:
        json.dump(banco, file, indent=4, ensure_ascii=False)

    return print(f'Saldo atualizado: {float(banco['investidor']['saldo'][entrada_moeda]):.2f}')