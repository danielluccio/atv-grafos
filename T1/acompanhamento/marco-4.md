# Marco 4 — Aplicação básica de BFS e conclusão

## Objetivo do marco

No quarto acompanhamento foi aplicado o algoritmo **Breadth-First Search (BFS)** ao problema Labyrinth.

Os itens abordados foram:

- execução manual;
- fila;
- `enqueue` e `dequeue`;
- níveis;
- distâncias;
- predecessores;
- comparação entre DFS e BFS;
- escolha justificada;
- adaptação;
- integração;
- testes;
- complexidade;
- submissão;
- resultado `Accepted`;
- ensaio da apresentação.

---

## Motivação para utilizar BFS

No Marco 3 foi identificado que o DFS consegue encontrar um caminho entre `A` e `B`, mas não garante que esse caminho seja mínimo.

O Labyrinth exige justamente um caminho com a menor quantidade de movimentos.

Como todos os movimentos possuem o mesmo custo, o grafo é não ponderado.

Nesse cenário, o BFS é adequado porque explora os vértices em ordem crescente de distância a partir da origem.

---

## Estrutura principal: fila

O BFS utiliza uma fila do tipo:

```text
FIFO — First In, First Out
```

As duas operações principais observadas durante a execução manual foram:

```text
enqueue -> adicionar um vértice ao final da fila
dequeue -> remover o vértice que está na frente da fila
```

Essa política de fila é a razão pela qual o BFS processa os vértices por níveis.

---

## Execução manual

O exemplo utilizado foi:

```text
########
#.A#...#
#.##.#B#
#......#
########
```

Com:

```text
A = (2,3)
B = (3,7)
```

ou, utilizando a abstração numérica:

```text
A = 2
B = 8
```

A execução começa com:

```text
dist[A] = 0
fila = [A]
```

O primeiro evento é:

```text
ENQUEUE A
```

Depois:

```text
DEQUEUE A
```

Se um vizinho ainda não foi visitado, ele é descoberto, recebe uma distância e entra na fila.

Exemplo:

```text
A descobre (2,2)

dist[(2,2)] = dist[A] + 1
dist[(2,2)] = 1

ENQUEUE (2,2)
```

Na execução manual foram acompanhadas as seguintes informações:

```text
operação | vértice | dist | fila
```

Isso permitiu visualizar separadamente cada `enqueue` e `dequeue`.

---

## Níveis do BFS

No BFS, os vértices podem ser agrupados pela distância em relação à origem.

Para o exemplo:

```text
nível 0 -> A
nível 1 -> (2,2)
nível 2 -> (3,2)
nível 3 -> (4,2)
nível 4 -> (4,3)
nível 5 -> (4,4)
nível 6 -> (4,5)
nível 7 -> (4,6), (3,5)
nível 8 -> (4,7), (2,5)
nível 9 -> B(3,7), (2,6)
```

Assim:

\[
dist(B)=9
\]

---

## Por que os níveis garantem o menor caminho?

Quando um vértice de nível `d` é processado, os novos vértices descobertos são colocados no final da fila com nível `d+1`.

Dessa forma, todos os vértices de uma determinada distância são processados antes dos vértices de uma distância maior.

A ordem conceitual é:

```text
distância 0
    |
distância 1
    |
distância 2
    |
distância 3
    |
   ...
```

Portanto, quando `B` é descoberto pela primeira vez, já foram consideradas todas as possibilidades de chegar a ele utilizando uma quantidade menor de arestas.

É por isso que a primeira distância atribuída a `B` é a distância mínima.

---

## Distâncias

Quando um vértice `v` é descoberto a partir de `u`:

\[
dist[v] = dist[u] + 1
\]

No exemplo:

```text
dist[A]       = 0
dist[(2,2)]   = 1
dist[(3,2)]   = 2
dist[(4,2)]   = 3
dist[(4,3)]   = 4
dist[(4,4)]   = 5
dist[(4,5)]   = 6
dist[(4,6)]   = 7
dist[(4,7)]   = 8
dist[B]       = 9
```

---

## Predecessores

Além da distância, foi estudado o uso de predecessores.

Quando `v` é descoberto a partir de `u`:

```text
edgeTo[v] = u
```

Para o menor caminho do exemplo:

```text
(2,2) <- A
(3,2) <- (2,2)
(4,2) <- (3,2)
(4,3) <- (4,2)
(4,4) <- (4,3)
(4,5) <- (4,4)
(4,6) <- (4,5)
(4,7) <- (4,6)
B      <- (4,7)
```

---

## Reconstrução do caminho

Após encontrar `B`, os predecessores podem ser percorridos no sentido contrário:

```text
B
<- (4,7)
<- (4,6)
<- (4,5)
<- (4,4)
<- (4,3)
<- (4,2)
<- (3,2)
<- (2,2)
<- A
```

Invertendo a sequência:

```text
A
-> (2,2)
-> (3,2)
-> (4,2)
-> (4,3)
-> (4,4)
-> (4,5)
-> (4,6)
-> (4,7)
-> B
```

Comparando as posições consecutivas, obtemos:

```text
L D D R R R R R U
```

Portanto:

```text
LDDRRRRRU
```

com comprimento:

```text
9
```

Uma saída válida para o exemplo é:

```text
YES
9
LDDRRRRRU
```

---

## Comparação entre DFS e BFS

| Característica | DFS | BFS |
|---|---|---|
| Estrutura principal | Pilha/recursão | Fila |
| Estratégia | Profundidade | Largura |
| Determina alcançabilidade | Sim | Sim |
| Utiliza predecessores | Sim | Sim |
| Explora por níveis | Não | Sim |
| Garante menor caminho em grafo não ponderado | Não | Sim |
| Complexidade | `O(V+E)` | `O(V+E)` |

A escolha do BFS não foi motivada por uma complexidade assintótica menor.

Os dois algoritmos possuem:

\[
O(V+E)
\]

A escolha foi realizada porque o BFS possui a propriedade exigida pelo problema: **menor caminho em grafo não ponderado**.

---

## Escolha justificada

A justificativa adotada pela equipe foi:

> O DFS consegue determinar a alcançabilidade entre `A` e `B`, porém não garante o menor caminho. Como o Labyrinth é representado por um grafo não ponderado, em que cada movimento possui custo unitário, o BFS é mais adequado, pois explora os vértices em ordem crescente de distância e garante a menor quantidade de arestas entre a origem e o destino.

---

## Adaptação ao problema

Para adaptar o BFS ao labirinto, cada célula livre é tratada como um vértice.

Para uma posição `(i,j)`, são avaliadas no máximo quatro direções:

```text
cima      -> (i-1,j)
baixo     -> (i+1,j)
esquerda  -> (i,j-1)
direita   -> (i,j+1)
```

Antes de considerar uma posição como novo vértice da busca, são verificadas três condições:

1. a posição está dentro dos limites da matriz;
2. a posição não é uma parede;
3. o vértice ainda não foi visitado.

Quando o novo vértice é descoberto:

```text
marcar visitado
      |
definir dist
      |
definir predecessor
      |
enqueue
```

O vértice é marcado como visitado no momento em que entra na fila, evitando múltiplas inserções do mesmo vértice.

---

## Integração

A solução completa pode ser dividida conceitualmente em:

```text
ler entrada
    |
localizar A e B
    |
construir/obter representação do grafo
    |
executar BFS a partir de A
    |
B foi encontrado?
  /       \
não       sim
 |         |
NO    reconstruir caminho
           |
       YES + tamanho + movimentos
```

A etapa de reconstrução utiliza os predecessores produzidos pela busca.

---

## Testes

A equipe considerou diferentes classes de teste.

### 1. Caminho existente

O destino pode ser alcançado.

Resultado esperado:

```text
YES
```

seguido do tamanho e de um caminho mínimo.

### 2. Caminho inexistente

`A` e `B` pertencem a componentes diferentes.

Resultado esperado:

```text
NO
```

### 3. Mais de um menor caminho

Quando existem vários caminhos mínimos, o BFS pode retornar qualquer um deles.

A ordem de análise dos vizinhos pode alterar a sequência de movimentos retornada, mas não a distância mínima.

### 4. Casos pequenos

Casos pequenos ajudam a validar:

- indexação;
- reconstrução do caminho;
- tratamento de paredes;
- início e destino próximos.

### 5. Casos maiores

Casos maiores permitem observar se a solução permanece dentro dos limites de tempo e memória.

---

## Complexidade

O BFS possui:

\[
O(V+E)
\]

de complexidade de tempo quando o grafo é representado por lista de adjacência.

No Labyrinth existem no máximo:

\[
V = n \times m
\]

vértices.

Como cada célula possui no máximo quatro vizinhos:

\[
E = O(V)
\]

Logo:

\[
O(V+E)=O(nm)
\]

### Tempo

\[
O(nm)
\]

### Memória

Também é necessário espaço proporcional ao número de células para estruturas como:

- representação do grafo;
- visitados;
- fila;
- distâncias;
- predecessores.

Portanto:

\[
O(nm)
\]

---

## Submissão e Accepted

Depois da integração e dos testes, a solução foi submetida ao juiz do CSES.

O resultado obtido foi:

```text
Accepted
```

Esse resultado valida, de forma prática, que a implementação produziu respostas compatíveis com os casos de teste do juiz dentro dos limites estabelecidos.

A evidência correspondente deve permanecer armazenada no diretório:

```text
evidencias/
```

É importante observar que o `Accepted` é uma validação experimental da implementação.

A justificativa teórica da correção do menor caminho vem da propriedade do BFS em grafos não ponderados.

---

## Ensaio da apresentação

Antes da conclusão do marco, também foi realizado um ensaio da explicação do problema.

A sequência utilizada para apresentar o raciocínio foi:

```text
problema
   |
modelagem
   |
representação
   |
DFS
   |
limitação do DFS
   |
BFS
   |
fila e níveis
   |
distâncias
   |
predecessores
   |
menor caminho
   |
complexidade
   |
testes
   |
Accepted
```

O objetivo foi evitar uma apresentação baseada apenas em código e priorizar a explicação das decisões algorítmicas.

---

## Conclusão do marco

O Marco 4 encerrou a evolução dos acompanhamentos.

A sequência de decisões foi:

```text
Labyrinth
    |
modelagem como grafo
    |
representação
    |
DFS
    |
alcançabilidade
    |
não garante menor caminho
    |
BFS
    |
exploração por níveis
    |
distância mínima
    |
predecessores
    |
reconstrução
    |
testes
    |
Accepted
```

A principal conclusão é que o BFS foi escolhido não por ser assintoticamente mais rápido que o DFS, mas porque possui a propriedade necessária ao problema: encontrar o menor caminho em um grafo não ponderado.
