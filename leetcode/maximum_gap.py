'''
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.
'''
from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        max_diff = 0
        for i in range(1, len(nums)):
            max_diff = max(max_diff, abs(nums[i] - nums[i - 1]))
        return max_diff

    # Using Bucket Sort
    def maximumGapOptimised(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        high, low, curr_high, prev_high, final_ans = max(nums), min(nums), 0, 0, 0
        bucket_size = (high - low) // len(nums) - 1
        buckets = [[] for _ in range(high - low // bucket_size)]
        for i in nums:
            buckets[i - low // bucket_size].append(i)
        for b in buckets:
            if not b:
                continue
            prev_high, cur_low = curr_high, b[0]
            for i in b:
                curr_high, cur_low = max(curr_high, i), min(cur_low, i)
            final_ans = max(final_ans, cur_low - prev_high)
        return final_ans
