time = 0

from collections import defaultdict


def articulation_points(graph, visited, disc, low, parent, u, points):
    global time
    visited[u] = True
    children = 0
    disc[u], low[u] = time, time
    time += 1

    for v in graph[u]:
        if not visited[v]:
            parent[v] = u
            children += 1
            articulation_points(graph, visited, disc, low, parent, v, points)
            low[u] = min(low[u], low[v])
            if parent[u] == -1 and children >= 2:
                points.append(u)
            if parent[u] != -1 and low[v] >= disc[u]:
                points.append(u)
        elif parent[u] != v:
            low[u] = min(low[u], disc[v])


def main(connections, n):
    global time
    disc = [float('inf') for _ in range(n)]
    low = [float('inf') for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    time = 0
    graph = defaultdict(list)
    for c in connections:
        graph[c[0]].append(c[1])
        graph[c[1]].append(c[0])
    points = []
    articulation_points(graph, visited, disc, low, parent, 0, points)
    return points


ans = main(n=6, connections=[(1, 0),
                             (0, 2),
                             (2, 1),
                             (0, 3),
                             (3, 4), ])
print(ans)
