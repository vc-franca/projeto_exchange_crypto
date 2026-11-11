import json
from banco import banco
from datetime import datetime

def depositar_reais():
    entrada_reais = int(input('Digite a quantidade de R$ a ser depositada: '))

    if entrada_reais <= 0:
        return print('Valor inválido.')

    banco['investidor']['saldo']['reais'] += entrada_reais

    # ---------------------------------------------------------------------------- #
    #                               atualizar extrato                              #
    # ---------------------------------------------------------------------------- #
    extratos = banco['investidor']['extratos']

    extratos['data'].append(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    extratos['operacao'].append('+')
    extratos['valor'].append(entrada_reais)
    extratos['moeda'].append('reais')
    extratos['cotacao'].append(1)
    extratos['taxa'].append(0)
    extratos['valor_reais'].append(entrada_reais)
    extratos['valor_bitcoin'].append(0.0)
    extratos['valor_ethereum'].append(0.0)
    extratos['valor_ripple'].append(0.0)

    with open('banco.json', 'w', encoding='utf-8') as file:
        json.dump(banco, file, indent=4, ensure_ascii=False)

    print('Depósito realizado com sucesso!\n')

    return print(f'''
Saldo atualizado em R$: {float(banco['investidor']['saldo']['reais']):.2f}
    ''')
    