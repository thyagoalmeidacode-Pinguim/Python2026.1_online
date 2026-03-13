# Aula: Operadores Matemáticos e Lógicos em Python

## 1. Introdução

Em Python, usamos **operadores matemáticos** para cálculos e **operadores lógicos** para trabalhar com valores booleanos (True/False). Nesta aula, vamos explorar ambos **sem usar estruturas condicionais**.

---

## 2. Operadores Matemáticos

| Operador | Descrição        | Exemplo             |
| -------- | ---------------- | ------------------- |
| `+`      | Adição           | `5 + 3` → `8`       |
| `-`      | Subtração        | `10 - 4` → `6`      |
| `*`      | Multiplicação    | `6 * 7` → `42`      |
| `/`      | Divisão (float)  | `10 / 3` → `3.3333` |
| `//`     | Divisão inteira  | `10 // 3` → `3`     |
| `%`      | Resto da divisão | `10 % 3` → `1`      |
| `**`     | Exponenciação    | `2 ** 3` → `8`      |

### Exemplos:

```python
# Adição e Subtração
a = 10
b = 3
print("Soma:", a + b)        # 13
print("Subtração:", a - b)   # 7

# Multiplicação e Divisão
print("Multiplicação:", a * b)  # 30
print("Divisão:", a / b)        # 3.3333
print("Divisão inteira:", a // b) # 3

# Resto e Potência
print("Resto:", a % b)   # 1
print("Potência:", a ** b) # 1000
```

---

## 3. Operadores de Atribuição

```python
x = 5
x += 3   # x = x + 3
print(x)  # 8

x *= 2   # x = x * 2
print(x)  # 16

x **= 2  # x elevado ao quadrado
print(x)  # 256
```

---

## 4. Operadores Lógicos

| Operador | Significado | Exemplo                  |
| -------- | ----------- | ------------------------ |
| `and`    | E lógico    | `True and False` → False |
| `or`     | OU lógico   | `True or False` → True   |
| `not`    | Negação     | `not True` → False       |

### Exemplos:

```python
x = True
y = False

print("x and y:", x and y)   # False
print("x or y:", x or y)     # True
print("not x:", not x)       # False
```

Podemos combinar operadores lógicos com comparações:

```python
a = 10
b = 5
c = 7

print("a > b:", a > b)           # True
print("b == c:", b == c)         # False
print("c <= a:", c <= a)         # True

print("a > b and c > b:", a > b and c > b) # True
print("a > b or b > c:", a > b or b > c)   # True
print("not(a == b):", not(a == b))         # True
```

---

## 5. Operadores de Comparação

| Operador | Descrição      | Exemplo          |
| -------- | -------------- | ---------------- |
| `==`     | Igual a        | `5 == 5` → True  |
| `!=`     | Diferente      | `5 != 3` → True  |
| `>`      | Maior que      | `7 > 10` → False |
| `<`      | Menor que      | `3 < 8` → True   |
| `>=`     | Maior ou igual | `5 >= 5` → True  |
| `<=`     | Menor ou igual | `4 <= 7` → True  |

Exemplo direto:

```python
x = 15
y = 10

resultado1 = x == y
resultado2 = x != y
resultado3 = x > y
resultado4 = x < y

print(resultado1, resultado2, resultado3, resultado4)  # False True True False
```

---

## 6. Combinações Matemáticas e Lógicas

```python
nota1 = 8
nota2 = 6
nota3 = 7

media = (nota1 + nota2 + nota3) / 3
print("Média:", media)                # 7.0
print("Média >= 7:", media >= 7)     # True
print("Média < 5 or nota3 > 6:", media < 5 or nota3 > 6)  # True
print("not(media < 7):", not(media < 7))  # True
```

---

## 7. Desafios para Prática (Sem if)

1. Crie um prohrama que solicite dois numeros ao usuario,  em seguida exiba a soma, subtração, multiplicação e divisão dos numeros.

---

**FIM DA AULA**