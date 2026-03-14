
""" 
Crie uma variável saldo com valor inicial de 1000.

Adicione 250 ao saldo.
Subtraia 150 do saldo.
Exiba o valor final do saldo. 
"""
print(30*"-") 
print("|Bem vindo ao banco Python |")
print(30*"-") 
print("")

saldo = 1000

deposito = float(input("Informe o valor do deposito: R$ "))
saldo = saldo + deposito
print("O valor de depósito foi R$ {}, Saldo atual de R$ {}".format(deposito,saldo))

saque = float(input("Informe o valor do saque R$ "))
saldo = saldo - saque
print("Valor de saque R$ {}, Saldo atual R$ {}".format(saque,saldo))

print("Operaçao realizada com sucesso!")