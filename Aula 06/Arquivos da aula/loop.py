# O que são loops ou repetição?
    # São comandos que permitem executar um bloco várias vezes.

#Tipos de estrutura de repetição no Python
    # While -> Repente enquanto uma condição for verdadeira.
    # For -> Repete Um numero determinada vezes.

#Estrutura de Wile
#Exemplo 01
print("Exemplo 01")
volta_carrossel = 0

while volta_carrossel <= 5:
    print("Volta no carrosel nº ", volta_carrossel )

    #Iteirando em 1
    #volta_carrossel = volta_carrossel + 1
    volta_carrossel += 1

#Exemplo 02

print("\nExemplo 02")

senha = ""
while senha != "1234":
    senha = input("Informe a senha: ")

print("Acesso Liberado!")

# Estrutura For
# range(inicio, fim, passo) - passo quanto vale a volta
print("\nEstrutura do For")

#Conta de 0 a 4
print("\nPirneiro exemplo:")
for variavel in range(5):    
    print("O valor é: ", variavel)


#Segundo exemplo
#Conta de 1 a 4
print("\nSegundo exemplo:")
for v in range(1,5):
    print("Valor é: ", v)


#Terceiro exemplo
print("Terceiro exemplo:")
for i in range(0,11,2):
    print("O valor é: ", i)

#Comandos de controle
    # break -> para a execução do loop imediamente
    # continue -> Pula a repetição atual e vai para a proxima

# Exemplo break

print("\n Exemplo do break")
for i in range(10):
    if i == 8:
        break
    print(i)

# Exemplo continue
print("Exemplo continue")

for i in range(5):
    if i == 3:
        continue
    print(i)

