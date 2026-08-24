### GRUPO A: PROBLEMA B (LABIRINTO)
---
- Limites de recursos \
As restrições de recursos são definidas na questão por até 1 segundo de tempo de execução e 512MB de memória.
- Entradas\
As entradas são duas variáveis chamadas n(quantidade de linhas) e m(quantidade de colunas), que deve formar um labirinto retangular que pode ser representado por meio de uma matriz. n e m <= 1000, ou seja podemos ter até 1000000 de células.
- Elementos\
Os elementos possíveis são A(Ponto Inicial), B(Ponto final), #(Parede), .(Esparso por onde é possivel caminhar).

- Saída\
Existe um caminho válido para sair do ponto A até o B ?\
(bool)\
Qual a menor quantidade de passos para percorrer o percusso caso seja possível ?\
(Int)\
Qual a sequência de direções utilizadas para chegar no ponto final com o menor caminho\
(String/Char)

A partir disto é possível verificar que temos um grafo não ponderado já que toda movimentação tem o mesmo peso, e não direcionado ou um grafo simples já que é possível ir e voltar entre os vértices, além de respeitar as regras de grafos simples que é não conter self loops e nem possuir arestas adjascentes. Como estamos lidando com uma matriz nxm também posso presumir uma complexidade assintótica inferior de n eleveado ao quadrado\
---
Vértice: Cada Célula caminhavel\
Aresta: Quando exister a possibilidade de caminhar entre dois vértices
---
É um grafo espaço já que temos uma quantidade máxima de 4 vizinhos
---
Caso não exista solução pode ser desconexo, mas o do exemplo é conexo
---
Grau médio -> Soma de todos os graus / quantidade de vértices\
Número de arestas -> (Vértices * 2)/2
Ordem: Número de arestas
Tamanho: Número de Vertices
Grau Máximo: Maior quantidade de vizinhos
Grau mínimo: Menor quantidade de vizinhos
Grau médio: Média de vizinhos
Densidade: Proporção das arestas existentes\
D = z * qtd de vértices / Arestas * Arestas - 1

