MARCO 1 - AV2
-> Entendimento sobre o problema , a apresentação será feita em sala de aula hoje mesmo.
-> Estamos com o PROBLEMA D (Links Críticos)


Temos um grafo não direcionado, e simples dado que não possui arestas paralelas e nem loops
onde o objetivo é encontrar todos as pontes (ou seja arestas ao qual, caso sejam removidas desconecta o 
grafo e aumenta a quantidade de componentes conexos) do exemplo
para resolver este problema, é utilizado uma variação da busca em profundidade (DFS) chamada de Algoritmo de Tarjan
para conseguir a resolução do problema em O(V + E), ou seja Linear


RESUMIR ENTRADA SAÍDA E RESTRIÇÕES
Receber um dataset do tipo texto, na primeira linha recebe um número inteiro com a quantidade de nós.
Se o valor for 0, significa que a rede está vazia, ou o arquivo acabou. As próximas n linhas descrevem as relações entre os
nós e seus vizinhos diretos
EXAMPLE:
1 -> Nó ao qual será setado a quantidade de vizinho entre parênteses e os nós vizinhos propriamente ditos.
A entrada não vem ordem, ou seja as relações do vértice 7 podem vir antes do 4 e tudo em
O programa entende que a entrada é N - 1 , ou seja como a entrada 8 os ids acessados serão de 0 até 7


-----------------------------------------------------------------------------------------------------------
A saída exige que a primeira linha exiba a quantidade de pontes que ele chama de critical links seguido da string Critical Links
Logo abaixo é exibido os links críticos passando o servidor predecessor e servidor sucessor
Sempre printar com uma linha em branco no final

