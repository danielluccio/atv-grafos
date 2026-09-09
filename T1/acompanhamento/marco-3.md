# Marco 3 — Aplicação básica de DFS

## Objetivo do marco

No terceiro acompanhamento foi estudado o algoritmo **Depth-First Search (DFS)** aplicado ao grafo do Labyrinth.

Os assuntos trabalhados foram:

- execução manual;
- estados dos vértices;
- árvore DFS;
- tempos de descoberta e término;
- alcançabilidade;
- predecessores (`edgeTo`);
- aplicabilidade do DFS ao problema;
- complexidade.

O objetivo deste marco não foi afirmar que DFS era a solução final do Labyrinth, mas compreender seu comportamento e analisar até onde ele atendia às necessidades do problema.

---

## Funcionamento do DFS

O DFS realiza uma busca em profundidade.

A partir de um vértice, o algoritmo escolhe um vizinho ainda não visitado e continua avançando por esse caminho.

Quando chega a um vértice que não possui novos vizinhos disponíveis, ocorre o **retorno** da busca para um vértice anterior.

Conceitualmente:

```text
origem
  |
  v
vizinho
  |
  v
vizinho
  |
  v
...
  |
sem novo vizinho
  |
  v
retorno
```

O DFS pode ser implementado utilizando recursão ou uma pilha explícita.

---

## Estados dos vértices

Durante a execução manual, foi utilizada a ideia de estados para acompanhar o progresso da busca.

Uma interpretação comum é:

- **não visitado** — o vértice ainda não foi descoberto;
- **em processamento** — o vértice já foi descoberto, mas sua exploração ainda não terminou;
- **finalizado** — todos os seus vizinhos já foram analisados.

Esses estados ajudam a compreender o funcionamento da recursão, os retornos e os tempos do DFS.

---

## Execução manual no exemplo

Foi utilizado o mesmo labirinto:

```text
########
#.A#...#
#.##.#B#
#......#
########
```

Com a abstração numérica:

```text
A = 2
B = 8
```

Uma possível execução do DFS, considerando os vizinhos em ordem crescente de identificador, possui a seguinte ordem de descoberta:

```text
2 -> 1 -> 6 -> 9 -> 10 -> 11 -> 12
   -> 7 -> 3 -> 4 -> 5 -> 8 -> 14 -> 13
```

A ordem exata pode mudar caso a ordem dos vizinhos da lista de adjacência seja alterada.

Esse fato foi relevante para perceber que o DFS não percorre o grafo em ordem de distância.

---

## Predecessores — edgeTo

Quando um novo vértice `v` é descoberto a partir de um vértice `u`, podemos registrar:

```text
edgeTo[v] = u
```

Para a execução acima:

| Vértice | Predecessor |
|---:|---:|
| 2 | — |
| 1 | 2 |
| 6 | 1 |
| 9 | 6 |
| 10 | 9 |
| 11 | 10 |
| 12 | 11 |
| 7 | 12 |
| 3 | 7 |
| 4 | 3 |
| 5 | 4 |
| 8 | 5 |
| 14 | 8 |
| 13 | 14 |

Esses predecessores formam a **árvore DFS**.

---

## Árvore DFS

Para essa ordem de execução, a árvore produzida pode ser visualizada como:

```text
2
|
1
|
6
|
9
|
10
|
11
|
12
|
7
|
3
|
4
|
5
|
8
|
14
|
13
```

Neste exemplo específico, a ordem escolhida faz com que a árvore tenha uma forma bastante profunda.

Isso ilustra diretamente o comportamento do DFS: aprofundar um caminho antes de explorar outras possibilidades.

---

## Tempos de descoberta e término

Também foi estudado o conceito de tempo no DFS.

O relógio lógico é incrementado quando:

1. um vértice é descoberto;
2. um vértice termina de ser processado.

Para a ordem de vizinhos adotada no exemplo, uma possível tabela é:

| Vértice | Descoberta | Término |
|---:|---:|---:|
| 2 | 1 | 28 |
| 1 | 2 | 27 |
| 6 | 3 | 26 |
| 9 | 4 | 25 |
| 10 | 5 | 24 |
| 11 | 6 | 23 |
| 12 | 7 | 22 |
| 7 | 8 | 21 |
| 3 | 9 | 20 |
| 4 | 10 | 19 |
| 5 | 11 | 18 |
| 8 | 12 | 17 |
| 14 | 13 | 16 |
| 13 | 14 | 15 |

Os valores não representam segundos reais.

Eles representam uma ordem lógica dos eventos da busca.

Por exemplo:

```text
d[2] = 1
f[2] = 28
```

significa que o vértice `2` foi o primeiro a ser descoberto e somente foi finalizado após o término de toda a exploração iniciada a partir dele.

---

## Alcançabilidade

Uma aplicação direta do DFS é verificar se um vértice pode ser alcançado a partir de outro.

Se a busca for iniciada em `A` e `B` for marcado como visitado, podemos concluir que existe pelo menos um caminho entre eles.

No exemplo:

```text
A = 2
B = 8
```

e o vértice `8` é visitado.

Portanto, `B` é alcançável a partir de `A`.

Se a execução terminasse sem visitar `B`, concluiríamos que não existe caminho entre os dois vértices.

---

## Aplicabilidade ao Labyrinth

O DFS atende corretamente à pergunta:

> Existe algum caminho entre `A` e `B`?

Entretanto, o problema do CSES exige algo adicional:

> Encontrar um caminho de menor comprimento.

O DFS não garante que o primeiro caminho encontrado seja o menor.

Considere o exemplo conceitual:

```text
A --- x --- x --- x --- x --- B
|
x --- B
```

Dependendo da ordem dos vizinhos, o DFS pode seguir primeiro o caminho superior e encontrar `B` utilizando mais arestas, mesmo existindo um caminho menor.

---

## Complexidade

Com lista de adjacência, o DFS possui complexidade:

\[
O(V+E)
\]

No Labyrinth:

\[
V = O(nm)
\]

Como cada vértice possui no máximo quatro vizinhos:

\[
E = O(V)
\]

Logo:

\[
O(V+E) = O(nm)
\]

---

## Conclusão do marco

O Marco 3 mostrou que DFS é adequado para:

- percorrer o grafo;
- determinar alcançabilidade;
- construir uma árvore de busca;
- registrar predecessores;
- analisar tempos de descoberta e término.

Entretanto, foi identificada uma limitação fundamental:

> DFS não garante o menor caminho em um grafo não ponderado.

Essa conclusão foi o ponto de partida para o Marco 4, no qual foi estudado o BFS.
