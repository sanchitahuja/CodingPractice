from collections import defaultdict
from typing import List


class Solution:
    def find_bridges(self, graph, disc, low, visited, final_ans, curr, parent):
        visited[curr] = True
        disc[curr], low[curr] = self.time, self.time
        self.time += 1
        for v in graph[curr]:
            if not visited[v]:
                parent[v] = curr
                self.find_bridges(graph, disc, low, visited, final_ans, v, parent)
                low[curr] = min(low[curr], low[v])
                if low[v] > disc[curr]:
                    final_ans.append([curr, v])
            elif parent[curr] != v:
                low[curr] = min(low[curr], disc[v])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        self.time = 0
        for c in connections:
            graph[c[0]].append(c[1])
            graph[c[1]].append(c[0])
        visited = [False for _ in connections]
        parent = [-1 for _ in connections]
        disc = [float('inf') for _ in connections]
        low = [float('inf') for _ in connections]
        final_ans = []
        self.find_bridges(graph, disc, low, visited, final_ans, 0, parent)
        return final_ans


ans = Solution().criticalConnections(n=4, connections=[[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]])
print(ans)
