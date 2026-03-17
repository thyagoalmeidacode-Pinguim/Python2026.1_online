#Captura os valores informados pelo usuario
valor_um = float(input("Informe o primeiro valor: "))
valor_dois = float(input("Informe o segundo valor: "))

#Pede para o usuario escolher a operacao
print(30*("-"))
print("Agora escolha uma operação: ")
operacao = input("Opções: [soma], [subtracao], [multiplicacao], [divisao]: ").lower()
print(operacao)

#if operacao == "soma":
if operacao in ["soma", "+", "s", "somar"]:
    #Guarda o resultado da operção de soma dos valores
    resultado = valor_um + valor_dois
    print(f"A soma é {resultado}")

elif operacao == "subtracao":
    resultado = valor_um - valor_dois
    print(f"A subtração {resultado}")

elif operacao == "multiplicacao":
    resultado = valor_um * valor_dois
    print(f"A Multiplicação {resultado}")

elif operacao == "divisao":
    if valor_dois == 0:
        print("Não é possivel divisao por zero!")
    else:
        resultado = valor_um / valor_dois
        print(f"A Diveisão é {resultado}")

else:
    print("Operação desconhecida!")





else:
    print("Operção invalida!")

