# Marco 2 — Representação computacional

**Problema:** B — CSES 1193, *Labyrinth*
**Continuação de:** `acompanhamento/marco-1.md`

## 1. Escolha da representação

O Labirinto é um **grafo esparso**: cada célula tem no máximo 4 vizinhos possíveis (cima,
baixo, esquerda, direita), então o número de arestas cresce apenas linearmente com o
número de células (na instância pequena, `|E| = 14` é praticamente igual a `|V| = 14`) —
nunca chega perto do máximo teórico de `|V|²` arestas que um grafo qualquer poderia ter.
É esse fato que orienta a escolha de representação a seguir.

Existem três formas clássicas de representar um grafo na memória: **matriz de
adjacência**, **lista de adjacência** e **representação implícita**. Para o Labirinto, a
escolha foi a representação **implícita**, pelos seguintes motivos:

| Representação        | Por que **não** serve aqui                                                                 |
|------------------------|---------------------------------------------------------------------------------------------|
| Matriz de adjacência   | Precisaria de uma tabela `|V| × |V|`. Com até 10⁶ células, seriam ~10¹² posições — inviável. |
| Lista de adjacência    | Exigiria montar, para cada uma das até 10⁶ células, uma lista de vizinhos — trabalho e memória desperdiçados à toa. |
| **Implícita (escolhida)** | Os vizinhos de qualquer célula `(i,j)` são triviais de calcular na hora: `(i±1,j)` e `(i,j±1)`, filtrando o que está fora da grade ou é parede. Nada precisa ser pré-calculado. |

A própria matriz de caracteres lida da entrada (`.`, `#`, `A`, `B`) já **é** o grafo — não
existe uma etapa separada de "montar arestas".

## 2. Leitura da entrada e construção do grafo

```python
data = sys.stdin.read().split('\n')
n, m = map(int, data[0].split())
grade = data[1:1+n]        # o grafo "é" essa lista de strings

for i in range(n):
    for j in range(m):
        if grade[i][j] == 'A':
            inicio = (i, j)
        elif grade[i][j] == 'B':
            fim = (i, j)
```

Não há uma função `construir_grafo()` separada: ler a entrada **é** construir a
representação, porque ela é implícita. Os "vizinhos" só são calculados quando o algoritmo
de busca (Marco 3/4) realmente precisa deles, dentro do laço de exploração:

```python
DIRECOES = [('U', -1, 0), ('D', 1, 0), ('L', 0, -1), ('R', 0, 1)]
for letra, di, dj in DIRECOES:
    ni, nj = ci + di, cj + dj
    if 0 <= ni < n and 0 <= nj < m and grade[ni][nj] != '#':
        ...  # (ci,cj) e (ni,nj) são vizinhos — a aresta "existe" neste instante
```

## 3. Medidas estruturais (instância pequena)

Calculadas sobre a instância oficial 5×8 do Marco 1:

```
5 8
########
#.A#...#
#.##.#B#
#......#
########
```

| Medida                          | Valor |
|----------------------------------|-------|
| Vértices, \|V\|                  | 14    |
| Arestas, \|E\|                   | 14    |
| Grau mínimo                      | 1 (célula `A`)  |
| Grau máximo                      | 3 (célula (linha 4, coluna 5), onde o corredor de baixo se ramifica para cima) |
| Grau médio (2·\|E\| / \|V\|)      | 2,0   |
| Densidade (2·\|E\| / (\|V\|·(\|V\|−1))) | ≈ 0,154 (15,4%) |
| Componentes conexas              | 1 (grafo conexo — todo nó alcança todo nó) |
| Grau de `A`                      | 1 — só existe uma saída (para a esquerda) |
| Grau de `B`                      | 2 — passagem, não é beco sem saída |

**Observação estrutural:** como o grafo é conexo e `|V| = |E| = 14`, ele contém
**exatamente um ciclo** (em um grafo simples conexo, número de arestas = número de
vértices − 1 + número de ciclos independentes). Esse ciclo é visível na figura do grafo
que já geramos: é o laço de 8 arestas que contorna o segundo bloco de parede, formado
pelas células (linha 2, colunas 5–7) e (linha 4, colunas 5–7) ligadas pelas colunas 5 e 7.

Tabela completa de grau por célula (linha, coluna — 0-indexado):

| Célula | Rótulo | Grau |
|--------|--------|------|
| (1,1) | . | 2 |
| (1,2) | A | 1 |
| (1,4) | . | 2 |
| (1,5) | . | 2 |
| (1,6) | . | 2 |
| (2,1) | . | 2 |
| (2,4) | . | 2 |
| (2,6) | B | 2 |
| (3,1) | . | 2 |
| (3,2) | . | 2 |
| (3,3) | . | 2 |
| (3,4) | . | 3 |
| (3,5) | . | 2 |
| (3,6) | . | 2 |

## 4. Validação com a instância pequena

Contagem manual, direto na grade:

- **Vértices:** conte todo caractere que não é `#` → linha 2 tem 5 (`.A...`), linha 3 tem
  3 (`.` `.` `B`), linha 4 tem 6 (`......`) → 5 + 3 + 6 = **14**, bate com a tabela acima.
- **Arestas:** conte todo par de vizinhos livres (horizontal e vertical), sem contar duas
  vezes → 3 na linha 2, 5 na linha 3, 6 ligando as linhas verticalmente → 3 + 5 + 6 =
  **14**, também bate.
- **Grau de A:** olhando a célula `A`, só a vizinha da esquerda é livre (`.`); acima,
  abaixo e à direita são paredes (`#`) → grau **1**, confirmado.

Essa contagem manual bate com os valores calculados, o que valida que a representação
implícita (a grade lida como está) contém exatamente a mesma informação estrutural que um
grafo montado explicitamente teria — só que sem gastar memória para isso.
