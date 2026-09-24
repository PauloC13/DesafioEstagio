from datetime import date

from src.juros import calcular_juros


def test_calcular_juros():

    resultado = calcular_juros(
        1000,
        date(2026, 9, 20),
        date(2026, 9, 24)
    )

    assert resultado["dias_atraso"] == 4
    assert resultado["juros"] == 100
    assert resultado["valor_total"] == 1100


def test_valor_nao_vencido():

    resultado = calcular_juros(
        1000,
        date(2026, 9, 24),
        date(2026, 9, 24)
    )

    assert resultado["dias_atraso"] == 0
    assert resultado["juros"] == 0
    assert resultado["valor_total"] == 1000