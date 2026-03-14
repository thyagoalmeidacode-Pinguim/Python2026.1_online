"""
Operadores matematicos
     + -> Somar
     - -> Subtrair
     * -> Multiplicar
     / -> Divisão

     // -> O resultado da divisão é exibido como inteiro
     % -> O resto da divisão (sobra)
     ** -> Devolve a exponenciação
"""

""" 
Crie duas variáveis numéricas, a e b.

Some, subtraia, multiplique e divida essas variáveis.
Exiba o resultado de cada operação.
Dica: Use print("Soma:", a + b), etc.

"""
#a = 10
#b = 3

a = int(input("Informe o primeiro valor: "))
b = int(input("Informe o segundo valor: "))

print("Soma e Subtração")
print("Soma: ", a+b)
print("Subtração: ", a-b)

print("")

print("Multiplicação e Divisão")
print("Multimplicação: ", a*b)
print("Divisão: ", a/b)
print("Divisão inteira: ", a//b)

print("")

print("Resto e Potência")
print("Resto da divisão: ", a%b)
print("Potência: ", a**b)