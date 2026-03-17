""" 
Verificar maior de idade
Peça a idade do usuário e informe se é "Maior de idade" ou "Menor de idade".

"""
idade = int(input("Informe sua Idade: "))

if idade >= 18:
    print("Você pode entrar na festa, maior de 18 anos ")
else: 
    print("Você não pode entrar na festa, menor de idade")

