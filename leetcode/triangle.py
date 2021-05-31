from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) <= 0:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                i_val = triangle[i][j]
                prev_val = triangle[i - 1][j] if j < i and i > 0 else float('inf')
                prev_val_1 = triangle[i - 1][j - 1] if j > 0 and i > 0 else float('inf')
                print('i', i, 'j', j, 'i_val', i_val, 'prev_val', prev_val, 'prev_val_1', prev_val_1)
                triangle[i][j] = min([i_val + prev_val, i_val + prev_val_1])
                print('###########')
                for ii in triangle:
                    print(ii)
                print('###########')
        return min(triangle[-1])


# arr = [[-1], [-2, -3]]
# arr = [[-1],[3,2],[1,-2,-1]]
arr = [[-1], [3, 2], [-3, 1, -1]]
print('###########')
for ii in arr:
    print(ii)
print('###########')
Solution().minimumTotal(arr)
