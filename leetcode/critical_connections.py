from collections import defaultdict
from typing import List


class Solution:
    def dfs(self, visited, graph, curr):
        if visited[curr]:
            return

        visited[curr] = True
        for i in graph[curr]:
            self.dfs(visited, graph, i)

    def is_connected(self, graph):
        visited = [False for _ in range(len(graph))]
        self.dfs(visited, graph, 0)
        return False in visited

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(set)
        final_ans = []
        for c in connections:
            graph[c[0]].add(c[1])
            graph[c[1]].add(c[0])

        for c in connections:
            graph[c[0]].remove(c[1])
            graph[c[1]].remove(c[0])
            connected_graph = self.is_connected(graph)
            if connected_graph:
                final_ans.append(c)
            graph[c[0]].add(c[1])
            graph[c[1]].add(c[0])
        return final_ans


ans = Solution().criticalConnections(n=4, connections=[[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]])
print(ans)
