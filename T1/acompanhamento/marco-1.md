# Marco 1 — Modelagem

**Problema:** B — CSES 1193, *Labyrinth*
**Link oficial:** https://cses.fi/problemset/task/1193
**Categoria no CSES:** Graph Algorithms

## 1. Enunciado (resumo próprio)

Dada uma grade de `n` linhas por `m` colunas representando um labirinto, determinar se existe um
caminho entre uma posição de início `A` e uma posição de destino `B`, andando apenas nas quatro
direções cardeais (cima, baixo, esquerda, direita) e sem atravessar paredes. Se existir caminho, é
preciso reportar o comprimento do caminho **mais curto** e a própria rota, como sequência de
movimentos.

Não é permitido andar na diagonal, nem sair dos limites da grade, nem passar por cima de uma parede.

## 2. Entrada

```
n m
<n linhas, cada uma com m caracteres>
```

- `1 ≤ n, m ≤ 1000`
- Cada célula é um dos quatro caracteres:
  - `.` — chão (livre)
  - `#` — parede (bloqueada)
  - `A` — posição inicial (ocorre **exatamente uma vez** na entrada)
  - `B` — posição de destino (ocorre **exatamente uma vez** na entrada)

## 3. Saída

- `NO`, se não existir caminho de `A` até `B`; ou
- três linhas:
  1. `YES`
  2. o comprimento do caminho mais curto (número de movimentos)
  3. a rota, como uma string de caracteres `L`, `R`, `U`, `D` (esquerda, direita, cima, baixo)

## 4. Restrições

| Restrição            | Valor                                   |
|-----------------------|------------------------------------------|
| Dimensões da grade    | `1 ≤ n, m ≤ 1000` (até 10⁶ células)      |
| Limite de tempo       | 1 segundo                                |
| Limite de memória     | 512 MB                                   |
| Ocorrências de `A`/`B`| exatamente uma de cada, garantido pelo enunciado |

A restrição de tempo é o motivo pelo qual a solução precisa ser **linear no número de células**
(ver justificativa completa no Marco 4, seção de complexidade).

## 5. Modelagem como grafo

O labirinto não vem pronto como grafo — ele precisa ser **enxergado** como um. A regra de
modelagem escolhida é a padrão para problemas de grade:

- **Vértices `V`:** toda célula que não é parede vira um nó.

  `V = { (i, j) : grade[i][j] ≠ '#' , 0 ≤ i < n, 0 ≤ j < m }`

- **Arestas `E`:** duas células viram uma aresta quando são vizinhas ortogonais (distância de
  Manhattan igual a 1) e nenhuma das duas é parede.

  `E = { {(i,j), (i',j')} ∈ V×V : |i−i'| + |j−j'| = 1 }`

- **Tipo do grafo:**
  - **implícito** — nunca é montada uma lista de adjacência explícita "de uma vez"; os vizinhos de
    cada célula são calculados sob demanda (as até 4 direções), durante a própria busca;
  - **não-direcionado** — se `(i,j)` alcança `(i',j')`, o inverso também vale (andar para a direita
    e depois voltar para a esquerda é sempre possível);
  - **não-ponderado** — toda aresta representa um único passo, sem custo diferenciado;
  - **simples** — sem laços (uma célula não é vizinha dela mesma) e sem arestas paralelas;
  - grau máximo de cada vértice é 4 (cima, baixo, esquerda, direita), o que o caracteriza como um
    **grafo de grade (grid graph)**, um caso particular de grafo planar.

O problema "existe caminho de A até B, e qual o mais curto" é, portanto, exatamente o problema
clássico de **caminho mínimo em grafo não-ponderado** entre dois vértices dados.

## 6. Instância pequena

Reaproveitamos a própria instância de exemplo do enunciado oficial do CSES — pequena (5×8 = 40
células) e suficiente para fazer à mão todos os traços pedidos nos próximos marcos.

```
5 8
########
#.A#...#
#.##.#B#
#......#
########
```

- `A` está na linha 2, coluna 3 (1-indexado) — célula `(1,2)` em índices 0-based.
- `B` está na linha 3, coluna 7 (1-indexado) — célula `(2,6)` em índices 0-based.

### Resultado esperado

```
YES
9
LDDRRRRRU
```

Ou seja: existe caminho, o mais curto tem 9 passos, e a rota é
esquerda, baixo, baixo, direita ×5, cima.

## 7. Hipótese inicial de solução

Como a grade vira um grafo não-ponderado, qualquer algoritmo de busca (DFS ou BFS) é capaz de
responder "existe caminho?" percorrendo o grafo a partir de `A` e verificando se `B` é alcançado.

A hipótese de trabalho, a ser testada nos Marcos 3 e 4, é que **apenas a busca em largura (BFS)
garante o caminho *mais curto***, por explorar o grafo em camadas de distância crescente a partir da
origem — a primeira vez que ela alcança um vértice, é necessariamente pela menor quantidade de
arestas possível. A busca em profundidade (DFS), por explorar em um único ramo até o fim antes de
voltar, resolve a existência de caminho, mas não garante minimalidade. Essa comparação empírica
será feita nos Marcos 3 e 4, executando os dois algoritmos manualmente sobre a mesma instância
pequena acima.
