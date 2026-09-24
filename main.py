from datetime import date

from src.comissao import (
    carregar_vendas,
    calcular_comissoes
)

from src.estoque import (
    carregar_estoque,
    buscar_produto,
    movimentar_estoque
)

from src.juros import calcular_juros


def executar_comissao():
    print("=" * 40)
    print("1 - CÁLCULO DE COMISSÕES")
    print("=" * 40)

    vendas = carregar_vendas(
        "data/vendas.json"
    )

    comissoes = calcular_comissoes(vendas)

    for vendedor, comissao in comissoes.items():
        print(
            f"{vendedor}: R$ {comissao:.2f}"
        )


def executar_estoque():
    print("\n" + "=" * 40)
    print("2 - MOVIMENTAÇÃO DE ESTOQUE")
    print("=" * 40)

    produtos = carregar_estoque(
        "data/estoque.json"
    )

    produto = buscar_produto(
        produtos,
        101
    )

    resultado = movimentar_estoque(
        produto=produto,
        quantidade=20,
        tipo="saida",
        descricao="Venda de mercadoria",
        identificador=1
    )

    print(f"ID: {resultado['id']}")
    print(f"Produto: {resultado['produto']}")
    print(f"Tipo: {resultado['tipo']}")
    print(f"Descrição: {resultado['descricao']}")
    print(f"Quantidade: {resultado['quantidade']}")
    print(
        f"Estoque final: "
        f"{resultado['estoqueFinal']}"
    )


def executar_juros():
    print("\n" + "=" * 20)
    print("3 - CÁLCULO DE JUROS")
    print("=" * 20)

    valor = 1000.00

    data_vencimento = date(
        2026,
        9,
        12
    )

    resultado = calcular_juros(
        valor,
        data_vencimento
    )

    print(
        f"Valor original: "
        f"R$ {valor:.2f}"
    )

    print(
        f"Dias de atraso: "
        f"{resultado['dias_atraso']}"
    )

    print(
        f"Juros: "
        f"R$ {resultado['juros']:.2f}"
    )

    print(
        f"Valor total: "
        f"R$ {resultado['valor_total']:.2f}"
    )


def main():
    executar_comissao()
    executar_estoque()
    executar_juros()


if __name__ == "__main__":
    main()