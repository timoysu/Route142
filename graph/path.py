class Path(object):

    def __init__(self, source_vertex, destination_vertex):
        self.source = source_vertex
        self.destination = destination_vertex
        self.path = [source_vertex]
        self.total_weight = float('inf')
        if source_vertex.has_edge(destination_vertex):
            edge = source_vertex.get_edge(destination_vertex)
            self.path.append(edge)
            self.path.append(destination_vertex)
            self.total_weight = edge.weight
        if source_vertex is destination_vertex:
            self.total_weight = 0

    def __repr__(self):
        return str(self.source.id) + ' ' + str(self.destination.id) + ' ' + str(
            self.total_weight)

    def merge_path(self, path):
        pass
