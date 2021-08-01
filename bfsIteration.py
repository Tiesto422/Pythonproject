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
queue = collections.deque()


def bfs(v, q, node):
    v.append(node)
    q.append(node)

    while q:
        s = q.popleft()
        print(s)
        for neighbor in graph[s]:
            if neighbor not in v:
                v.append(neighbor)
                q.append(neighbor)


bfs(visited, queue, 'A')
