from vertex import Vertex

class Graph:
    def __init__(self, directed=False ) -> None:
        self.graph_dict = {}
        self.directed = directed

    def add_vertex(self, vertex):
        print("Adding " + vertex.value)
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex):
        print(f"Adding edge from {from_vertex.value} to {to_vertex.value}")
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value)
