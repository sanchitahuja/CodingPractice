'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
'''
from typing import List


class Solution:
    def is_valid(self, matrix, i: int, j: int):
        # Check row
        for idx in range(j - 1, -1, -1):
            if matrix[i][idx] == 'Q':
                return False
        # CHeck Upper diagonal
        row, col = i - 1, j - 1
        while row >= 0 and col >= 0:
            if matrix[row][col] == 'Q':
                return False
            row, col = row - 1, col - 1
        # Check lower diagonal
        row, col = i + 1, j - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == 'Q':
                return False
            row, col = row + 1, col - 1
        return True

    def queen_util(self, matrix: List[List[str]], col: int, n: int, final_list: List):
        if col == n:
            final_list.append([''.join(i) for i in matrix])
        else:
            for row in range(n):
                matrix[row][col] = 'Q'
                if self.is_valid(matrix, i=row, j=col):
                    self.queen_util(matrix, col + 1, n, final_list)
                matrix[row][col] = '.'

    def solveNQueens(self, n: int) -> List[List[str]]:
        matrix, final_list = [['.' for _ in range(n)] for _ in range(n)], []
        self.queen_util(matrix, 0, n, final_list)
        return final_list


x = Solution().solveNQueens(4)
for m in x:
    print(m)
