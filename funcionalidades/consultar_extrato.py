from banco import banco

from funcionalidades.senha_numerica import senha_numerica

def consultar_extrato():
    entrada_senha_numerica = int(input('Digite sua senha numérica: '))
    
    if entrada_senha_numerica != senha_numerica:
        return print('Senha incorreta. Acesso negado.')

    extratos = banco['investidor']['extratos']

    extrato_atualizado = ''

    for i in range(len(extratos['data'])):
        data = extratos['data'][i]
        operacao = extratos['operacao'][i]
        valor = extratos['valor'][i]
        moeda = extratos['moeda'][i]
        cotacao = extratos['cotacao'][i]
        taxa = extratos['taxa'][i]
        valor_reais = extratos['valor_reais'][i]
        valor_bitcoin = extratos['valor_bitcoin'][i]
        valor_ethereum = extratos['valor_ethereum'][i]
        valor_ripple = extratos['valor_ripple'][i]

        extrato_atualizado += f'''
    {data} {operacao} {valor} {moeda} CT: {cotacao} TX: {taxa} REAL: {valor_reais} BTC {valor_bitcoin} ETH: {valor_ethereum} XRP: {valor_ripple}
'''

    return print(f'''
    Nome: {banco['investidor']['nome']}
    CPF: {banco['investidor']['cpf']}

    {extrato_atualizado}
''')