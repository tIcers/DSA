def dfs(graph, current_vertex, target_value, visited=None):
    if not visited:
        visited = []
    visited.append(current_vertex)

    if current_vertex == target_value:
        return visited

    for neighbor in graph[current_vertex]:
        if neighbor not in visited:
            path =  dfs(graph, neighbor, target_value, visited)
            if path:
                return path

