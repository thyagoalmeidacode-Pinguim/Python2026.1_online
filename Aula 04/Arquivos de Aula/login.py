""" 
Sistema de login

Crie duas variáveis:
usuario = "admin"
senha = "1234"

Peça ao usuário para digitar usuário e senha e informe se o login foi bem-sucedido ou incorreto.

"""
#Cadastrado no sistema
usuario = "admin"
senha = "1234"

#Login e senha informados no acesso ao sistema
login = input("Informe seu login: ")
passwd = input("informe sua senha: ")

#Primeira Forma
#O operador and precisa que as duas condições sejam verdadeiras

if usuario == login and senha == passwd:
    print("Acesso autorizado!")
else:
    print("Acesso negado, usuario ou senha invalidos!")

#Segunda forma
""" 
if usuario == login:
    print("usuario correto")
    if senha == passwd:
        print("senha correta")
    else:
        print("senha incorreta")
else:
    print("usuario incorreto") """
 

 


