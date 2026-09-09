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

```text
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

```text
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

```text
posição na matriz  ↔  vértice do grafo

(2,3)              ↔  A
(2,2)              ↔  outro vértice
(3,2)              ↔  outro vértice
...