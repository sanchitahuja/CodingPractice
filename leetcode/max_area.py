'''
Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
Given a rectangular cake with height h and width w, and two arrays of integers horizontalCuts and verticalCuts where
horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly,
verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.

Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in
the arrays horizontalCuts and verticalCuts. Since the answer can be a huge number, return this modulo 10^9 + 7.
'''
from typing import List


class Solution:
    MAX = 10 ** 9 + 7

    def maxArea(self, h: int, w: int, horizontal_cuts: List[int], vertical_cuts: List[int]) -> int:
        horizontal_cuts = [0] + sorted(horizontal_cuts) + [h]
        vertical_cuts = [0] + sorted(vertical_cuts) + [w]
        h_diff_max, v_diff_max = 0, 0
        for i in range(1, len(horizontal_cuts)):
            h_diff_max = max(h_diff_max, horizontal_cuts[i] - horizontal_cuts[i - 1])
        for i in range(1, len(vertical_cuts)):
            v_diff_max = max(v_diff_max, vertical_cuts[i] - vertical_cuts[i - 1])
        print(h_diff_max, v_diff_max)
        return (h_diff_max * v_diff_max) % self.MAX


print(Solution().maxArea(h=5, w=4, horizontal_cuts=[3, 1], vertical_cuts=[1]))
print(Solution().maxArea(h=5, w=4, horizontal_cuts=[1, 2, 4], vertical_cuts=[1, 3]))
