#Simule uma votação com 5 pessoas. Pergunte o voto (1, 2 ou 3) e mostre ao final qual opção teve mais votos.

#Criar as variaveis
candidato_um = 0
candidato_dois = 0
candidato_tres = 0

#Solicita os votos e contabiliza
#for i in range(5):
#    voto = int(input("Digite seu voto: [1],[2],[3]: "))
#    if voto == 1:
#        candidato_um += 1
#    elif voto == 2:
#        candidato_dois += 1
#    elif voto == 3:
#        candidato_tres += 1
#    else:
#        print("Candidadto invalido! ")

while controle < 5:
    voto = int(input("Informe seu voto: [1],[2],[3]: "))
    if voto == 1:
        candidato_um += 1
    elif voto == 2:
        candidato_dois += 1
    elif voto == 3:
        candidato_tres += 1
    else:
        print(" Candidato Inválido: ")
    controle += 1

#Exibe a quantidade de votos de cada candidato
print("Candidato 1: ", candidato_um)
print("Candidato 2: ", candidato_dois)
print("Candidato 3: ", candidato_tres)