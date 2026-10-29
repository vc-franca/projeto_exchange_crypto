import json

from banco import banco

def sacar_reais():
    entrada_saque = int(input('Digite a quantidade de R$ a ser sacada: '))

    if entrada_saque > banco['investidor']['saldo']['reais']:
        return print('Saldo insuficiente.')

    banco['investidor']['saldo']['reais'] -= entrada_saque

    with open('banco.json', 'w', encoding='utf-8') as file:
        json.dump(banco, file, indent=4, ensure_ascii=False)

    print('Saque realizado com sucesso!\n')

    return print(f'''
Saldo atualizado em R$: {float(banco['investidor']['saldo']['reais']):.2f}
    ''')
    