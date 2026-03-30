# 🧾 Estudo de Caso: Sistema de Lista de Compras

## 🎯 Contexto

Uma pequena mercearia do bairro quer organizar melhor suas compras semanais. Atualmente, tudo é anotado no papel, o que causa erros, esquecimentos e retrabalho.

Para resolver isso, você foi contratado para desenvolver um programa simples em Python que utilize **vetores (listas)** para controlar os itens da compra.

---

## 🧠 Problema

O sistema deve permitir que o usuário gerencie uma lista de compras, podendo:

* Adicionar itens
* Remover itens
* Visualizar a lista
* Ver a quantidade de itens cadastrados

Tudo isso utilizando **listas (vetores)**.

---

## 🛠️ Requisitos do Sistema

O programa deve exibir um menu com as seguintes opções:

```
1 - Adicionar item  
2 - Remover item  
3 - Listar itens  
4 - Mostrar quantidade de itens  
5 - Sair  
```

---

## 📋 Regras de Negócio

* Os itens devem ser armazenados em uma lista
* O usuário pode adicionar quantos itens quiser
* Ao remover, o programa deve pedir o nome do item
* Caso o item não exista, mostrar uma mensagem de erro
* O programa só deve encerrar quando o usuário escolher a opção 5

---

## 💡 Exemplo de Funcionamento

```
Escolha uma opção: 1
Digite o item: arroz

Escolha uma opção: 1
Digite o item: feijão

Escolha uma opção: 3
Lista: ['arroz', 'feijão']

Escolha uma opção: 4
Quantidade: 2
```

---

## 🚀 Desafio Extra (Opcional)

Implemente funcionalidades adicionais:

* ✅ Evitar itens duplicados
* ✅ Ordenar a lista em ordem alfabética
* ✅ Permitir inserir item em uma posição específica
* ✅ Permitir remover item usando índice (`pop`)

---

## 📝 Entrega

O aluno deverá entregar:

* Código funcionando
* Uso correto de listas (vetores)
* Uso de estruturas como:

  * `if`
  * `while`
  * `for`
