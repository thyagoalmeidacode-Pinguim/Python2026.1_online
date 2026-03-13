""" Solicite ao usuário nome, idade e altura e exiba usando as quatro formas de print.

Converta idade para int e altura para float """

nome = input("Informe seu nome: ")
idade = input("Informe sua Idade: ")
altura = input("Informe sua altura: ")

""" Primeira forma """
print("O nome é: ", nome)

""" Segunda forma """
print(f"A idade é: {int(idade)} ")

""" Terceira forma """
print("A altura é: {}".format(float(altura)))