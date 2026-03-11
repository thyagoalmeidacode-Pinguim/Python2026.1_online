# Aula: Variáveis, Tipos, Operadores, Conversão e Formas de Exibir Valores em Python

## Objetivos

Ao final da aula, o aluno será capaz de:

* Entender o conceito de **variáveis**
* Conhecer os **principais tipos de dados**
* Diferenciar **linguagens fortemente e fracamente tipadas**
* Utilizar **operadores matemáticos e lógicos**
* **Converter tipos de dados** com `int()`, `float()` e `str()`
* Exibir valores usando **formas de concatenação e f-strings**
* Criar um **sistema simples de cadastro de alunos**

---

## 1️⃣ Conceito de Variável

Variável é como uma **vaga de estacionamento**:

* **Vaga** = nome da variável
* **Carro** = valor armazenado
* **Trocar o carro** = mudar o valor da variável

```python
vaga1 = "Carro vermelho"
vaga2 = "Carro azul"
vaga3 = None  # vaga vazia
```

---

## 2️⃣ Tipos de Dados

| Tipo  | Exemplo |
| ----- | ------- |
| int   | 25      |
| float | 3.14    |
| str   | "Ana"   |
| bool  | True    |

```python
idade = 20        # int
altura = 1.75     # float
nome = "João"     # str
aprovado = True   # bool

print(type(idade))
```

---

## 3️⃣ Conversão de Tipos (`int()`, `float()`, `str()`)

Às vezes precisamos **mudar o tipo de dado** de uma variável.

* **`int()`** → converte para número inteiro
* **`float()`** → converte para número decimal
* **`str()`** → converte para texto

### Exemplos:

```python
numero1 = input("Digite um número: ")  # input retorna str
numero2 = input("Digite outro número: ")

# Convertendo para int
numero1 = int(numero1)
numero2 = int(numero2)

soma = numero1 + numero2
print("Soma:", soma)
```

```python
preco = 19.90
print("O preço é: " + str(preco))  # Converte float para string
```

---

## 4️⃣ Operadores Matemáticos e Lógicos

### Matemáticos

| Operador | Função        |
| -------- | ------------- |
| +        | soma          |
| -        | subtração     |
| *        | multiplicação |
| /        | divisão       |
| %        | resto         |
| **       | potência      |

### Lógicos

| Operador | Função         |
| -------- | -------------- |
| ==       | igual          |
| !=       | diferente      |
| >        | maior          |
| <        | menor          |
| >=       | maior ou igual |
| <=       | menor ou igual |
| and      | e lógico       |
| or       | ou lógico      |
| not      | negação        |

Exemplo:

```python
idade = 20
tem_carteira = True

print(idade >= 18 and tem_carteira)
```

---

## 5️⃣ Formas de Exibir Valores e Concatenação

Suponha:

```python
cor_camisa = "azul"
nome = "Maria"
idade = 20
```

### Forma 1: Vírgula no print

```python
print("Primeira forma - A cor da camisa é:", cor_camisa, nome, "e a idade é", idade)
```

### Forma 2: Concatenação com `+`

```python
print("Segunda forma - A cor da camisa é: " + cor_camisa + " " + nome + " e a idade é " + str(idade))
```

### Forma 3: f-strings (Python ≥3.6)

```python
print(f"Terceira forma - A cor da camisa é {cor_camisa} {nome} e a idade é {idade}")
```

### Forma 4: `.format()`

```python
print("Quarta forma - A cor da camisa é: {} {} e a idade é {}".format(cor_camisa, nome, idade))
```

---

## 6️⃣ Exercícios com Conversão e Exibição

1. Solicite ao usuário **nome, idade e altura** e exiba usando **as quatro formas de print**.

   * Converta idade para **int** e altura para **float**
2. Solicite dois números, some-os, e exiba o resultado usando **todas as formas de concatenação**.
3. Crie uma variável `nota`, peça ao usuário, e mostre se é maior que 7 usando **operadores lógicos e conversão de tipo**.
4. Crie variáveis `idade` e `tem_carteira` e exiba se pode dirigir usando **todas as formas de exibição**.

---