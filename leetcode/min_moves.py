'''
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.



Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

Example 2:

Input: nums = [1,10,2,9]
Output: 16

'''
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums, n = sorted(nums), len(nums)
        final_sum, median = 0, nums[n // 2]
        for i in nums:
            final_sum += abs(i - median)
        if n % 2 == 0:
            new_sum, median = 0, nums[n // 2 - 1]
            for i in nums:
                new_sum += abs(i - median)
            final_sum = min(final_sum, new_sum)

        return final_sum


print(Solution().minMoves2([1, 10, 2, 9]))
