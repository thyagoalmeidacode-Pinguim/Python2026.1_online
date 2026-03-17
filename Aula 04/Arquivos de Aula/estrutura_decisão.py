""" 
Estrutura de decisão?
    - Ajuda na tomada
    - Lista as opções disponiveis
    - Comandos que ajudam na decisão

    - Conceito: Estrutura de decisão permitem que o computador possa tomar uma decisão com base em uma condição

    Classificações: 
        Simples -- Somente um resposta
        Composta -- Duas repostas possíveis
        Encadeada -- Possui várias respostas
        Match Case -- Escolhe uma opção entre várias

"""
#Decisão Simples:
print("Decisão Simples")

idade = 10
if (idade >= 18):
    print("Maior de idade")

#Decisão composta
fruta = "Banana"

if fruta == "Banana":
    print("Você escolheu a fruta correta!", fruta)
else:
    print("Você escolheu a fruta errada! ")

#Decisão encadeada
liguagem_preferida = "java"

if liguagem_preferida == "python":
    print("Liguagem versátil")
elif liguagem_preferida == "php":
    print("Muito usada em aplicações web")
elif liguagem_preferida == "java":
    print("Linguagem robusta")
else:
    print("Não conheço esta linguagem")

#Match Case (Funciona a partir da versão 3.10 do pyhton)
print("match case")

time = "Plameiras"
match time:
    case "Flamengo":
        print("O maior do Rio")
    case "Botafogo":
        print("Kd os torcedores")
    case "Fluminense":
        print("Time de guerreiros")
    case "Vasco":
        print("Gigante da colina(Maior do Brasil)")
    case _:
        print("Time não conhecido")
