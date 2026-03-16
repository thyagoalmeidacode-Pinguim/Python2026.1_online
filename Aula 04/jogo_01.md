# Exercício: O Jogo da Adivinhação

## Objetivo
Desenvolver um programa em Python que simule um jogo de adivinhação simples, onde o usuário deve tentar descobrir um número pré-definido pelo sistema.

---

## Descrição da Atividade
Escreva um script que realize as seguintes etapas:

1.  **Interface Visual:** Exiba um cabeçalho estilizado para o jogo utilizando linhas de traços (`-`) e o título "Descubra o valor Secreto".
2.  **Armazenamento:** Defina uma variável chamada `numero_secreto` e atribua a ela um valor inteiro de sua escolha (ex: 10).
3.  **Entrada de Dados:** Solicite que o usuário digite um palpite. Certifique-se de converter o valor recebido (que vem como texto) para um número **inteiro**.
4.  **Lógica de Comparação:** Utilize estruturas condicionais (`if`, `elif`, `else`) para comparar o palpite do usuário com o número secreto:
    * **Se o usuário acertar:** exiba uma mensagem de parabéns.
    * **Se o palpite for menor** que o número secreto: informe que o número secreto é maior.
    * **Se o palpite for maior** que o número secreto: informe que o número secreto é menor.
    * **Tratamento de exceção:** Trate qualquer outra condição inesperada com uma mensagem de "Valor inválido".

---

> **Dica do Professor:** > Lembre-se de que a função `input()` sempre retorna um dado do tipo *string*. Para realizar comparações numéricas, a conversão de tipo (casting) é obrigatória!