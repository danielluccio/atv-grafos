import sys

from labyrinth_graph import LabyrinthGraph
from labyrinth_bfs import LabyrinthBFS
from path_converter import vertices_to_moves


def main():
    input_stream = sys.stdin

    n, m = map(int, input_stream.readline().split())

    grid = [
        input_stream.readline().strip()
        for _ in range(n)
    ]

    labyrinth = LabyrinthGraph(grid)

    bfs = LabyrinthBFS(
        labyrinth.graph,
        labyrinth.start_vertex,
    )

    target = labyrinth.target_vertex

    if not bfs.has_path_to(target):
        print("NO")
        return

    vertex_path = bfs.path_to(target)

    moves = vertices_to_moves(
        vertex_path,
        labyrinth.vertex_to_position,
    )

    print("YES")
    print(bfs.distance_to(target))
    print(moves)


if __name__ == "__main__":
    main()