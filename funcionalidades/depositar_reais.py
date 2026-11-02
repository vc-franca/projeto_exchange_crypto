import json
from banco import banco

def depositar_reais():
    entrada_reais = int(input('Digite a quantidade de R$ a ser depositada: '))

    if entrada_reais <= 0:
        return print('Valor inválido.')

    banco['investidor']['saldo']['reais'] += entrada_reais

    with open('banco.json', 'w', encoding='utf-8') as file:
        json.dump(banco, file, indent=4, ensure_ascii=False)

    print('Saque realizado com sucesso!\n')

    return print(f'''
Saldo atualizado em R$: {float(banco['investidor']['saldo']['reais']):.2f}
    ''')
    