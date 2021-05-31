from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dist = []
        for i in range(len(obstacleGrid)):
            dist.append([0] * len(obstacleGrid[i]))

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1:
                    dist[i][j] = 0
                elif i == 0 and j == 0:
                    dist[0][0] = 1
                else:
                    left = 0 if j - 1 < 0 or obstacleGrid[i][j - 1] == 1 else dist[i][j - 1]
                    above = 0 if i - 1 < 0 or obstacleGrid[i - 1][j] == 1 else dist[i - 1][j]
                    dist[i][j] += left + above

        return dist[-1][-1] if dist[-1][-1] else 0


arr =[[0,1],[0,0]]
for m in arr:
    print(m)

print('##############')
print(Solution().uniquePathsWithObstacles(arr))
