import sys
from collections import deque

def main():
    data = sys.stdin.read().split('\n')
    n, m = map(int, data[0].split())
    grade = data[1:1+n]

    for i in range(n):
        for j in range(m):
            if grade[i][j] == 'A':
                inicio = (i, j)
            elif grade[i][j] == 'B':
                fim = (i, j)

    DIRECOES = [('U', -1, 0), ('D', 1, 0), ('L', 0, -1), ('R', 0, 1)]

    visitado = [[False] * m for _ in range(n)]
    veio_de  = [[None] * m for _ in range(n)]

    si, sj = inicio
    visitado[si][sj] = True
    fila = deque([inicio])

    while fila:
        ci, cj = fila.popleft()
        if (ci, cj) == fim:
            break
        for letra, di, dj in DIRECOES:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and not visitado[ni][nj] and grade[ni][nj] != '#':
                visitado[ni][nj] = True
                veio_de[ni][nj] = (ci, cj, letra)
                fila.append((ni, nj))

    if not visitado[fim[0]][fim[1]]:
        print("NO")
        return

    caminho = []
    atual = fim
    while atual != inicio:
        pi, pj, letra = veio_de[atual[0]][atual[1]]
        caminho.append(letra)
        atual = (pi, pj)
    caminho.reverse()

    print("YES")
    print(len(caminho))
    print(''.join(caminho))

main()
