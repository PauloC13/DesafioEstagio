from src.comissao import (
    carregar_vendas,
    calcular_comissoes
)


def main():
    vendas = carregar_vendas(
        "data/vendas.json"
    )

    comissoes = calcular_comissoes(vendas)

    print("=" * 20)
    print("CÁLCULO DE COMISSÕES")
    print("=" * 20)

    for vendedor, comissao in comissoes.items():
        print(
            f"{vendedor}: R$ {comissao:.2f}"
        )


if __name__ == "__main__":
    main()