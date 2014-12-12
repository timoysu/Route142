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
        else:
            print 'FUCK!'

    def add_edge(self, id, source_id, destination_id, weight, two_way=False):
        if source_id in self._vertices and destination_id in self._vertices:
            self._vertices[source_id].add_edge(
                id, self._vertices[destination_id], weight)
            if two_way:
                self._vertices[destination_id].add_edge(
                    id, self._vertices[source_id], weight)
        else:
            print 'FUCK!'

    def initialize_matrix(self):
        self._M = {}
        for i in self._vertices:
            self._M[i] = {}
            for j in self._vertices:
                self._M[i][j] = Path(self._vertices[i], self._vertices[j])

        print self._M


g = Graph.get_instance()
g.add_vertex(2)
g.add_vertex(3)
g.add_edge(1,2,3,5)
g.initialize_matrix()
