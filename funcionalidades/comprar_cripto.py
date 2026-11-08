import json
from banco import banco
from datetime import datetime

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

    banco['investidor']['saldo'][entrada_moeda] += entrada_quantidade - (entrada_quantidade * banco['moedas'][entrada_moeda]['taxa_compra'])

    # ---------------------------------------------------------------------------- #
    #                               atualizar extrato                              #
    # ---------------------------------------------------------------------------- #
    extratos = banco['investidor']['extratos']
    cotacao = banco['moedas'][entrada_moeda]['cotacao']

    valor_reais = entrada_quantidade * cotacao

    extratos['data'].append(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    extratos['operacao'].append('+')
    extratos['valor'].append(entrada_quantidade)
    extratos['moeda'].append(entrada_moeda)
    extratos['cotacao'].append(cotacao)
    extratos['taxa'].append(banco['moedas'][entrada_moeda]['taxa_compra'])
    extratos['valor_reais'].append(valor_reais)
    extratos['valor_bitcoin'].append(valor_reais if entrada_moeda == 'bitcoin' else 0.0)
    extratos['valor_ethereum'].append(valor_reais if entrada_moeda == 'ethereum' else 0.0)
    extratos['valor_ripple'].append(valor_reais if entrada_moeda == 'ripple' else 0.0)


    with open('banco.json', 'w', encoding='utf-8') as file:
        json.dump(banco, file, indent=4, ensure_ascii=False)

    return print(f'Saldo atualizado: {float(banco['investidor']['saldo'][entrada_moeda]):.2f}')