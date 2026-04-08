import numpy


numeros = [
    [1,2,5],
    [3,4,6],
    [7,8,9]
]
 
par = 0
 
for linha in numeros: 
    for elementos in linha: 
        if elementos % 2 == 0:
            par += 1
 
print(f"A quantidade de números pares é: {par}")