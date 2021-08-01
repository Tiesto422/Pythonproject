import collections
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
visited = []


def dfs(v, node):
    v.append(node)
    print(node)
    for neighbor in graph[node]:
        if neighbor not in v:
            dfs(v, neighbor)


dfs(visited, 'A')
