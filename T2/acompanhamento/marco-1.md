### Entrada, saída e restrições

O problema designado à nossa equipe foi o problema D (**UVA 796 – Critical Links**), disponível na URL indicada. Basicamente, a premissa deste problema envolve identificar **links críticos (pontes)** dentro de um grafo, onde os vértices representam servidores e as arestas representam as conexões entre eles. Uma conexão é considerada crítica quando sua remoção separa uma parte da rede que antes estava conectada. :chatgpt-content-reference{index="0"}

## Entrada, saída e restrições

A entrada informa inicialmente o número `n` de servidores da rede. Em seguida, são fornecidas `n` linhas indicando, para cada servidor, a quantidade de conexões diretas e quais servidores estão conectados a ele.

Os servidores são identificados de `0` até `n - 1`. As conexões são bidirecionais, um servidor não possui conexão direta consigo mesmo e a rede pode possuir componentes desconexas. O enunciado não apresenta um limite máximo explícito para `n`. :chatgpt-content-reference{index="1"}

A saída deve apresentar a quantidade de **critical links** encontrados e, em seguida, cada uma dessas conexões no formato `u - v`, ordenadas de forma crescente. :chatgpt-content-reference{index="2"}

## Modelagem e classificação do grafo

- **Vértices:** servidores, identificados de `0` até `n - 1`.
- **Arestas:** conexões entre dois servidores.
- **Classificação:** grafo não direcionado e não ponderado, podendo ser desconexo.
- **Resposta procurada:** todas as pontes do grafo, isto é, arestas cuja remoção separa uma parte da rede.

## Conhecimento prévio e resultado de aprendizagem

Utilizaremos uma **lista de adjacência** para representar o grafo e uma **Busca em Profundidade (DFS)** para percorrer suas componentes. Durante a DFS, serão utilizados os tempos de descoberta dos vértices e os menores tempos alcançáveis para determinar quais arestas são pontes.

**Resultado de aprendizagem aferido:** compreender o conceito de ponte em um grafo não direcionado e utilizar DFS para identificar conexões críticas, analisando os valores de descoberta e retorno de cada vértice.

## Instância pequena e rastreamento preliminar

Considere a seguinte rede:

```text
4
0 (1) 1
1 (3) 0 2 3
2 (2) 1 3
3 (2) 1 2
```

Podemos representá-la como:

```text
0 ── 1
     / \
    2 ─ 3
```

A conexão `0 - 1` é crítica, pois sua remoção deixa o servidor `0` isolado do restante da rede. Já as conexões entre `1`, `2` e `3` não são críticas, pois esses três vértices formam um ciclo e possuem caminhos alternativos entre si.

Durante a DFS, esse comportamento será identificado comparando o tempo de descoberta dos vértices com o menor vértice anteriormente descoberto que suas subárvores conseguem alcançar.
