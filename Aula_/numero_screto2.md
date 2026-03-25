# 🎮 Sistema de Níveis e Pontuação

## 1. Níveis de Dificuldade

O jogador escolhe um nível antes de começar. Cada nível define quantas **tentativas** (fichas) ele terá para acertar o número.

| Nível | Nome     | Tentativas |
|-------|----------|------------|
| 1     | Fácil    | 20         |
| 2     | Médio    | 10         |
| 3     | Difícil  | 5          |

---

## 2. Sistema de Pontuação

O jogo utiliza um sistema de pontos que incentiva a precisão:  
- **Acerto** → ganha pontos  
- **Erro** → perde pontos  

### 🔢 Pontuação inicial
O jogador começa com uma base de **100 pontos** (valor ajustável).

### ⚖️ Regras por nível
Os valores de perda podem variar conforme a dificuldade, deixando os níveis mais difíceis mais recompensadores, mas também mais punitivos.

| Nível | Ganho por Acerto | Perda por Erro |
|-------|------------------|----------------|
| Fácil | +5               | -2             |
| Médio | +10              | -5             |
| Difícil| +15             | -8             |

### 🧩 Exemplo de fluxo

1. Jogador escolhe **Nível Médio** → 10 tentativas, começa com 100 pontos.
2. **Acertou na 3ª tentativa** → ganha +10 pontos.  
   - Pontuação final: 100 + 10 = 110.
3. Se tivesse errado na 3ª tentativa: 100 - 5 = 95 pontos, e continuaria com as tentativas restantes.

---

## 3. Condições de Término

O jogo encerra quando um dos dois eventos ocorrer:

- **Acerto** → o jogador vence e sua pontuação final é exibida.
- **Esgotamento das tentativas** → o jogador perde e a pontuação final (mesmo que negativa) é mostrada.

---

## 4. Resumo da Experiência

- Escolha do nível determina o número de tentativas.
- Pontuação dinâmica: acertos aumentam a pontuação; erros diminuem.
- Níveis mais altos oferecem maior desafio, mas também maior recompensa por acerto.
- Ideal para criar competição e incentivar o jogador a melhorar seu desempenho.