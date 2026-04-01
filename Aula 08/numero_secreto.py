total = 0
quantidade1 = 0
quantidade2 = 0
quantidade3 = 0
quantidade4 = 0
quantidade5 = 0
 
print("Bem Vindo a SalgadosDoRio")
print(25*"-")
print("        Cardápio")
print(25*"-")
 
try:
 
    while True:
   
        escolha = int(input(" 1 = [Coxinha] - R$5 \n 2 = [Risole de Camarão] - R$7 \n 3 = [Empada de Frango] - R$7 \n 4 = [Kibe] - R$6 \n 5 = [Joelho] - R$6 \n 0 = [Encerrar pedido] \n Escolha o seu salgado: "))
 
        if escolha == 1:
            quantidade1 +=1
            total += 5
            print(f"total: R${total}")
            print("Pedido anotado!")
        elif escolha == 2:
            quantidade2 +=1
            total += 7
            print(f"total: R${total}")
            print("Pedido anotado!")
        elif escolha == 3:
            quantidade3 +=1
            total += 7
            print(f"total: R${total}")
            print("Pedido anotado!")
        elif escolha == 4:
            quantidade4 +=1
            total += 6
            print(f"total: R${total}")
            print("Pedido anotado!")
        elif escolha == 5:
            quantidade5 +=1
            total += 6
            print(f"total: R${total}")
            print("Pedido anotado!")
        elif escolha == 0:
            break
        else:
            print("Não possuímos este salgado no nosso cardápio")
 
 
    if quantidade1 > 0 or quantidade2 > 0 or quantidade3 > 0 or quantidade4 > 0 or  quantidade5 > 0:
        print(f"Pedido \n 1 = {quantidade1} \n 2 = {quantidade2} \n 3 = {quantidade3} \n 4 = {quantidade4} \n 5 = {quantidade5}")


    print("Conta R$ ",total)
 
except ValueError:
        print("Valor Inválido")  