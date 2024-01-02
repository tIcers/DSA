from vertex import Vertex

class Graph:
    def __init__(self, directed=False ) -> None:
        self.graph_dict = {}
        self.directed = directed

    def add_vertex(self, vertex):
        print("Adding " + vertex.value)
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        print(f"Adding edge from {from_vertex.value} to {to_vertex.value}")
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)
    
    def find_path(self, start_vertex, end_vertex):
        print(f"I am searching from {start_vertex} to {end_vertex}")
        start = self.graph_dict[start_vertex]
        seen = {}
        while start:
            current_vertex = start.pop(0)
            seen[current_vertex] = True
            if current_vertex == end_vertex: 
                return True
            else: 
                vertex = self.graph_dict[current_vertex]
                next_vertices = vertex.get_edges()
                next_vertices = [vertex for vertex in next_vertices if vertex not in seen]
                start.extend(next_vertices)

        return False


