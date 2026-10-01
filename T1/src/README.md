# T1 — Resolução de Problemas com Grafos

Trabalho desenvolvido para a disciplina de **Resolução de Problemas com Grafos**, com o objetivo de modelar, implementar e analisar uma solução baseada em algoritmos de grafos, utilizando a biblioteca algs4.

---

## Integrantes do Grupo A

| Integrante | Matrícula |
|---|---|
| DANIEL LUCIO DE CASTRO | `2310285` |
| JUAN DOTH CAMERINO COSTA COELHO | `2417203` |
| GUILHERME MACHADO FARIA | `21161881` |

---

## Problema

### CSES — Labyrinth

O problema atribuído foi o **Labyrinth**, que neste nosso caso é o problema B,disponível na plataforma CSES.

**Problema:**  
CSES Problem Set — Labyrinth (1193)

**Link:**  
https://cses.fi/problemset/task/1193/

O problema fornece uma matriz representando um labirinto contendo:

- `.` — célula livre;
- `#` — parede;
- `A` — posição inicial;
- `B` — posição de destino.

A movimentação pode ocorrer em quatro direções:

- esquerda (`L`);
- direita (`R`);
- cima (`U`);
- baixo (`D`).

O objetivo é determinar se existe um caminho entre `A` e `B` e, caso exista, encontrar um caminho de menor comprimento.

---

## Linguagem

A implementação será desenvolvida em:

- **Python**

A solução utilizará estruturas e algoritmos baseados na biblioteca **algs4**, conforme especificação da disciplina.

> A definição final das classes, módulos e componentes da biblioteca utilizados será documentada após a validação da implementação.

---

## Estrutura do projeto

```
T1/
├── README.md
├── acompanhamento/
│   ├── marco-1.md
│   ├── marco-2.md
│   ├── marco-3.md
│   └── marco-4.md
├── src/
│   ├── main.py
│   └── módulos necessários
├── evidencias/
│   └── accepted.png | accepted.pdf
├── apresentacao/
│   └── apresentacao.pdf
└── dados/
    └── casos-de-teste.txt



## Execução

### Pré-requisitos

Para executar o projeto é necessário possuir:

- Python 3 instalado;
- `pip` disponível para instalação das dependências.

As dependências utilizadas pelo projeto estão listadas no arquivo:

```
requirements.txt




## Modelagem

O problema **Labyrinth** é originalmente apresentado como uma matriz de `n` linhas e `m` colunas. Para solucioná-lo utilizando algoritmos de grafos, o labirinto é modelado como um grafo:

\[
G = (V, E)
\]

onde:

- `V` representa o conjunto de vértices;
- `E` representa o conjunto de arestas.

### Vértices

Cada célula percorrível do labirinto é representada por um vértice.

Portanto, pertencem ao conjunto `V` todas as posições `(i, j)` da matriz que não representam uma parede (`#`):

\[
V = \{(i,j) \mid matriz[i][j] \neq \#\}
\]

As células especiais:

- `A` representa o vértice de origem;
- `B` representa o vértice de destino.

As paredes (`#`) não fazem parte do grafo, pois não podem ser percorridas.

### Arestas

Existe uma aresta entre dois vértices quando suas respectivas células são vizinhas horizontalmente ou verticalmente e ambas são percorríveis.

Dessa forma, para uma célula `(i,j)`, os possíveis vizinhos são:

\[
(i-1,j),\quad(i+1,j),\quad(i,j-1),\quad(i,j+1)
\]

correspondendo, respectivamente, aos movimentos:

- cima;
- baixo;
- esquerda;
- direita.

Formalmente, duas células percorríveis `(i,j)` e `(x,y)` são adjacentes quando:

\[
|i-x| + |j-y| = 1
\]

### Características do grafo

A partir dessa modelagem, o grafo possui as seguintes características:

- **não direcionado:** todo movimento válido pode ser realizado nos dois sentidos;
- **não ponderado:** todos os movimentos possuem o mesmo custo;
- **grau máximo 4:** cada vértice pode possuir no máximo quatro vizinhos;
- **esparso:** cada vértice possui apenas uma pequena quantidade de arestas em relação ao número total de vértices;
- **não necessariamente conexo:** paredes podem separar o labirinto em diferentes componentes.

### Objetivo no grafo

Seja:

- `s` o vértice correspondente à posição inicial `A`;
- `t` o vértice correspondente à posição de destino `B`.

O problema passa a ser:

> determinar se existe um caminho entre `s` e `t` e, caso exista, encontrar um caminho com a menor quantidade possível de arestas.

Como cada aresta corresponde exatamente a um movimento no labirinto, minimizar a quantidade de arestas equivale a minimizar a quantidade de movimentos entre `A` e `B`.



## Representação

Após a modelagem do labirinto como um grafo, é necessário converter as posições da matriz para uma representação compatível com as estruturas utilizadas pela biblioteca `algs4`.

### Identificação dos vértices

Cada célula percorrível da matriz recebe um identificador numérico único.

Além do identificador utilizado internamente pelo grafo, é mantida uma associação entre:

- posição `(i,j)` da matriz;
- identificador numérico do vértice.

Conceitualmente:

```
posição na matriz  ↔  vértice do grafo

(2,3)              ↔  A
(2,2)              ↔  outro vértice
(3,2)              ↔  outro vértice




## Algoritmo

Para solucionar o problema foi escolhido o algoritmo **Breadth-First Search (BFS)**.

O BFS realiza uma busca em largura utilizando uma fila FIFO (*First In, First Out*). Dessa forma, os vértices são explorados em ordem crescente de distância em relação ao vértice de origem.

No Labyrinth, cada movimento entre duas células adjacentes possui o mesmo custo. Portanto, o grafo é não ponderado e a distância entre dois vértices pode ser medida pela quantidade de arestas percorridas.

A execução parte do vértice correspondente à posição `A`.

Durante a busca são mantidas três informações principais para cada vértice:

- `marked`: indica se o vértice já foi descoberto;
- `edgeTo`: registra o predecessor utilizado para chegar ao vértice;
- `distTo`: registra a quantidade mínima de arestas entre a origem e o vértice.

O funcionamento geral pode ser resumido como:

```
A entra na fila
      ↓
retirar vértice da frente
      ↓
percorrer seus vizinhos
      ↓
vizinho ainda não visitado?
      ↓ sim
marcar como visitado
      ↓
registrar predecessor
      ↓
distTo[vizinho] = distTo[atual] + 1
      ↓
adicionar vizinho à fila
```

Quando o vértice correspondente a `B` é encontrado, `distTo[B]` representa a distância mínima entre `A` e `B`.

Os predecessores registrados em `edgeTo` permitem reconstruir posteriormente o caminho realizado.

---

## Implementação de referência

A implementação utilizada como referência é baseada no algoritmo `BreadthFirstPaths`, apresentado em **Algorithms, 4th Edition**, de Robert Sedgewick e Kevin Wayne, e disponibilizado através da biblioteca `algs4`.

Para Python foi utilizada a biblioteca `algs4-py`, que procura manter a estrutura e as interfaces dos algoritmos apresentados no material original.

A implementação de referência do BFS utiliza principalmente:

```
Graph
Queue
marked
edgeTo
```

O algoritmo segue a estrutura tradicional:

```
origem
   ↓
Queue
   ↓
dequeue
   ↓
adj(v)
   ↓
novo vértice
   ↓
marked + edgeTo + enqueue
```

A classe `Graph` é utilizada para representar o grafo não direcionado através de listas de adjacência.

A fila utilizada pelo BFS segue a estrutura `Queue` disponibilizada pela biblioteca.

### Referências

- Algorithms, 4th Edition — Robert Sedgewick e Kevin Wayne
- Biblioteca algs4
- Implementação Python: `algs4-py`

---

## Alterações realizadas

A implementação de referência foi adaptada para atender às características específicas do problema **Labyrinth**.

### 1. Conversão da matriz em grafo

A implementação original do BFS recebe diretamente um grafo com vértices numéricos.

Entretanto, o Labyrinth fornece uma matriz.

Foi necessário criar uma etapa responsável por transformar:

```
matriz
   ↓
células livres
   ↓
vértices numéricos
   ↓
arestas entre células vizinhas
   ↓
Graph
```

Cada célula percorrível recebe um identificador numérico utilizado pela estrutura `Graph`.

Também são mantidos mapeamentos entre:

```
(i,j) → vértice
vértice → (i,j)
```

Isso permite utilizar os algoritmos de grafos sem perder as coordenadas originais do labirinto.

### 2. Identificação da origem e do destino

Durante a leitura da matriz são identificados:

```
A → vértice de origem
B → vértice de destino
```

Esses identificadores são utilizados posteriormente na execução do BFS.

### 3. Registro das distâncias

Além das estruturas de vértices visitados e predecessores, foi adicionada a estrutura:

```
distTo
```

A origem inicia com:

```
distTo[A] = 0
```

Sempre que um vértice `w` é descoberto a partir de `v`:

```
distTo[w] = distTo[v] + 1
```

Essa informação representa diretamente a quantidade mínima de movimentos necessária para alcançar cada vértice.

### 4. Reconstrução do caminho

A implementação de referência trabalha com caminhos entre vértices.

O problema Labyrinth, entretanto, exige uma sequência formada pelos caracteres:

```
L
R
U
D
```

Após obter o caminho entre os vértices `A` e `B`, as coordenadas consecutivas são comparadas.

Exemplo:

```
(2,3) → (2,2) = L
(2,2) → (3,2) = D
(3,2) → (4,2) = D
```

Dessa forma, um caminho entre vértices é convertido para o formato exigido pelo CSES.

No exemplo utilizado durante o trabalho:

```
LDDRRRRRU
```

### 5. Adequação da entrada e da saída

A implementação de referência foi adaptada para receber diretamente o formato do problema:

```
n m
labirinto
```

e produzir apenas as informações exigidas pelo juiz:

```
YES
comprimento
caminho
```

ou:

```
NO
```

---

## Justificativas

### Escolha do BFS

O DFS estudado anteriormente consegue determinar se `B` é alcançável a partir de `A`, porém não garante que o primeiro caminho encontrado seja mínimo.

O BFS foi escolhido porque o grafo é não ponderado e o algoritmo percorre os vértices em níveis de distância.

Assim, a primeira descoberta de um vértice corresponde à menor quantidade de arestas necessária para alcançá-lo.

### Uso de lista de adjacência

Cada célula possui no máximo quatro vizinhos.

Portanto, o grafo é esparso e a lista de adjacência evita o custo de uma matriz de adjacência de dimensão `V × V`.

### Uso de identificadores numéricos

As estruturas da `algs4` trabalham com vértices identificados numericamente.

Por isso, as posições `(i,j)` do labirinto são convertidas para identificadores numéricos.

O mapeamento inverso é preservado para que o caminho possa posteriormente ser convertido para movimentos.

### Uso de predecessores

A distância mínima informa quantos movimentos são necessários, mas não informa quais movimentos foram realizados.

O vetor `edgeTo` permite reconstruir o caminho entre o destino e a origem.

### Uso de `distTo`

O vetor `distTo` permite relacionar diretamente os níveis produzidos pelo BFS com a distância da origem.

Para cada nova descoberta:

```
distTo[w] = distTo[v] + 1
```

Assim, se `B` é encontrado com:

```
distTo[B] = 9
```

o menor caminho possui nove movimentos.

---

## Complexidade

O BFS possui complexidade:

\[
O(V+E)
\]

onde:

- `V` é a quantidade de vértices;
- `E` é a quantidade de arestas.

No Labyrinth, cada célula percorrível pode representar um vértice.

Para uma matriz de `n` linhas e `m` colunas:

\[
V \leq n \cdot m
\]

Cada vértice possui no máximo quatro vizinhos.

Consequentemente:

\[
E = O(V)
\]

Assim:

\[
O(V+E) = O(nm)
\]

### Tempo

A construção do grafo percorre a matriz:

\[
O(nm)
\]

A execução do BFS possui:

\[
O(V+E)
\]

que, para o Labyrinth, corresponde a:

\[
O(nm)
\]

A reconstrução do caminho possui custo proporcional ao tamanho do caminho e, no pior caso:

\[
O(nm)
\]

Portanto, a complexidade total permanece:

\[
\boxed{O(nm)}
\]

### Memória

São armazenados:

- a matriz;
- o grafo;
- os mapeamentos entre vértices e posições;
- `marked`;
- `edgeTo`;
- `distTo`;
- a fila do BFS.

No pior caso, essas estruturas possuem tamanho proporcional à quantidade de células.

Portanto:

\[
\boxed{O(nm)}
\]

de memória.