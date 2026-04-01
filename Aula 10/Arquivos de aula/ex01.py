""" 
Crie um lista com 6 números inteiros e mostre:

Todos os elementos
O maior valor
O menor valor

"""

#idades = [23, 43, 18, 35, 12]

#print(idades) #Exibe todos
#print("Maior idade é: ", max(idades)) #Exibe o maior
#print("Menor idade é: ", min(idades)) #Exibe o menor

idade_aluno = [] 
for i in range(4):
    idade = int(input("Informe a idade do aluno: "))
    #append()- adiciona itens a lista
    idade_aluno.append(idade)

print("Idades dos alunos: ", idade_aluno)

print("O aluno mais velho é: ", max(idade_aluno))
print("O aluno mais novo é: ", min(idade_aluno))



