from src.comissao import calcular_comissao


def test_venda_abaixo_de_100():
    assert calcular_comissao(50) == 0


def test_venda_de_100():
    assert calcular_comissao(100) == 1


def test_venda_abaixo_de_500():
    assert calcular_comissao(200) == 2


def test_venda_de_500():
    assert calcular_comissao(500) == 25


def test_venda_acima_de_500():
    assert calcular_comissao(1000) == 50