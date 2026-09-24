# Desafio de Estágio

Solução desenvolvida para o desafio técnico de estágio, utilizando Python.

O projeto possui três exercícios envolvendo cálculo de comissão, movimentação de estoque e cálculo de juros por atraso.

## Tecnologias utilizadas

 Python 3
 JSON
 Pytest
 Git e GitHub

## 1. Cálculo de comissão

O programa lê os registros de vendas armazenados em `data/vendas.json` e calcula a comissão de cada vendedor.

### Regras

 Valor da venda             Comissão 
 Abaixo de R$ 100,00               0% 
 De R$ 100,00 até R$ 499,99        1% 
 A partir de R$ 500,00             5%

As comissões das diferentes vendas são acumuladas por vendedor.

## 2. Movimentação de estoque

O programa permite realizar movimentações de entrada e saída dos produtos cadastrados em data/estoque.json.

Cada movimentação possui:

 Identificador único;
 Código e descrição do produto;
 Tipo da movimentação;
 Descrição da movimentação;
 Quantidade movimentada;
 Estoque final.

Também são realizadas validações para evitar:

 Quantidade menor ou igual a zero;
 Tipo de movimentação inválido;
 Saída maior que a quantidade disponível em estoque;
 Produto inexistente.

## 3. Cálculo de juros

O programa calcula os juros de uma determinada quantia de acordo com a quantidade de dias em atraso.

A taxa utilizada é de:

**2,5% ao dia.**

Quando o vencimento ainda não ocorreu, nenhum juros é aplicado.

## Como executar

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

Depois, entre na pasta do projeto:

```bash
cd desafio-estagio
```

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 3. Executar o programa

```bash
python main.py
```

## Testes

Os testes foram desenvolvidos utilizando o Pytest.

Para executar todos os testes:

```bash
python -m pytest
```

Para executar os testes individualmente:

```bash
python -m pytest tests/test_comissao.py
```

```bash
python -m pytest tests/test_estoque.py
```

```bash
python -m pytest tests/test_juros.py
```

## Objetivo

O objetivo do projeto é demonstrar a aplicação de lógica de programação, manipulação de arquivos JSON, organização de código, tratamento de erros e testes automatizados na resolução das regras propostas no desafio.

##
Autor - Paulo Cavalcante
