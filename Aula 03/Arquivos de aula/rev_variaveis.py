#Crie variáveis para armazenar seu nome, idade e cidade. Depois, exiba essas informações usando print().

# 1 - Passo: Criar as variáveis
# O sinal de igual (=) significa atribuição
nome = "Thyago Assis"
idade = 44
cidade = "Niteroi"
altura = 1.70

int() #Converte para inteiro
float() #Converte para numero fracionario

#A função print (imprimir) exibe na tela

#A primeira forma de formatar a saida
print("O nome é: ",  nome) #Ao juntar a frase e a variavel concatenando
print("A idade é: " + str(idade))

#Segunda forma de formatar a saída
print(f"A cidade é: {cidade}")

#Terceira foram de formatação
print("A altura é: {}".format(altura))