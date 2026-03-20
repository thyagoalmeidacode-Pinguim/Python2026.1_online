# 📘 Aula: Estruturas de Repetição em Python

## 🎯 Objetivo
Aprender a repetir ações automaticamente usando **laços de repetição**, evitando escrever o mesmo código várias vezes.

---

## 🔁 O que são estruturas de repetição?

São comandos que permitem executar um bloco de código várias vezes.

Imagine:
- Você quer imprimir "Bom dia" 10 vezes  
- Ou pedir a senha até acertar  
- Ou somar vários números  

👉 Em vez de repetir código manualmente, usamos **loops**

---

## 🧠 Tipos de repetição em Python

Existem dois principais:

- `while` → repete **enquanto uma condição for verdadeira**
- `for` → repete **um número determinado de vezes**

---

# 🔄 1. Estrutura `while`

## 📌 Ideia
Repete **enquanto algo for verdadeiro**

## 🧾 Exemplo simples

```python
contador = 1

while contador <= 5:
    print("Contando:", contador)
    contador = contador + 1