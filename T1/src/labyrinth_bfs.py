from algs4.queue import Queue


class LabyrinthBFS:
    """
    BFS adaptado da implementação BreadthFirstPaths da algs4.

    Além de marked e edge_to, mantém dist_to para registrar
    a distância mínima da origem até cada vértice.
    """

    def __init__(self, graph, source):
        self.source = source

        self.marked = [False] * graph.V
        self.edge_to = [-1] * graph.V
        self.dist_to = [-1] * graph.V

        self._bfs(graph, source)

    def _bfs(self, graph, source):
        queue = Queue()

        self.marked[source] = True
        self.dist_to[source] = 0

        queue.enqueue(source)

        while not queue.is_empty():

            vertex = queue.dequeue()

            for neighbor in graph.adj[vertex]:

                if self.marked[neighbor]:
                    continue

                self.marked[neighbor] = True

                self.edge_to[neighbor] = vertex

                self.dist_to[neighbor] = (
                    self.dist_to[vertex] + 1
                )

                queue.enqueue(neighbor)

    def has_path_to(self, vertex):
        """
        Verifica se o vértice foi alcançado pela busca.
        """

        return self.marked[vertex]

    def distance_to(self, vertex):
        """
        Retorna a distância mínima da origem até o vértice.
        """

        return self.dist_to[vertex]

    def path_to(self, vertex):
        """
        Reconstrói o menor caminho da origem até vertex
        utilizando edge_to.
        """

        if not self.has_path_to(vertex):
            return None

        path = []

        current = vertex

        while current != self.source:

            path.append(current)

            current = self.edge_to[current]

        path.append(self.source)

        path.reverse()

        return path