from datetime import date


TAXA_DIARIA = 0.025


def calcular_juros(
    valor,
    data_vencimento,
    data_atual=None
):
    """
    Calcula os juros de 2,5% ao dia sobre um valor vencido.

    data_vencimento e data_atual devem ser objetos date.
    """

    if valor < 0:
        raise ValueError(
            "O valor não pode ser negativo."
        )

    if data_atual is None:
        data_atual = date.today()

    dias_atraso = (
        data_atual - data_vencimento
    ).days

    if dias_atraso <= 0:
        return {
            "dias_atraso": 0,
            "juros": 0,
            "valor_total": valor
        }

    juros = valor * TAXA_DIARIA * dias_atraso

    return {
        "dias_atraso": dias_atraso,
        "juros": juros,
        "valor_total": valor + juros
    }