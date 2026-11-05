import random
import json
from banco import banco

def atualizar_cotacao():
    for moeda, dados in banco['moedas'].items():

        cotacao = dados['cotacao']

        variacao = random.uniform(-0.05, 0.05)

        cotacao_atualizada = cotacao + (cotacao * variacao)

        dados['cotacao'] = round(cotacao_atualizada, 2)

        with open('banco.json', 'w', encoding='utf-8') as file:
            json.dump(banco, file, indent=4, ensure_ascii=False)

        print(f'{moeda.capitalize()}: R$ {dados["cotacao"]:.2f}')

    return 