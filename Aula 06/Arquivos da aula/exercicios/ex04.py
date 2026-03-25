# Mostre apenas os números pares de 0 a 20

for i in range(2, 21, 2):
    print(i)

print('Numeros pares de 1 a 20:')  
 
for num in range(1,21):
    if num % 2 == 0:
        print('Numero par:' + str(num))
print('_' * 40)