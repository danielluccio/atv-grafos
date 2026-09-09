# Marco 2 — Representação do grafo

## Objetivo do marco

No segundo acompanhamento, a equipe partiu da modelagem definida no Marco 1 e discutiu como o grafo poderia ser representado computacionalmente.

Os principais pontos abordados foram:

- representação dos vértices;
- relação entre posições `(i,j)` e identificadores;
- lista de adjacência;
- comparação com matriz de adjacência;
- grafo implícito;
- adequação da representação ao problema.

---

## Matriz original

O problema fornece os dados na forma de uma matriz.

Exemplo:

```text
########
#.A#...#
#.##.#B#
#......#
########
```

Cada célula percorrível pode inicialmente ser identificada por sua coordenada `(i,j)`.

Por exemplo:

```text
A = (2,3)
B = (3,7)
```

---

## Abstração dos vértices

Para facilitar a manipulação do grafo e também sua visualização durante a apresentação, as posições `(i,j)` podem ser abstraídas para identificadores numéricos.

No exemplo utilizado pela equipe:

| Vértice | Posição |
|---:|---|
| 1 | `(2,2)` |
| 2 | `A = (2,3)` |
| 3 | `(2,5)` |
| 4 | `(2,6)` |
| 5 | `(2,7)` |
| 6 | `(3,2)` |
| 7 | `(3,5)` |
| 8 | `B = (3,7)` |
| 9 | `(4,2)` |
| 10 | `(4,3)` |
| 11 | `(4,4)` |
| 12 | `(4,5)` |
| 13 | `(4,6)` |
| 14 | `(4,7)` |

Assim:

```text
A -> vértice 2
B -> vértice 8
```

Essa numeração foi utilizada como uma abstração para facilitar a execução manual dos algoritmos.

---

## Lista de adjacência

A representação estudada foi a **lista de adjacência**.

Nela, cada vértice armazena apenas os vértices diretamente conectados a ele.

Para o exemplo, a lista de adjacência é:

```text
1  -> [2, 6]
2  -> [1]

3  -> [4, 7]
4  -> [3, 5]
5  -> [4, 8]

6  -> [1, 9]
7  -> [3, 12]
8  -> [5, 14]

9  -> [6, 10]
10 -> [9, 11]
11 -> [10, 12]
12 -> [7, 11, 13]
13 -> [12, 14]
14 -> [13, 8]
```

Por exemplo:

```text
1 -> [2, 6]
```

significa que o vértice `1`, correspondente à posição `(2,2)`, possui uma aresta com:

- o vértice `2`, correspondente a `A`;
- o vértice `6`, correspondente à posição `(3,2)`.

---

## Por que utilizar lista de adjacência?

Uma alternativa seria utilizar uma matriz de adjacência de dimensão:

\[
V \times V
\]

Entretanto, essa representação exige:

\[
O(V^2)
\]

de memória.

No Labyrinth, cada vértice possui no máximo quatro vizinhos.

Portanto, a maior parte das posições de uma matriz de adjacência seria utilizada apenas para indicar ausência de conexão.

A lista de adjacência armazena somente as arestas existentes e utiliza:

\[
O(V+E)
\]

de memória.

Como o grafo é esparso, essa representação é mais adequada.

---

## Grafo implícito

Outro ponto discutido foi que o labirinto pode ser entendido como um **grafo implícito**.

A entrada não fornece diretamente algo como:

```text
1 2
1 6
3 4
...
```

As arestas são descobertas a partir da própria matriz.

Para uma célula `(i,j)`, basta analisar:

```text
(i-1,j)
(i+1,j)
(i,j-1)
(i,j+1)
```

e verificar se cada posição:

1. está dentro da matriz;
2. não contém `#`.

Assim, a matriz contém informações suficientes para derivar todo o grafo.

---

## Relação entre matriz e representação

Foi importante separar duas ideias:

```text
MATRIZ
  |
  | fornece posições e obstáculos
  v
MODELAGEM
  |
  | transforma células em vértices
  v
REPRESENTAÇÃO
  |
  | armazena conexões
  v
LISTA DE ADJACÊNCIA
```

A matriz continua sendo necessária para entender o ambiente original, enquanto a lista de adjacência permite visualizar e percorrer o grafo como uma estrutura de vértices e arestas.

---

## Construção das conexões

Para cada célula livre, podem ser verificadas as células adjacentes.

Quando uma célula livre é vizinha de outra célula livre, existe uma aresta entre seus respectivos vértices.

Como o grafo é não direcionado:

```text
u --- v
```

representa simultaneamente a possibilidade de:

```text
u -> v
v -> u
```

---

## Conclusão do marco

O Marco 2 permitiu definir uma representação adequada ao tipo de grafo produzido pelo labirinto.

A lista de adjacência foi considerada apropriada principalmente porque:

- o grafo é esparso;
- cada vértice possui grau máximo quatro;
- apenas as conexões existentes precisam ser armazenadas;
- os algoritmos de busca conseguem percorrer diretamente os vizinhos de cada vértice.

Essa etapa deixou o problema pronto para o estudo de algoritmos de busca.
