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


```
# T2 — Resolução de Problemas com Grafos

## Problema

### UVA 796 — Critical Links

O problema atribuído à equipe no T2 é o **UVA 796 — Critical Links**.

O problema representa uma rede de computadores por meio de servidores e conexões entre eles. Algumas dessas conexões são consideradas **críticas**, pois sua remoção faz com que uma parte da rede deixe de possuir comunicação com outra parte anteriormente conectada.

Em termos de Teoria dos Grafos, essas conexões correspondem às **pontes** de um grafo.

Uma aresta é uma ponte quando sua remoção aumenta a quantidade de componentes conexas do grafo.

---

## Entrada, saída e restrições

A entrada informa inicialmente a quantidade `n` de servidores da rede.

Em seguida, são fornecidas `n` linhas descrevendo as conexões de cada servidor no formato:

```text
u (k) v1 v2 ... vk
```

onde:

- `u` representa o servidor atual;
- `k` representa a quantidade de servidores diretamente conectados a `u`;
- `v1 ... vk` representam seus vizinhos.

Os servidores são identificados numericamente de:

```text
0 até n - 1
```

As conexões são bidirecionais e a rede pode possuir mais de uma componente conexa.

A saída deve informar inicialmente a quantidade de conexões críticas encontradas:

```text
X critical links
```

seguida das pontes no formato:

```text
u - v
```

As arestas encontradas devem ser apresentadas em ordem crescente.

---

## Modelagem

A rede pode ser modelada como um grafo:

\[
G = (V,E)
\]

onde:

- `V` representa o conjunto de servidores;
- `E` representa o conjunto de conexões existentes entre os servidores.

### Vértices

Cada servidor corresponde diretamente a um vértice do grafo.

Como os servidores já são identificados por valores inteiros de `0` até `n - 1`, não é necessária uma etapa adicional de conversão de identificadores.

### Arestas

Cada conexão entre dois servidores `u` e `v` é representada por uma aresta:

\[
(u,v) \in E
\]

Como as conexões funcionam nos dois sentidos:

\[
(u,v) = (v,u)
\]

Portanto, o grafo é **não direcionado**.

### Características do grafo

A partir do enunciado, o grafo possui as seguintes características:

- **não direcionado:** as conexões são bidirecionais;
- **não ponderado:** não existe custo associado às conexões;
- **possivelmente desconexo:** podem existir grupos de servidores sem conexão entre si;
- **representado por lista de adjacência:** adequada para percorrer diretamente os vizinhos de cada vértice.

### Objetivo no grafo

O problema passa a ser:

> identificar todas as arestas de `G` cuja remoção aumenta a quantidade de componentes conexas.

Essas arestas são denominadas **pontes** e correspondem aos **critical links** solicitados pelo problema.

---

## Representação

A representação utilizada será baseada na estrutura `Graph` da biblioteca **algs4-py**, que representa grafos não direcionados utilizando listas de adjacência.

Conceitualmente:

```text
0 → [1, 2]
1 → [0, 2, 3]
2 → [0, 1]
3 → [1, 4]
4 → [3]
5 → []
```

A lista de adjacência é adequada porque permite percorrer apenas as arestas realmente existentes.

Não há necessidade de utilizar uma matriz `V × V`, principalmente porque o algoritmo necessita consultar repetidamente os vizinhos dos vértices durante a DFS.

---

## Propriedade e critério de reconhecimento

A propriedade procurada é a existência de uma **ponte**.

Para reconhecer uma ponte durante uma DFS, cada vértice `v` mantém duas informações principais:

```text
disc[v]
low[v]
```

### `disc`

`disc[v]` representa o instante em que o vértice `v` foi descoberto pela DFS.

Por exemplo:

```text
disc[0] = 0
disc[1] = 1
disc[2] = 2
```

Esses valores representam a ordem de descoberta dos vértices.

### `low`

`low[v]` representa o menor tempo de descoberta que pode ser alcançado partindo de `v` ou de sua subárvore da DFS.

Inicialmente:

```text
low[v] = disc[v]
```

Esse valor pode diminuir caso a DFS encontre um caminho que permita retornar a algum vértice descoberto anteriormente.

---

## Critério para identificar uma ponte

Considere que, durante a DFS, `u` descobre um novo vértice `v`.

A aresta:

```text
u — v
```

é uma ponte quando:

```text
low[v] > disc[u]
```

Isso significa que `v` e sua subárvore não possuem nenhum outro caminho capaz de alcançar `u` ou algum ancestral de `u`.

Portanto, a aresta `u — v` é a única conexão entre essa subárvore e o restante da componente.

Se ela for removida, o grafo será separado.

---

## Atualização dos valores `low`

Existem duas situações principais durante a DFS.

### Aresta de árvore

Se `v` ainda não foi visitado, a DFS continua recursivamente por ele.

Após o retorno:

```text
low[u] = min(low[u], low[v])
```

Dessa forma, `u` recebe a informação sobre o vértice mais antigo que a subárvore de `v` consegue alcançar.

### Aresta para vértice já descoberto

Se `v` já foi visitado e não é o pai de `u` na DFS:

```text
low[u] = min(low[u], disc[v])
```

Essa situação indica a existência de um caminho alternativo para um vértice descoberto anteriormente.

A aresta que liga `u` ao seu pai não deve ser considerada nesse cálculo, pois corresponde à própria aresta utilizada pela DFS para chegar a `u`.

---

## Algoritmo

A solução utiliza uma **Busca em Profundidade (DFS)** com o cálculo dos valores `disc` e `low`, aplicando o critério utilizado pelo algoritmo de Tarjan para identificação de pontes.

Para cada vértice serão mantidas as seguintes informações:

```text
visited
disc
low
parent
```

onde:

- `visited[v]` indica se o vértice já foi descoberto;
- `disc[v]` armazena seu tempo de descoberta;
- `low[v]` armazena o menor tempo de descoberta alcançável;
- `parent[v]` informa qual vértice descobriu `v`.

Também será mantido um contador utilizado para gerar os tempos de descoberta.

O funcionamento geral pode ser representado como:

```text
iniciar DFS em u
       ↓
marcar u como visitado
       ↓
disc[u] = low[u] = tempo
       ↓
percorrer adj(u)
       ↓
vizinho ainda não visitado?
       ↓ sim
parent[v] = u
       ↓
DFS(v)
       ↓
low[u] = min(low[u], low[v])
       ↓
low[v] > disc[u] ?
       ↓ sim
u — v é uma ponte
```

Quando o vizinho já foi visitado e não corresponde ao pai:

```text
low[u] = min(low[u], disc[v])
```

---

## Tratamento de componentes desconexas

O problema permite que a rede possua mais de uma componente conexa.

Portanto, não é suficiente executar a DFS apenas a partir do vértice `0`.

É necessário percorrer todos os vértices:

```text
para cada vértice v:
    se v ainda não foi visitado:
        iniciar DFS(v)
```

Assim, todas as componentes do grafo são analisadas.

Um vértice isolado também será visitado, mas nenhuma ponte será encontrada a partir dele.

---

## Implementação de referência

A implementação será desenvolvida utilizando **Python** e tomando como base as estruturas disponibilizadas pela biblioteca **algs4-py**.

A principal estrutura utilizada é:

```text
Graph
```

responsável pela representação do grafo não direcionado por meio de listas de adjacência.

Como referência para a estratégia de percurso será utilizada a estrutura de uma **Depth-First Search (DFS)**.

A DFS tradicional fornece principalmente o mecanismo de:

```text
marcar vértice
      ↓
percorrer adjacências
      ↓
visitar vértices ainda não descobertos
      ↓
retornar pela árvore da DFS
```

Entretanto, apenas executar a DFS não é suficiente para identificar pontes.

Por isso, são necessários pontos de extensão sobre a implementação de referência.

---

## Alterações realizadas sobre a referência da `algs4`

### 1. Leitura do formato do UVA 796

A estrutura `Graph` recebe vértices e arestas, enquanto o problema fornece linhas no formato:

```text
0 (2) 1 2
1 (3) 0 2 3
```

Portanto, a entrada deve ser interpretada para identificar:

```text
servidor
quantidade de vizinhos
lista de vizinhos
```

e posteriormente construir o grafo.

---

### 2. Tempos de descoberta

A DFS tradicional precisa ser estendida com:

```text
disc[v]
```

Quando um vértice é visitado:

```text
disc[v] = tempo
```

e o contador é incrementado.

---

### 3. Valores `low`

Também é acrescentado:

```text
low[v]
```

Inicialmente:

```text
low[v] = disc[v]
```

Durante o retorno das chamadas recursivas:

```text
low[u] = min(low[u], low[v])
```

Para uma conexão com um vértice já descoberto:

```text
low[u] = min(low[u], disc[v])
```

---

### 4. Registro do pai

Para distinguir a aresta utilizada pela DFS das demais conexões, será mantido:

```text
parent[v]
```

Assim, ao encontrar um vizinho já visitado, a atualização de `low` só é realizada quando:

```text
v != parent[u]
```

---

### 5. Identificação das pontes

Após retornar da DFS executada sobre um filho `v`, será verificada a condição:

```text
low[v] > disc[u]
```

Se for verdadeira:

```text
u — v
```

é registrado como um **critical link**.

---

### 6. Percurso de todas as componentes

A DFS da implementação de referência passa a ser executada para cada vértice ainda não visitado.

Isso garante o tratamento correto de grafos desconexos.

---

### 7. Ordenação da resposta

As pontes serão armazenadas de forma padronizada:

```text
(min(u, v), max(u, v))
```

Após a execução completa, serão ordenadas antes da impressão.

Isso permite produzir a saída exigida pelo problema:

```text
1 - 3
3 - 4
```

em ordem crescente.

---

## Justificativas

### Uso de DFS

A identificação de pontes depende da relação entre a árvore produzida pela busca e os caminhos alternativos encontrados durante o percurso.

A DFS permite identificar naturalmente:

- relações entre pai e filho;
- ordem de descoberta;
- retornos da recursão;
- conexões com vértices anteriormente descobertos.

Essas informações permitem calcular `disc` e `low`.

### Uso de `disc`

Somente saber se um vértice foi visitado não informa quando ele foi descoberto.

`disc[v]` estabelece uma ordem temporal entre os vértices da árvore DFS.

### Uso de `low`

`low[v]` permite responder à principal questão do algoritmo:

> a subárvore de `v` consegue alcançar algum vértice descoberto antes de `u` sem utilizar novamente a aresta `u — v`?

Se conseguir, existe um caminho alternativo.

Se não conseguir, `u — v` é uma ponte.

### Uso de lista de adjacência

A DFS necessita percorrer os vizinhos dos vértices.

Com listas de adjacência, todas as arestas podem ser percorridas em tempo proporcional a:

\[
O(V+E)
\]

sem a necessidade de examinar posições que representam arestas inexistentes.

### Uso do vetor `parent`

Como o grafo é não direcionado, uma aresta:

```text
u — v
```

aparece nas listas de adjacência de ambos os vértices.

O vetor `parent` permite reconhecer que a conexão de `v` para `u`, quando `u` foi responsável por descobrir `v`, corresponde à mesma aresta utilizada pela DFS e não a um caminho alternativo.

---

## Instância utilizada para análise

Considere a seguinte entrada:

```text
6
0 (2) 1 2
1 (3) 0 2 3
2 (2) 0 1
3 (2) 1 4
4 (1) 3
5 (0)
```

Sua representação é:

```text
0 ----- 1 ----- 3 ----- 4
 \     /
  \   /
    2

5
```

As listas de adjacência são:

| Vértice | Vizinhos |
|---|---|
| `0` | `1, 2` |
| `1` | `0, 2, 3` |
| `2` | `0, 1` |
| `3` | `1, 4` |
| `4` | `3` |
| `5` | nenhum |

Nesse grafo:

```text
1 — 3
3 — 4
```

são pontes.

Os vértices:

```text
0, 1 e 2
```

formam um ciclo.

Consequentemente, existem caminhos alternativos entre eles e nenhuma das arestas desse ciclo é uma ponte.

O vértice `5` encontra-se isolado.

---

## Rastreamento manual

Considerando os vizinhos em ordem crescente, a DFS pode ser acompanhada da seguinte forma:

| Passo | Operação | `disc` / `low` | Resultado |
|---|---|---|---|
| 1 | Visitar `0` | `disc[0] = low[0] = 0` | Avançar para `1`. |
| 2 | Visitar `1` | `disc[1] = low[1] = 1` | `0` é o pai; avançar para `2`. |
| 3 | Visitar `2` | `disc[2] = low[2] = 2` | Encontrar conexão com `0`. |
| 4 | Processar `2 — 0` | `low[2] = 0` | Existe caminho alternativo. |
| 5 | Retornar para `1` | `low[1] = 0` | `1 — 2` não é ponte. |
| 6 | De `1`, visitar `3` | `disc[3] = low[3] = 3` | Avançar para `4`. |
| 7 | Visitar `4` | `disc[4] = low[4] = 4` | Não existe caminho alternativo. |
| 8 | Retornar para `3` | `low[4] = 4` | `low[4] > disc[3]`: `3 — 4` é ponte. |
| 9 | Retornar para `1` | `low[3] = 3` | `low[3] > disc[1]`: `1 — 3` é ponte. |
| 10 | Retornar para `0` | `low[1] = 0` | `0 — 1` não é ponte. |
| 11 | Visitar `5` | `disc[5] = low[5] = 5` | Vértice isolado. |

Ao final:

```text
2 critical links
1 - 3
3 - 4
```

---

## Componentes conexas da instância

A instância possui duas componentes:

```text
C₀ = {0, 1, 2, 3, 4}
C₁ = {5}
```

O vértice `5` constitui sozinho uma componente conexa.

Essa situação demonstra por que a solução precisa iniciar uma nova DFS sempre que encontrar um vértice ainda não visitado.

---

## Excentricidade, raio, diâmetro e centro

Como análise complementar da instância utilizada, as distâncias na componente:

```text
C₀ = {0, 1, 2, 3, 4}
```

são:

| Origem | `d(·,0)` | `d(·,1)` | `d(·,2)` | `d(·,3)` | `d(·,4)` | Excentricidade |
|---|---:|---:|---:|---:|---:|---:|
| `0` | 0 | 1 | 1 | 2 | 3 | **3** |
| `1` | 1 | 0 | 1 | 1 | 2 | **2** |
| `2` | 1 | 1 | 0 | 2 | 3 | **3** |
| `3` | 2 | 1 | 2 | 0 | 1 | **2** |
| `4` | 3 | 2 | 3 | 1 | 0 | **3** |

A menor excentricidade é:

```text
2
```

Portanto:

```text
raio = 2
centro = {1, 3}
```

A maior excentricidade é:

```text
3
```

portanto:

```text
diâmetro = 3
```

Um caminho correspondente ao diâmetro é:

```text
0 — 1 — 3 — 4
```

Para a componente:

```text
C₁ = {5}
```

temos:

```text
excentricidade(5) = 0
raio = 0
diâmetro = 0
centro = {5}
```

Essas propriedades descrevem estruturalmente as componentes, mas **não fazem parte diretamente do algoritmo utilizado para identificar os critical links**.

---

## Complexidade

Sejam:

- `V` a quantidade de vértices;
- `E` a quantidade de arestas.

### Tempo

A DFS visita cada vértice uma única vez.

Cada aresta de um grafo não direcionado aparece nas listas de adjacência de seus dois extremos e é analisada durante o percurso.

Portanto:

\[
O(V+E)
\]

O cálculo de `disc`, `low` e a verificação:

```text
low[v] > disc[u]
```

são realizados durante a própria DFS e não alteram sua ordem de complexidade.

A ordenação das pontes encontradas é realizada somente após o percurso do grafo.

Considerando `B` como a quantidade de pontes encontradas, essa etapa possui custo:

\[
O(B \log B)
\]

Como:

\[
B \leq E
\]

a parte principal da identificação das pontes permanece:

\[
\boxed{O(V+E)}
\]

---

## Memória

A representação por lista de adjacência necessita:

\[
O(V+E)
\]

de memória.

Além do grafo, são mantidas estruturas de tamanho proporcional ao número de vértices:

```text
visited
disc
low
parent
```

A pilha de chamadas da DFS também pode atingir:

\[
O(V)
\]

no pior caso.

Portanto, considerando também o armazenamento do grafo:

\[
\boxed{O(V+E)}
\]

de memória total.

Desconsiderando a estrutura utilizada para armazenar o próprio grafo, a memória auxiliar utilizada pelo algoritmo é:

\[
\boxed{O(V)}
\]

---

## Resultado esperado

A solução deve ser capaz de:

1. interpretar a entrada fornecida pelo UVA 796;
2. construir o grafo utilizando a estrutura da `algs4-py`;
3. percorrer todas as componentes utilizando DFS;
4. calcular os valores `disc` e `low`;
5. identificar uma aresta `u — v` como ponte quando:

```text
low[v] > disc[u]
```

6. armazenar todos os **critical links** encontrados;
7. ordenar as arestas;
8. produzir a saída no formato exigido pelo problema.

A principal adaptação em relação à DFS disponibilizada como referência pela `algs4` está, portanto, na inclusão das informações necessárias para analisar o retorno da busca e determinar se a subárvore de um vértice possui ou não outro caminho para alcançar vértices descobertos anteriormente.
```