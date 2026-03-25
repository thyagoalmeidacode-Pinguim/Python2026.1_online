# 📘 Atividade: Controle de Acesso no Sistema Bancário

Recupere o código do sistema bancário desenvolvido em aula anteriormente.

## 🎯 Objetivo
Modificar o programa para que ele **permaneça em execução até que o usuário escolha sair**.

## 📝 O que deve ser feito
Atualmente, o programa executa apenas uma operação e encerra. Sua tarefa é:

- Implementar uma estrutura de repetição (`while`) para manter o sistema rodando.
- Exibir continuamente um menu com as opções:
  - Saque  
  - Depósito  
  - Saldo  
  - Sair  
- O sistema **só deve ser encerrado quando o usuário digitar "sair"**.
- Caso o usuário escolha qualquer outra opção, o programa deve executar a ação e depois **retornar ao menu**.

## ⚠️ Regras
- Utilize boas práticas de organização do código.
- Valide a opção digitada pelo usuário.
- Exiba mensagens claras para cada operação.

## 💡 Dica
Use uma variável de controle (por exemplo: `opcao`) dentro de um `while` para repetir o menu até que o usuário digite `"sair"`.