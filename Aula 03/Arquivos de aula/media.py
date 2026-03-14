nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

media = (nota1+nota2+nota3)/3
resultado = media >= 5

print("Média: ", media)
print("Aprovado?", resultado)

print( ["REPROVADO", "APROVADO"] [int(media > 5)] )