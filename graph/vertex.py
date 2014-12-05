from edge import Edge

class Vertex:

    def __init__(self):
        self._edges = []

    def add_edge(self, destination_vertex, weight):
        edge = Edge(self, destination_vertex, weight)
        self._edges.append(edge)