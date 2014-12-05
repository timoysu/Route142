from singleton import Singleton
from vertex import Vertex
from edge import Edge

@Singleton
class Graph:
    
    def __init__(self):
        self._vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self._vertices:
            self._vertices[vertex_id] = Vertex()
        else:
            print 'FUCK!'

    def add_edge(self, source_id, destination_id, weight):
        if source_id in self._vertices and destination_id in self._vertices:
            self._vertices[source_id].add_edge(
                self._vertices[destination_id], weight)
        else:
            print 'FUCK!'

g = Graph.get_instance()
g.add_vertex(2)
g.add_vertex(3)
g.add_edge(2,3,5)
