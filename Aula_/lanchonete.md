# 🧠 Estudo de Caso: Sistema de Caixa de Lanchonete

## 🎯 Contexto

Uma pequena lanchonete precisa de um sistema simples para registrar pedidos dos clientes.

Atualmente, os pedidos são feitos de cabeça, o que causa erros no valor total.

Você foi contratado para criar um programa em Python que ajude a resolver esse problema.

---

## 🧩 Problema

Crie um programa que permita ao usuário:

1. Escolher produtos de um menu
2. Somar o valor total da compra
3. Continuar adicionando itens até decidir finalizar
4. Mostrar o total final ao encerrar

---

## 🍔 Cardápio

O programa deve exibir:

* Hambúrguer → R$ 10
* Refrigerante → R$ 5
* Batata Frita → R$ 7

---

## ⚙️ Regras do Sistema

* O usuário deve digitar o nome do produto
* Se o produto existir → adicionar ao total
* Se não existir → mostrar "Produto inválido"
* O sistema deve repetir até o usuário digitar **"finalizar"**
* Ao final, mostrar o valor total da compra

---

## 🧱 O que você deve usar

✔ Variáveis
✔ `if` e `else`
✔ `while`
✔ `input()` e `print()`

---

## 💡 Dicas

* Use uma variável para guardar o total:

```python
total = 0
```

* Use um `while` para continuar o pedido:

```python
while True:
```

* Compare os produtos com `if`:

```python
if produto == "hamburguer":
```

---

## ▶️ Exemplo de funcionamento

```
Cardápio:
Hamburguer - R$10
Refrigerante - R$5
Batata Frita - R$7

Digite um produto (ou 'finalizar'): hamburguer
Item adicionado!

Digite um produto (ou 'finalizar'): batata frita
Item adicionado!

Digite um produto (ou 'finalizar'): chocolate
Produto inválido!

Digite um produto (ou 'finalizar'): finalizar

Total da compra: R$17
```

---

## 🚀 Desafio Extra (Opcional)

Se quiser melhorar seu sistema:

* Mostrar quantos itens foram comprados
* Permitir escolher quantidade (ex: 2 refrigerantes)
* Aplicar desconto se o total for maior que R$ 20

---

## 🧑‍🏫 Objetivo de Aprendizagem

Com essa atividade, você vai aprender a:

* Trabalhar com entrada de dados
* Usar decisões com `if/else`
* Criar repetições com `while`
* Controlar valores com variáveis
