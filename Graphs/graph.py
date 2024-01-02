from vertex import Vertex

class Graph:
    def __init__(self, directed=False ) -> None:
        self.graph_dict = {}
        self.directed = directed

    def add_vertex(self, vertex):
        print("Adding " + vertex.value)
        self.graph_dict[vertex.value] = vertex
