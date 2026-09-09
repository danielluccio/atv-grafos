def vertices_to_moves(path, vertex_to_position):
    """
    Converte um caminho formado por vértices para
    uma sequência L, R, U e D.
    """

    moves = []

    movement_by_difference = {
        (0, -1): "L",
        (0, 1): "R",
        (-1, 0): "U",
        (1, 0): "D",
    }

    for current, next_vertex in zip(path, path[1:]):

        current_i, current_j = vertex_to_position[current]

        next_i, next_j = vertex_to_position[next_vertex]

        difference = (
            next_i - current_i,
            next_j - current_j,
        )

        move = movement_by_difference[difference]

        moves.append(move)

    return "".join(moves)