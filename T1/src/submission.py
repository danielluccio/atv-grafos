import sys
from collections import deque


def main():
    input_stream = sys.stdin.buffer

    n, m = map(int, input_stream.readline().split())

    grid = [
        input_stream.readline().strip()
        for _ in range(n)
    ]

    start = -1
    target = -1

    for row_index, row in enumerate(grid):

        start_column = row.find(b"A")

        if start_column != -1:
            start = row_index * m + start_column

        target_column = row.find(b"B")

        if target_column != -1:
            target = row_index * m + target_column

    # 0 = não visitado
    # 1 = chegou aqui usando L
    # 2 = chegou aqui usando R
    # 3 = chegou aqui usando U
    # 4 = chegou aqui usando D
    # 255 = posição inicial
    parent = bytearray(n * m)

    queue = deque([start])

    parent[start] = 255

    found = False

    while queue:

        current = queue.popleft()

        if current == target:
            found = True
            break

        row, column = divmod(current, m)

        # Esquerda
        if column > 0:

            neighbor = current - 1

            if (
                parent[neighbor] == 0
                and grid[row][column - 1] != ord("#")
            ):
                parent[neighbor] = 1
                queue.append(neighbor)

        # Direita
        if column + 1 < m:

            neighbor = current + 1

            if (
                parent[neighbor] == 0
                and grid[row][column + 1] != ord("#")
            ):
                parent[neighbor] = 2
                queue.append(neighbor)

        # Cima
        if row > 0:

            neighbor = current - m

            if (
                parent[neighbor] == 0
                and grid[row - 1][column] != ord("#")
            ):
                parent[neighbor] = 3
                queue.append(neighbor)

        # Baixo
        if row + 1 < n:

            neighbor = current + m

            if (
                parent[neighbor] == 0
                and grid[row + 1][column] != ord("#")
            ):
                parent[neighbor] = 4
                queue.append(neighbor)

    if not found:
        print("NO")
        return

    path = bytearray()

    current = target

    while current != start:

        movement = parent[current]

        if movement == 1:
            path.append(ord("L"))
            current += 1

        elif movement == 2:
            path.append(ord("R"))
            current -= 1

        elif movement == 3:
            path.append(ord("U"))
            current += m

        elif movement == 4:
            path.append(ord("D"))
            current -= m

    path.reverse()

    print("YES")
    print(len(path))
    print(path.decode())


if __name__ == "__main__":
    main()