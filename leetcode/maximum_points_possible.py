'''
Maximum Points You Can Obtain from Cards
There are several cards arranged in a row, and each card has an associated number of points The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

'''
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        pre_sum = cardPoints.copy()
        post_sum = cardPoints.copy()
        for i in range(1, n):
            pre_sum[i] += pre_sum[i - 1]
        for i in range(n - 2, -1, -1):
            post_sum[i] += post_sum[i + 1]

        if k >= n:
            return pre_sum[-1]
        elif k == 0:
            return 0
        else:
            i = k - 1
            j = n - 1

            max_sum = pre_sum[i]
            i -= 1
            while i >= 0:
                if pre_sum[i] + post_sum[j] > max_sum:
                    max_sum = pre_sum[i] + post_sum[j]
                i -= 1
                j -= 1
            if post_sum[j] > max_sum:
                max_sum = post_sum[j]

            return max_sum


print(Solution().maxScore(cardPoints=[100, 40, 17, 9, 73, 75], k=3))
