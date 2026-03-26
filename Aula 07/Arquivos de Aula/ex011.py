#Crie um programa que mostre todos os números pares entre dois números informados pelo usuário.
#controle = True

while True:

    try:

        numero_um = int(input("Informe o primeiro valor: "))
        numero_dois = int(input("Informe o segundo valor: "))


        if numero_um > numero_dois:
            numero_tres = numero_um #Guarda o valor de UM 
            numero_um = numero_dois #Troca o valor de um para o do dois
            numero_dois = numero_tres  #Troca o valor de dois para tres
            
            print(numero_um, numero_dois)

        for i in range(numero_um, numero_dois + 1):
            if i % 2 == 0:
                print(i)
        
        #Executou sem erro Encerra o loop
        break

    except ValueError:
        print("Valor inválido! ")
        