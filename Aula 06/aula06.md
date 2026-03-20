# 📘 Tutorial Completo: Estruturas de Repetição em Python

---

## 🎯 Objetivo
Aprender a repetir ações automaticamente usando **laços de repetição (`while` e `for`)**, com exemplos simples do dia a dia e exercícios práticos.

---

# 🔁 O que são estruturas de repetição?

São comandos que permitem executar um bloco de código várias vezes.

### 💡 Exemplos do dia a dia:
- Repetir uma tarefa (lavar pratos várias vezes 🍽️)
- Pedir senha até acertar 🔐
- Somar vários números 🧮

👉 Em vez de repetir código manualmente, usamos **loops**.

---

# 🧠 Tipos de repetição em Python

- `while` → Repete **enquanto uma condição for verdadeira**.
- `for` → Repete **um número determinado de vezes**.

---

# 🔄 1. Estrutura `while`

## 📌 Ideia
Repete enquanto uma condição for verdadeira.

### 🧾 Exemplo simples
```python
contador = 1

while contador <= 5:
    print("Contando:", contador)
    contador = contador + 1
```

#### 🔍 Explicação
1.  **Início**: Começa em 1.
2.  **Condição**: Enquanto for menor ou igual a 5, repete.
3.  **Incremento**: Soma +1 a cada volta para não ficar em loop infinito.

### 🧃 Exemplo do dia a dia: Senha
```python
senha = ""

while senha != "1234":
    senha = input("Digite a senha: ")

print("Acesso liberado!")
```
👉 O programa continua pedindo a senha até que o usuário digite a correta.

⚠️ **Cuidado com loop infinito**: Sempre garanta que a condição do `while` um dia se torne falsa!

---

# 🔁 2. Estrutura `for`

## 📌 Ideia
O `for` é usado quando sabemos quantas vezes queremos repetir ou quando queremos percorrer uma sequência.

### 🧾 Estrutura básica
```python
for variavel in range(inicio, fim, passo):
    # código
```

### 🔍 Exemplo simples
```python
for i in range(5):
    print("Valor:", i)
```
*Saída: 0, 1, 2, 3, 4 (o 5 não entra).*

---

# 🔢 Entendendo o `range()`

| Comando | O que faz |
| :--- | :--- |
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 (Início e fim) |
| `range(0, 11, 2)` | 0, 2, 4, 6, 8, 10 (Pula de 2 em 2) |
| `range(10, 0, -1)` | 10, 9, 8... 1 (Contagem regressiva) |

### 🧃 Exemplo do dia a dia
```python
for i in range(3):
    print("Lavando prato 🍽️")
```

---

# 🔄 Comparação Rápida

| Situação | Usar |
| :--- | :--- |
| Não sei quantas vezes repetir | `while` |
| Sei quantas vezes repetir | `for` |

---

# 🛑 Comandos de Controle

- **`break`**: Para o loop imediatamente.
- **`continue`**: Pula a repetição atual e vai para a próxima.

```python
# Exemplo break
for i in range(10):
    if i == 5:
        break
    print(i)

# Exemplo continue
for i in range(5):
    if i == 2:
        continue
    print(i)
```