## Propriedade e critério de reconhecimento

**Propriedade:** existência de uma **ponte** em um grafo não dirigido. No problema, é necessário identificar todas as arestas críticas da rede.

**Critério:** durante uma busca em profundidade (DFS), cada vértice `v` recebe um tempo de descoberta `disc[v]` e um valor `low[v]`, que representa o menor tempo de descoberta alcançável a partir de `v`.

Ao explorar uma aresta de árvore entre `u` e `v`, a aresta é uma ponte quando:

```text
low[v] > disc[u]
```

Essa condição indica que a subárvore iniciada em `v` não possui outro caminho capaz de alcançar `u` ou algum ancestral de `u`. Portanto, a conexão `u—v` é o único caminho ligando aquela parte da rede ao restante da componente.

A aresta que liga um vértice ao seu pai na DFS é ignorada ao atualizar o valor `low`, pois representa a própria aresta utilizada para chegar ao vértice atual.

## Referências de `algs4` e adaptações previstas

- **`Graph.java` ou `graph.py`:** utilizar como referência para representar a rede por meio de listas de adjacência de um grafo não dirigido. No UVA 796, os vértices já são identificados de `0` até `n−1`.

- **`DepthFirstSearch.java` ou implementação equivalente:** utilizar como base para percorrer todas as componentes do grafo com DFS. A adaptação deverá acrescentar os vetores `disc`, `low` e `parent`.

- **DFS para pontes:** durante o retorno das chamadas da DFS, atualizar:

```text
low[u] = min(low[u], low[v])
```

para um filho `v` da árvore de busca.

Caso seja encontrada uma aresta para um vértice já visitado que não seja o pai de `u`, atualizar:

```text
low[u] = min(low[u], disc[v])
```

Após explorar completamente um filho `v`, verificar:

```text
low[v] > disc[u]
```

Se a condição for verdadeira, a aresta `u—v` deve ser registrada como um **critical link**.

Como o grafo pode possuir mais de uma componente conexa, a DFS deve ser iniciada novamente para cada vértice ainda não visitado.

## Rastreamento manual em uma instância pequena

Utilizamos a mesma instância do marco anterior:

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

Considerando os vizinhos em ordem crescente:

| Vértice | Vizinhos |
| ------- | -------- |
| 0 | 1, 2 |
| 1 | 0, 2, 3 |
| 2 | 0, 1 |
| 3 | 1, 4 |
| 4 | 3 |
| 5 | nenhum |

O rastreamento da DFS pode ser resumido da seguinte forma:

| Passo | Ação | `disc` / `low` | Decisão |
| ----- | ---- | -------------- | ------- |
| 1 | Iniciar DFS em `0` | `disc[0] = low[0] = 0` | Avançar para `1`. |
| 2 | Visitar `1` | `disc[1] = low[1] = 1` | Ignorar `0`, pois é o pai; avançar para `2`. |
| 3 | Visitar `2` | `disc[2] = low[2] = 2` | Encontrar `2—0`; atualizar `low[2] = 0`. |
| 4 | Retornar para `1` | `low[1] = 0` | `low[2] > disc[1]` é falso; `1—2` não é ponte. |
| 5 | De `1`, visitar `3` | `disc[3] = low[3] = 3` | Avançar para `4`. |
| 6 | Visitar `4` | `disc[4] = low[4] = 4` | Não existe caminho alternativo. |
| 7 | Retornar para `3` | `low[4] = 4` | `low[4] > disc[3]`; `3—4` é ponte. |
| 8 | Retornar para `1` | `low[3] = 3` | `low[3] > disc[1]`; `1—3` é ponte. |
| 9 | Retornar para `0` | `low[1] = 0` | `low[1] > disc[0]` é falso; `0—1` não é ponte. |
| 10 | Iniciar DFS em `5` | `disc[5] = low[5] = 5` | Vértice isolado; nenhuma ponte adicional. |

Ao final da execução, são encontrados dois **critical links**:

```text
1 - 3
3 - 4
```

O ciclo formado por `0`, `1` e `2` impede que suas arestas sejam pontes, pois existem caminhos alternativos entre esses vértices.

## Estimativa de complexidade

Sejam `V` o número de vértices e `E` o número de arestas.

- **Tempo: `O(V + E)`.** Cada vértice é visitado uma única vez pela DFS e cada aresta é examinada em seus dois sentidos.
- **Memória total: `O(V + E)`.** A lista de adjacência ocupa `O(V + E)`, enquanto os vetores `disc`, `low`, `parent` e `visited`, além da pilha da DFS, ocupam `O(V)`.
- **Memória auxiliar: `O(V)`.** Desconsiderando a estrutura utilizada para armazenar o grafo.

Dessa forma, a utilização de DFS com os valores `disc` e `low` permite identificar todos os links críticos em uma única exploração do grafo.