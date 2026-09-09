from algs4.graph import Graph


class LabyrinthGraph:

    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

        self.position_to_vertex = {}
        self.vertex_to_position = []

        self.start_vertex = None
        self.target_vertex = None

        self._index_vertices()

        self.graph = Graph(len(self.vertex_to_position))

        self._build_edges()

    def _index_vertices(self):

        for i in range(self.rows):
            for j in range(self.cols):

                if self.grid[i][j] == "#":
                    continue

                vertex = len(self.vertex_to_position)

                self.position_to_vertex[(i, j)] = vertex
                self.vertex_to_position.append((i, j))

                if self.grid[i][j] == "A":
                    self.start_vertex = vertex

                elif self.grid[i][j] == "B":
                    self.target_vertex = vertex

        if self.start_vertex is None:
            raise ValueError("Vértice inicial A não encontrado.")

        if self.target_vertex is None:
            raise ValueError("Vértice destino B não encontrado.")

    def _build_edges(self):

        directions = [
            (0, 1),   # direita
            (1, 0),   # baixo
        ]

        for (i, j), vertex in self.position_to_vertex.items():

            for di, dj in directions:

                neighbor_position = (i + di, j + dj)

                if neighbor_position not in self.position_to_vertex:
                    continue

                neighbor_vertex = self.position_to_vertex[neighbor_position]

                self.graph.add_edge(vertex, neighbor_vertex)

    def position_of(self, vertex):
        """
        Retorna a posição (i, j) correspondente a um vértice.
        """

        return self.vertex_to_position[vertex]