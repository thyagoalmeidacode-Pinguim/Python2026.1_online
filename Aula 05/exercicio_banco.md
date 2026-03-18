# Exercício: Simulação de Sistema Bancário Básico

## Objetivo
Criar um programa em Python que simule o funcionamento básico de uma conta bancária, incluindo abertura de conta, depósito inicial, e operações de saque, depósito e consulta de saldo.

## Descrição do Problema
1. Solicite ao usuário o **nome do titular da conta**.  
2. Solicite ao usuário o **valor do depósito inicial** e valide se o valor é um número positivo.  
   - Se o valor informado for válido (maior ou igual a 0), a conta é aberta com este saldo.  
   - Caso contrário, a conta é aberta com saldo **R$ 0,00** e uma mensagem de aviso é exibida.  

3. Pergunte ao titular se ele deseja **realizar alguma operação**.  
   - Caso a resposta seja afirmativa, o programa deve permitir que o usuário escolha entre três operações:  
     - **Sacar**: Solicitar o valor a ser sacado e verificar se há saldo suficiente.  
     - **Depositar**: Solicitar o valor do depósito e validar se é positivo.  
     - **Saldo**: Exibir o saldo disponível.  
   - Caso a resposta seja negativa, o programa deve exibir uma mensagem de encerramento do atendimento.  

4. Ao final de cada operação, exibir mensagens informando o resultado da operação e o saldo atual, se aplicável.  

## Regras e Validações
- O depósito inicial deve ser um número maior ou igual a zero.  
- Para saques, o valor não pode ser maior que o saldo disponível.  
- Para depósitos, o valor deve ser maior que zero.  
- O programa deve aceitar variações de respostas afirmativas para realizar operações, como `"sim"`, `"s"` ou `"si"`.  

## Exemplo de Execução