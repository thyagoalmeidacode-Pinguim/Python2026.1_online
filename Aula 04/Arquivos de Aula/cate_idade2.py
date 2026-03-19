""" 
Categoria por idade
Peça a idade de uma pessoa e classifique:

0 – 12 → Criança
13 – 17 → Adolescente
18 – 59 → Adulto
60+ → Idoso

"""


idade = int(input("Informe sua Idade: "))

match idade:
    case i if i < 0:
        print("Idade inválida")
    case i if i <= 12: 
        print("Categoria Criança")
    case i if i <= 17: 
        print("Categoria Adolescente")
    case i if i <= 59: 
        print("Categoria Adulto")
    case i if i > 60: 
        print("Categoria Idoso")    
    case _:
        print("Sem categoria")