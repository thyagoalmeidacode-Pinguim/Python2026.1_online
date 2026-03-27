print(('_' * 30 ) + '\n')
print('--Jogo da adivinhação--')
print(('_' * 30) + '\n')
print('Descubra o valor secreto')
print(('_' * 30) + '\n')
 
import random
nivel = 0
n_certo = random.randint(10,101)
nivel = int(input('Digite o nivel desejado: \n (1= facil, 2= normal e 3= dificil): '))
base = 100
 
while nivel == 1:
    try:
        for i in range(20):
 
           
            num = int(input('Digite um numero entre 10 e 100: ' ))
            print(f"-Você digitou: ({num})-")
            print(('_' * 30) + '\n')
       
            if num < 10 or num > 100:
                print(f"[ERRO] Tente um número entre 10 e 100. Digitado:({num})")
            elif num == n_certo:
                print('\n')
                print(('- Acertou Miseravi -') + '\n')
                print(('_' * 30) + '\n')
                base += 5
                break
            elif num < n_certo:
                print('\n')
                print((f'- Quase lá, este valor é menor que o desejado!-') + '\n')
                print(('_' * 30) + '\n')
                base -= 2
            else:
                print('\n')
                print((f'- Quase lá, este valor é maior que o desejado!') + '\n')
                print(('_' * 30) + '\n')
                base -= 2
        break
    except ValueError:
     print('\n')
     print ('Valor Invalido')
     print(('_' * 30) + '\n')
 
while nivel == 2:
    try:
        for i in range(10):
 
           
            num = int(input('Digite um numero entre 10 e 100: ' ))
            print(f"-Você digitou: ({num})-")
            print(('_' * 30) + '\n')
       
            if num < 10 or num > 100:
                print(f"[ERRO] Tente um número entre 10 e 100. Digitado:({num})")
            elif num == n_certo:
                print('\n')
                print(('- Acertou Miseravi -') + '\n')
                print(('_' * 30) + '\n')
                base += 10
                break
            elif num < n_certo:
                print('\n')
                print((f'- Quase lá, este valor ainda é menor que o desejado!') + '\n')
                print(('_' * 30) + '\n')
                base -= 5
            else:
                print('\n')
                print((f'- Quase lá, este valor é maior que o desejado!') + '\n')
                print(('_' * 30) + '\n')
                base -= 5
        break
    except ValueError:
     print('\n')
     print ('Valor Invalido')
     print(('_' * 30) + '\n')
 
while nivel == 3:
    try:
        for i in range(5):
 
           
            num = int(input('Digite um numero entre 10 e 100: ' ))
            print(f"-Você digitou: ({num})-")
            print(('_' * 30) + '\n')
       
            if num < 10 or num > 100:
                print(f"[ERRO] Tente um número entre 10 e 100. Digitado:({num})")
            elif num == n_certo:
                print('\n')
                print(('- Acertou Miseravi -') + '\n')
                print(('_' * 30) + '\n')
                base += 15
                break
            elif num < n_certo:
                print('\n')
                print((f'- Quase lá, este valor ainda é menor que o desejado!') + '\n')
                print(('_' * 30) + '\n')
                base -= 8
            else:
                print('\n')
                print((f'- Quase lá, este valor é maior que o desejado!') + '\n')
                print(('_' * 30) + '\n')
                base -= 8
        break
    except ValueError:
     print('\n')
     print ('Valor Invalido')
     print(('_' * 30) + '\n')    
 
print(f'Sua pontuação final foi de: {base} o numero certo era {n_certo}')