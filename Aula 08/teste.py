while True:
    total = 0
 
    print('-----Seja bem vindo!------')
    print('-Menu Restaurante Simples-')
    print('_' * 30 + '\n' )
    print('Nosso cardapio: \n Cardápio: \n Hamburguer - R$10 \n Refrigerante - R$5 \n Batata Frita - R$7')
    try:
        pedido = input("Digite o item desejado: ").lower()
        print('_' * 30 + '\n' )
 
        if pedido == 'hamburger':
            total += 10
        if pedido == 'refrigerante':
            total += 5
        if pedido == 'batata' or 'batata frita' or 'batatafrita':
            total += 7 
 
 
    except ValueError:
        print('\n')
        print ('Valor Invalido')
        print(('_' * 30) + '\n')
 
    print('Obrigado por nos escolher, volte sempre!')
    print('_' * 30 + '\n' )
   
    input('Finalizar','finalizar','fim')