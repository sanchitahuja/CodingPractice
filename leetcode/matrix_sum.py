from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        sum_matrix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            sum_matrix[i][0] = 0
        for i in range(m + 1):
            sum_matrix[0][i] = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                sum_matrix[i][j] = sum_matrix[i - 1][j] + sum_matrix[i][j - 1] + matrix[i - 1][j - 1] - \
                                   sum_matrix[i - 1][j - 1]
        self.sum_matrix = sum_matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        print('row1', row1, 'col1', col1, 'row2', row2, 'col2', col2)
        return self.sum_matrix[row2 + 1][col2 + 1] + self.sum_matrix[row1][col1] - self.sum_matrix[row2 + 1][col1] - \
               self.sum_matrix[row1][col2 + 1]


arr = [[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]], [2, 1, 4, 3],
       [1, 1, 2, 2], [1, 2, 2, 4]]
for i in arr[0]:
    print(i)
print('###########')
n = NumMatrix(arr[0])
for i in n.sum_matrix:
    print(i)
print('###########')

for i in range(1, len(arr)):
    print(n.sumRegion(arr[i][0], arr[i][1], arr[i][2], arr[i][3]))
