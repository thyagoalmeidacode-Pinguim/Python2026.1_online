# 🧾 Estudo de Caso: Jogo de Adivinhação de Pratos

## 🎯 Contexto

Uma escola de culinária deseja criar um **jogo interativo** para seus alunos praticarem nomes de pratos famosos de forma divertida.

A ideia é desenvolver um programa em Python onde o computador escolhe, de forma aleatória, um prato de um cardápio pré-definido, e o jogador deve tentar adivinhar qual foi o prato escolhido.

---

## 🧩 Desafio

Você foi contratado para desenvolver esse jogo utilizando Python.

O sistema deve:

- Ter uma lista (vetor) com nomes de pratos.
- Escolher aleatoriamente um prato da lista.
- Permitir que o usuário tente adivinhar o prato escolhido.
- Informar se o usuário acertou ou errou.
- Controlar o número de tentativas disponíveis.

---

## 📋 Requisitos do Sistema

1. Crie uma lista com pelo menos 5 pratos diferentes.
2. O programa deve selecionar aleatoriamente um prato da lista.
3. O usuário terá um número limitado de tentativas (ex: 5).
4. A cada tentativa:
   - O usuário deve digitar o nome de um prato.
   - O programa deve informar se ele acertou ou errou.
5. Caso o usuário acerte:
   - Exibir uma mensagem de sucesso.
   - Encerrar o jogo.
6. Caso o usuário erre:
   - Diminuir o número de tentativas.
   - Informar quantas tentativas ainda restam.
7. Caso as tentativas acabem:
   - Exibir uma mensagem de fim de jogo.
   - Mostrar qual era o prato correto.

---

## 💡 Regras Importantes

- O programa deve ignorar diferenças entre letras maiúsculas e minúsculas.
- Utilize estruturas de repetição (`while`) para controlar o jogo.
- Utilize estruturas condicionais (`if/else`) para verificar as respostas.
- Utilize a biblioteca `random` para fazer a escolha aleatória.

---


## 🎓 Objetivo de Aprendizagem

Ao final desta atividade, você será capaz de:

- Trabalhar com **listas (vetores)** em Python  
- Utilizar **laços de repetição (`while`)**  
- Aplicar **condicionais (`if/else`)**  
- Usar a biblioteca **`random`**  
- Criar um programa interativo com o usuário  