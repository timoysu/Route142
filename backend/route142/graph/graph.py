from singleton import Singleton
from vertex import Vertex
from edge import Edge
from path import Path

@Singleton
class Graph(object):

    def __init__(self):
        self._M = {}
        self._vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self._vertices:
            self._vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, id, source_id, destination_id, weight, two_way=False):
        if source_id in self._vertices and destination_id in self._vertices:
            self._vertices[source_id].add_edge(
                id, self._vertices[destination_id], weight)
            if two_way:
                self._vertices[destination_id].add_edge(
                    id, self._vertices[source_id], weight)

    def initialize_matrix(self):
        self._M = {}
        for i in self._vertices:
            self._M[i] = {}
            for j in self._vertices:
                self._M[i][j] = Path(self._vertices[i], self._vertices[j])

    def floyd_algorithm(self):
        for i in self._vertices:
            for j in self._vertices:
                for k in self._vertices:
                    if i != j:
                        a = self._M[j][k].total_weight
                        b = self._M[j][i].total_weight + self._M[i][k].total_weight
                        if a > b:
                            c = self._M[j][i].merge_path(self._M[i][k])
                            self._M[j][k] = c

    def get_path(self, source_id, destination_id):
        return self._M[source_id][destination_id]

