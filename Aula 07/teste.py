candidato1 = 0
candidato2 = 0
candidato3 = 0
controle = 0 

while controle < 5:

    try: 
        voto = int(input("Informe seu voto: [1],[2],[3]: "))
        if voto == 1:
            candidato1 += 1
        elif voto == 2:
            candidato2 += 1
        elif voto == 3:
            candidato3 += 1
        else:
            print("Candidato Inválido: ")
        controle += 1 
                
    except ValueError:
        print("Digite um valor dos candidatos")
        
print("Candidato 1: ", candidato1)
print("Candidato 2: ", candidato2)
print("Candidato 3: ", candidato3)