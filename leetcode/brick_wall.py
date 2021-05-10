from collections import defaultdict
from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        d = defaultdict(set)
        n = len(wall)
        l = []
        if n == 1:
            if len(wall[0]) == 1:
                return 1
            else:
                return 0
        for i in range(n):
            for j in range(1, len(wall[i])):
                wall[i][j] += wall[i][j - 1]
        for i in range(n):
            for j in range(len(wall[i])):
                d[i].add(wall[i][j])
                l.append(wall[i][j])

        max_width = wall[0][-1]
        min_count = n
        for w in wall:
            print(w)

        print('d', d)
        for i in l:
            if i < max_width:
                curr_count = 0
                for j, j_val in d.items():
                    if i in j_val:
                        continue
                    else:
                        curr_count += 1

                print('i', i, 'curr_count', curr_count)
                if min_count != 0 and curr_count < min_count:
                    min_count = curr_count

        return min_count


arr = [[1, 2, 2, 1],
       [3, 1, 2],
       [1, 3, 2],
       [2, 4],
       [3, 1, 2],
       [1, 3, 1, 1]]
# arr = [[1], [1], [1]]
# arr = [[79, 12, 208, 1]]
print(Solution().leastBricks(arr))
