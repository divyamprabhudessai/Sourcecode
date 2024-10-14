def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    # Mark the current node as visited
    visited.add(node)
    print(node, end=" ")

    # Recur for all the adjacent nodes not visited yet
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Perform DFS starting from node 'A'
dfs(graph, 'A')
