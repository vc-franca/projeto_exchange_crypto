import json

from banco import banco

def depositar_reais():
    entrada_reais = input('Digite a quantidade de R$ a ser depositada: ')

    banco['investidor']['saldo']['reais'] += int(entrada_reais)

    with open('banco.json', 'w', encoding='utf-8') as file:
        json.dump(banco, file, indent=4, ensure_ascii=False)

    return print('Deposito realizado com sucesso!\n')
    