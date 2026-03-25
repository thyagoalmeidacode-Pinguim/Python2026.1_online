# 🎓 Aula: Vetores e Matrizes em Python

Nesta aula, vamos desmistificar o uso de **Vetores (listas simples)** e **Matrizes (listas de listas)** utilizando analogias do cotidiano e exemplos práticos.

---

## 🧠 1. Vetores (Listas)

### 📌 O que é um vetor?
Um vetor é uma coleção linear de dados. Pense nele como uma **prateleira**, onde cada item ocupa uma posição específica, chamada de **índice**.

> ⚠️ **Regra de Ouro:** Em programação, a contagem de posições sempre começa no **0**.

### 💡 Exemplo do dia a dia: Lista de Compras
- Índice 0: Arroz  
- Índice 1: Feijão  
- Índice 2: Leite  

---

### 🧾 Implementação em Python
```python
# Criando o vetor (lista)
compras = ["arroz", "feijão", "leite"]

# 🔎 Acessando elementos
print(compras[0])  # Saída: arroz
print(compras[1])  # Saída: feijão

# ✏️ Alterando valores
compras[1] = "macarrão"
print(compras)     # Saída: ['arroz', 'macarrão', 'leite']

# ➕ Adicionando elementos (no final da lista)
compras.append("café")

# ❌ Removendo elementos
compras.remove("arroz")
📊 Exemplo Prático: Média de Notas
notas = [7.5, 8.0, 6.5]

# Calculando a média acessando os índices
media = (notas[0] + notas[1] + notas[2]) / 3

print(f"Média do aluno: {media:.2f}")
🧠 2. Matrizes (Listas de Listas)
📌 O que é uma matriz?

Uma matriz é uma tabela de dados. Enquanto o vetor tem apenas uma linha, a matriz possui linhas e colunas.

No Python, representamos isso colocando listas dentro de uma lista principal.

💡 Exemplo do dia a dia: Boletim Escolar
Índice	Coluna 0 (Nome)	Coluna 1 (Nota)
Linha 0	João	7.0
Linha 1	Maria	8.5
🧾 Implementação em Python
# Estrutura: matriz[linha][coluna]
matriz = [
    ["João", 7.0],  # Linha 0
    ["Maria", 8.5]  # Linha 1
]

# 🔎 Acessando dados
print(matriz[0][0])  # Saída: João (Linha 0, Coluna 0)
print(matriz[1][1])  # Saída: 8.5 (Linha 1, Coluna 1)

# ✏️ Alterando valores (Melhorando a nota do João)
matriz[0][1] = 9.0

# ➕ Adicionando nova linha (Novo Aluno)
matriz.append(["Carlos", 6.5])
📊 Exemplo Prático: Controle de Estoque
estoque = [
    ["Arroz", 10],   # Produto, Quantidade
    ["Feijão", 5],
    ["Leite", 8]
]

print(f"Produto: {estoque[0][0]} | Quantidade: {estoque[0][1]}")
🔁 3. Percorrendo os Dados (Loops)

Para processar vários dados de uma vez sem escrever código repetitivo, usamos o for.

🔹 Percorrendo Vetores
nomes = ["Ana", "Bruno", "Carlos"]

for nome in nomes:
    print(f"Nome do aluno: {nome}")
🔹 Percorrendo Matrizes
alunos = [
    ["Ana", 7],
    ["Bruno", 6],
    ["Carlos", 9]
]

for aluno in alunos:
    # aluno[0] pega o nome, aluno[1] pega a nota
    print(f"Aluno: {aluno[0]} - Nota: {aluno[1]}")
🚀 Dica Final

Para não confundir as coordenadas em matrizes, lembre-se sempre da ordem:

Primeiro colchete [x]: Seleciona a Linha (qual lista você quer)
Segundo colchete [y]: Seleciona a Coluna (qual item dentro daquela lista)