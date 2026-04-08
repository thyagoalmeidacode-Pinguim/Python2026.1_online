# MATRIZ 2X2
matriz = [
    [7, 10],
    [8, 2],
]
 
total = 0
#ler cada item da lista
for linha in matriz:
    for itens in linha:
        total += itens

print(f"total: {total}")