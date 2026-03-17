"""
1 - Crie uma variável senha = "python123". Peça ao usuário para digitar a senha e informe se está correta ou incorreta.

""" 
senha = input("Digite sua senha: ")
#if - se alguma coisa acontece
if senha == "python123":
    print("A senha esta correta! ")
 
#Else - senao acontecer o que esta no if - Resposta padrao
else:
    print("A senha esta incorreta!")

""" 
2 - Peça um número ao usuário e informe se ele é par ou ímpar.
"""

#A Regra é clara - todo numero para ser par deve ser divisivel por 2 e ter resto zero.  o Sinal % deovolve para mim o resto de uma divisão
num = int(input("Informe um valor: "))
resto = num % 2
#divisao = num / 2

if resto == 0:
    print("O numero é par")
else: 
    print("O numero é impar")
