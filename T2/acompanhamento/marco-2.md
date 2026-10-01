## Caso particular e representação

Retomamos uma instância pequena do problema **UVA 796 - Critical Links**, com `V = 6` e `E = 5`, dentro dos limites deste marco (`V ≤ 6` e `E ≤ 6`):

```text
6
0 (2) 1 2
1 (3) 0 2 3
2 (2) 0 1
3 (2) 1 4
4 (1) 3
5 (0)
```

O grafo representa uma rede de servidores com conexões bidirecionais. Seu desenho é:

```text
0 ----- 1 ----- 3 ----- 4
 \     /
  \   /
    2

5
```

O vértice `5` representa um servidor isolado. Considerando os vizinhos em ordem crescente, as listas de adjacência são:

| Vértice | Vizinhos |
| ------- | -------- |
| 0 | 1, 2 |
| 1 | 0, 2, 3 |
| 2 | 0, 1 |
| 3 | 1, 4 |
| 4 | 3 |
| 5 | nenhum |

Neste caso, as arestas `1 — 3` e `3 — 4` são **critical links**. A remoção de qualquer uma delas aumenta a quantidade de componentes conexas. Já as arestas entre `0`, `1` e `2` não são críticas, pois esses vértices formam um ciclo e possuem caminhos alternativos.

## Excentricidades, raio, diâmetro e centro

As componentes conexas do grafo original são:

```text
C₀ = {0, 1, 2, 3, 4}
C₁ = {5}
```

As distâncias dentro de `C₀` são:

| Origem | `d(·,0)` | `d(·,1)` | `d(·,2)` | `d(·,3)` | `d(·,4)` | Excentricidade |
| ------ | -------- | -------- | -------- | -------- | -------- | -------------- |
| 0 | 0 | 1 | 1 | 2 | 3 | 3 |
| 1 | 1 | 0 | 1 | 1 | 2 | 2 |
| 2 | 1 | 1 | 0 | 2 | 3 | 3 |
| 3 | 2 | 1 | 2 | 0 | 1 | 2 |
| 4 | 3 | 2 | 3 | 1 | 0 | 3 |

Em `C₀`, a menor excentricidade é `2`. Portanto, o **raio é `2`** e o **centro é `{1, 3}`**. A maior excentricidade é `3`, logo o **diâmetro é `3`**.

Um exemplo de caminho que representa o diâmetro é:

```text
0 — 1 — 3 — 4
```

Em `C₁`, existe apenas o vértice `5`, portanto sua excentricidade é `0`, assim como o raio e o diâmetro dessa componente. Seu centro é `{5}`.

## Rastreamento manual das componentes conexas

Para identificar as componentes conexas, utilizamos uma DFS. A busca mantém `marked[v]`, indicando se o vértice já foi visitado, `id[v]`, indicando a componente à qual pertence, e `size[c]`, indicando o tamanho da componente.

Considerando os vértices e seus vizinhos em ordem crescente:

| Passo | Chamada ou retorno | Pilha de chamadas | Visitados e identificadores | Tamanhos e `count` |
| ----- | ------------------ | ----------------- | --------------------------- | ------------------ |
| 1 | Iniciar `dfs(0)` | `0` | `marked[0]`, `id[0] = 0` | `size[0] = 1`, `count = 0` |
| 2 | De `0`, chamar `dfs(1)` | `0 → 1` | `marked[1]`, `id[1] = 0` | `size[0] = 2` |
| 3 | De `1`, chamar `dfs(2)` | `0 → 1 → 2` | `marked[2]`, `id[2] = 0` | `size[0] = 3` |
| 4 | Retornar para `1` e chamar `dfs(3)` | `0 → 1 → 3` | `marked[3]`, `id[3] = 0` | `size[0] = 4` |
| 5 | De `3`, chamar `dfs(4)` | `0 → 1 → 3 → 4` | `marked[4]`, `id[4] = 0` | `size[0] = 5` |
| 6 | Finalizar a DFS iniciada em `0` | vazia | `{0,1,2,3,4}` têm `id = 0` | `count = 1` |
| 7 | Encontrar `5` não visitado e chamar `dfs(5)` | `5` | `marked[5]`, `id[5] = 1` | `size[1] = 1` |
| 8 | Retornar de `5` | vazia | Todos visitados | `count = 2` |

Ao final, temos:

```text
C₀ = {0, 1, 2, 3, 4}
C₁ = {5}
```

Esse percurso também será importante na solução do problema, pois a identificação dos **critical links** utiliza uma DFS para analisar se uma subárvore possui ou não outro caminho para alcançar vértices já descobertos.

## Custo do algoritmo e das consultas

Com listas de adjacência, a identificação das componentes conexas utilizando DFS possui custo de **`O(V + E)` em tempo**, pois cada vértice é visitado uma vez e cada aresta não dirigida é analisada em seus dois sentidos.

A representação por lista de adjacência ocupa **`O(V + E)` de memória**, enquanto os vetores utilizados pela DFS e sua pilha de chamadas ocupam **`O(V)` de memória auxiliar** no pior caso.

Depois da identificação das componentes, verificar se dois servidores pertencem à mesma componente possui custo **`O(1)`**, bastando comparar seus identificadores. Por exemplo:

```text
id[0] = id[4]
id[0] ≠ id[5]
```

O cálculo de distâncias, excentricidades, raio, diâmetro e centro é realizado separadamente para cada componente conexa e não faz parte diretamente do algoritmo utilizado para encontrar os **critical links**.