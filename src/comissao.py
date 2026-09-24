import json


def calcular_comissao(valor):
    """ Calcula a comissão de uma venda conforme as regras do desafio. """

    if valor < 100:
        return 0

    if valor < 500:
        return valor * 0.01

    return valor * 0.05


def calcular_comissoes(vendas):
    """   Calcula o total de comissão de cada vendedor. """

    comissoes = {}

    for venda in vendas:
        vendedor = venda["vendedor"]
        valor = venda["valor"]

        comissao = calcular_comissao(valor)

        comissoes[vendedor] = (
            comissoes.get(vendedor, 0) + comissao
        )

    return comissoes


def carregar_vendas(caminho):
    """ Carrega as vendas do arquivo JSON. """

    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados["vendas"]