# Marco 1 — Modelagem do problema

## Objetivo do marco

Neste primeiro acompanhamento, a equipe apresentou a interpretação inicial do problema **Labyrinth (CSES 1193)** e realizou sua modelagem utilizando conceitos de grafos.

O objetivo principal foi deixar de enxergar o problema apenas como uma matriz e identificar formalmente quais elementos do labirinto poderiam ser representados como **vértices** e **arestas**.

---

## Problema analisado

O problema recebe uma matriz de `n` linhas e `m` colunas contendo:

- `.` — célula livre;
- `#` — parede;
- `A` — posição inicial;
- `B` — posição de destino.

A movimentação é permitida apenas em quatro direções:

- esquerda (`L`);
- direita (`R`);
- cima (`U`);
- baixo (`D`).

O objetivo é determinar se existe um caminho entre `A` e `B` e, caso exista, encontrar um caminho de menor comprimento.

Exemplo utilizado durante os acompanhamentos:

```text
########
#.A#...#
#.##.#B#
#......#
########
```

---

## Modelagem como grafo

O labirinto foi modelado como um grafo:

\[
G = (V,E)
\]

onde:

- `V` representa o conjunto de vértices;
- `E` representa o conjunto de arestas.

### Vértices

Cada célula percorrível da matriz é representada por um vértice.

Assim:

- `.` corresponde a um vértice comum;
- `A` corresponde ao vértice de origem;
- `B` corresponde ao vértice de destino;
- `#` não pertence ao conjunto de vértices, pois representa uma posição que não pode ser ocupada.

Cada vértice pode ser identificado inicialmente por sua posição `(i,j)` na matriz.

No exemplo:

```text
A = (2,3)
B = (3,7)
```

---

## Arestas

Existe uma aresta entre duas células quando:

1. ambas são percorríveis;
2. estão imediatamente lado a lado na horizontal ou vertical.

Para um vértice localizado em `(i,j)`, as quatro posições potencialmente adjacentes são:

\[
(i-1,j),\quad(i+1,j),\quad(i,j-1),\quad(i,j+1)
\]

Não são permitidos movimentos diagonais.

Duas posições `(i,j)` e `(x,y)` podem ser consideradas vizinhas quando:

\[
|i-x| + |j-y| = 1
\]

desde que nenhuma delas seja uma parede.

---

## Classificação do grafo

Durante a análise, a equipe identificou as seguintes características.

### Grafo não direcionado

O movimento entre duas células livres pode ser realizado nos dois sentidos.

Se podemos sair de `u` e chegar em `v`, também podemos sair de `v` e voltar para `u`.

### Grafo não ponderado

Todos os movimentos possuem o mesmo custo: **um movimento**.

Dessa forma, todas as arestas podem ser consideradas equivalentes em custo.

### Grau máximo igual a 4

Cada célula pode possuir no máximo quatro vizinhos:

```text
        cima
          |
esquerda-v-direita
          |
        baixo
```

Logo:

\[
grau(v) \leq 4
\]

### Grafo esparso

Mesmo que o labirinto tenha muitos vértices, cada vértice possui no máximo quatro conexões.

Portanto, o número de arestas é pequeno em relação ao número máximo de conexões possíveis de um grafo completo.

### Grafo não necessariamente conexo

As paredes podem separar as células livres em diferentes componentes.

Assim, pode existir um labirinto em que `A` e `B` pertencem a componentes diferentes e não exista caminho entre eles.

---

## Reformulação do problema

Depois da modelagem, o problema pôde ser descrito de forma puramente relacionada a grafos:

> Dado um grafo não direcionado e não ponderado, determinar se existe um caminho entre um vértice de origem `A` e um vértice de destino `B` e, caso exista, encontrar um caminho com a menor quantidade de arestas.

A correspondência adotada foi:

```text
LABIRINTO                    GRAFO

célula livre      ->         vértice
movimento válido  ->         aresta
A                 ->         origem
B                 ->         destino
#                 ->         não pertence ao grafo
```

---

## Conclusão do marco

O principal resultado do Marco 1 foi mostrar que a matriz é apenas a forma de entrada do problema.

A estrutura matemática que representa as possibilidades de movimentação é um **grafo não direcionado, não ponderado e esparso**.

Essa modelagem criou a base necessária para, no marco seguinte, estudar uma forma adequada de representar computacionalmente os vértices e suas conexões.
