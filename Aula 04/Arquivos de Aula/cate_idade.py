""" 
Categoria por idade
Peça a idade de uma pessoa e classifique:

0 – 12 → Criança
13 – 17 → Adolescente
18 – 59 → Adulto
60+ → Idoso

"""
idade = int(input("Informe a idade: "))

if idade < 0:
    print("Idade invalida!")
elif idade <= 12:
    print("Categoria Criança")
elif idade <= 17: 
    print("Cateroria Adolescente!")
elif idade <= 59:
    print("Categoria Adulto")
elif idade >= 60:
    print("Categoria Idoso!")
else: 
    print("Categoria inexistente")
