""" 
Você foi contratado como programador iniciante para desenvolver um programa simples de cadastro de alunos.

O sistema deverá:

Solicitar ao usuário as seguintes informações:

    Nome do aluno
    Idade
    Curso em que está matriculado
    Email para contato

Após coletar as informações, o programa deverá salvar esses dados em um arquivo de texto.

Cada cadastro deve ser registrado de forma organizada no arquivo.

Obs: Para esta atividade vocês precisarão pesquisar sobre a função open() para criação do arquivo 
"""
print(30*"-")
print("| Cadastro de Alunos |")
print(30*"-")
print("")

#Declarar as variáveis
nome = input("Informe seu nome: ")
idade = input("Informe a Idade: ")
curso = input("Informe o curso: ")
email = input("Informe um email para contato: ")

# A função open() premite criar um arquivo com python
dados = open("cadastro.txt", "a", encoding="utf-8") # o a é de append, serve para adicionar os dados dentro do arquivo

#Adicoinando dados dentro do arquivo
dados.write("Nome: " + nome + "\n")
dados.write("Idade: " + idade + "\n")
dados.write("Curso: " + curso + "\n")
dados.write("Email: " + email + "\n\n") 
dados.write("-----------------------------------" + "\n")

#Fechar o arquivo
dados.close()
print("Dados do aluno cadastrado com sucesso!")