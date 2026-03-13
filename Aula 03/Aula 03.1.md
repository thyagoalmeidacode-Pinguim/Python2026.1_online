# Estruturas de Decisão em Python

## Introdução

Estruturas de decisão servem para que nossa aplicação tome uma decisão
baseada em uma condição.

A aplicação analisa uma condição e escolhe qual caminho seguir.

### Classificações

-   **Simples** -- Somente uma única resposta\
-   **Composta** -- Duas respostas possíveis\
-   **Encadeada** -- Possui várias respostas\
-   **Match Case** -- Escolhe uma opção entre vários casos

------------------------------------------------------------------------

# Decisão Simples

Na decisão simples existe apenas **uma resposta possível**.

``` python
print("Decisão Simples")

idade = 18

if (idade >= 18):
    print("Você é maior de idade")
```

### Explicação

-   `if` verifica a condição
-   Se for **verdadeira**, o código é executado
-   Se for **falsa**, nada acontece

------------------------------------------------------------------------

# Decisão Composta

Na decisão composta existem **duas respostas possíveis**.

``` python
print("Decisão Composta")

idade = 15

if (idade >= 18):
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
```

### Explicação

-   `if` → executa se a condição for verdadeira
-   `else` → executa se a condição for falsa

------------------------------------------------------------------------

# Decisão Encadeada

Na decisão encadeada existem **várias verificações possíveis**.

``` python
print("Decisão Encadeada")

fruta = "Laranja"

if fruta == "banana":
    print("Fica bom com mel")

elif fruta == "Laranja":
    print("A melhor fruta")

elif fruta == "Maracuja":
    print("Fica em mousse")

else:
    print("Não tenho resposta")
```

### Explicação

-   `if` → primeira condição
-   `elif` → outras verificações
-   `else` → executado caso nenhuma condição seja verdadeira

------------------------------------------------------------------------

# Match Case (Python 3.10+)

O **match case** funciona de forma parecida com o **switch case** de
outras linguagens.

Ele permite verificar vários casos de forma organizada.

``` python
print("Match Case")

fruta = "banana"

match fruta:

    case "banana":
        print("Fica bom com mel")

    case "laranja":
        print("Boa para suco")

    case "maracuja":
        print("Boa para mousse")

    case _:
        print("Fruta não cadastrada")
```

### Explicação

-   `match` → variável que será analisada
-   `case` → valores possíveis
-   `_` → funciona como **default** (caso nenhum valor seja encontrado)

------------------------------------------------------------------------

# Exemplo com números

``` python
print("Exemplo com números")

numero = 2

match numero:

    case 1:
        print("Número um")

    case 2:
        print("Número dois")

    case 3:
        print("Número três")

    case _:
        print("Número não encontrado")
```

------------------------------------------------------------------------

# Comparação das estruturas

  Estrutura          Uso
  ------------------ -------------------------------
  if                 Verificar uma condição
  if / else          Duas possibilidades
  if / elif / else   Várias possibilidades
  match case         Escolher entre vários valores
