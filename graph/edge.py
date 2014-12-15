class Edge(object):

    def __init__(self, id, source_vertex, destination_vertex, weight):
        self.source = source_vertex
        self.destination = destination_vertex
        self.weight = weight