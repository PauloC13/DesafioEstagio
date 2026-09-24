import json


def carregar_estoque(caminho):
    """
    Carrega os produtos do arquivo JSON.
    """

    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados["estoque"]


def buscar_produto(produtos, codigo_produto):
    """
    Busca um produto pelo código.
    """

    for produto in produtos:
        if produto["codigoProduto"] == codigo_produto:
            return produto

    return None


def movimentar_estoque(
    produto,
    quantidade,
    tipo,
    descricao,
    identificador
):
    """
    Realiza uma entrada ou saída de estoque.
    """

    if quantidade <= 0:
        raise ValueError(
            "A quantidade deve ser maior que zero."
        )

    if tipo == "entrada":
        produto["estoque"] += quantidade

    elif tipo == "saida":

        if quantidade > produto["estoque"]:
            raise ValueError(
                "Estoque insuficiente para realizar a saída."
            )

        produto["estoque"] -= quantidade

    else:
        raise ValueError(
            "Tipo de movimentação inválido. "
            "Use 'entrada' ou 'saida'."
        )

    return {
        "id": identificador,
        "codigoProduto": produto["codigoProduto"],
        "produto": produto["descricaoProduto"],
        "tipo": tipo,
        "descricao": descricao,
        "quantidade": quantidade,
        "estoqueFinal": produto["estoque"]
    }