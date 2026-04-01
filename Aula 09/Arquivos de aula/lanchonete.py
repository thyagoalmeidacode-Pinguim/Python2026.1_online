print("=== Lanchonete do Python === ")

#Declarando as variáveis
total = 0 #Caixinha para guardar o total da compra
qtd_itens = 0 #Caixinha que guarda a quantidade de itens
qtd_hamburguer = 0 
qtd_refrigerante = 0
qtd_batata = 0

#Aqui começa a magica
try:
    while True:
        print("\nCardápio: ")
        print("Hamburguer - R$ 15")
        print("Refrigerante - R$ 7")
        print("Batata Frita - R$ 10")

        pedido =  input("Faça seu pedido ou escreva finalizar para encerrar: ").lower()

        #Encerramento
        if pedido in ["fim", "finalizar", "f"]:
            break

        #verificar os pedidos
        if pedido == "hamburguer":
            #Solicito a quantidade
            qtd = int(input("Quantidade: "))
            #Multiplico o preço pela quantidade
            total += 15 * qtd
            #Guarda a quantidade
            qtd_itens += qtd
            qtd_hamburguer += qtd
           

        elif pedido == "refrigerante":
            qtd = int(input("Quabtidade: "))
            total += 7 * qtd
            qtd_itens += qtd
            qtd_refrigerante += qtd
            

        elif pedido == "batata frita":
            qtd = int(input("Quantidade: "))
            total += 10 * qtd
            qtd_itens += qtd
            qtd_batata += qtd
            

        else:
            print("Produto invalido!")

        print("Item Adcionado")

    #Calculo do desconto
    if total >= 20:

        #Calcula o desconto
        desconto = total * 0.10

        #Subtrai o deconto do valor total
        total -= desconto

    if qtd_hamburguer > 0:
        print(f'Quantidade de Hmburguer {qtd_hamburguer}')
    
    if qtd_refrigerante > 0:
        print(f'Quabtidade de Refrigerenate {qtd_refrigerante}')
    
    if qtd_batata > 0:
        print(f'Quabtidade de Batata Frita {qtd_batata}')

    print(f"Total de itens {qtd_itens}")
    print(f"Valor da comanda R$ {total:.2f}")   


except ValueError:
    print("Opção Invalida.")