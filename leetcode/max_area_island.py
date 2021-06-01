from typing import List


class Solution:
    def get_count(self, row: int, col: int, arr: List[List[int]], count: List[int]):
        if arr[row][col] == 0 or arr[row][col] == -1:
            return
        count[0] += 1
        arr[row][col] = -1
        if row + 1 < len(arr):
            self.get_count(row + 1, col, arr, count)
        if col + 1 < len(arr[row]):
            self.get_count(row, col + 1, arr, count)
        if col - 1 >= 0:
            self.get_count(row, col - 1, arr, count)
        if row - 1 >= 0:
            self.get_count(row - 1, col, arr, count)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count, max_count = [0], 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                self.get_count(i, j, grid, count)
                max_count = max(max_count, count[0])
                count[0] = 0
        return max_count


print(Solution().maxAreaOfIsland(grid=[[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                       [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                                       [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
