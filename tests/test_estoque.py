import pytest

from src.estoque import movimentar_estoque


def criar_produto():
    return {
        "codigoProduto": 101,
        "descricaoProduto": "Caneta Azul",
        "estoque": 100
    }


def test_entrada_de_estoque():

    produto = criar_produto()

    resultado = movimentar_estoque(
        produto,
        20,
        "entrada",
        "Compra de mercadoria",
        1
    )

    assert resultado["estoqueFinal"] == 120


def test_saida_de_estoque():

    produto = criar_produto()

    resultado = movimentar_estoque(
        produto,
        30,
        "saida",
        "Venda de mercadoria",
        1
    )

    assert resultado["estoqueFinal"] == 70


def test_nao_permitir_estoque_negativo():

    produto = criar_produto()

    with pytest.raises(ValueError):

        movimentar_estoque(
            produto,
            150,
            "saida",
            "Venda",
            1
        )


def test_quantidade_deve_ser_positiva():

    produto = criar_produto()

    with pytest.raises(ValueError):

        movimentar_estoque(
            produto,
            0,
            "entrada",
            "Entrada",
            1
        )