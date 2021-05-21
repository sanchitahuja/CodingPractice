'''
Jump Game II
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.


'''
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(1, n):
            j = i - 1
            min_val = 100001
            while j >= 0:
                if nums[j] >= i - j:
                    min_val = min(min_val, dp[j])
                j -= 1
            dp[i] = min_val + 1
        print('dp', dp)
        return dp[-1]


print(Solution().jump(nums=[2,3,0,1,4]))