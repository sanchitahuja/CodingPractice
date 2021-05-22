import bisect
from typing import *


class Solution:
    def find_left_most_value(self, arr, x):
        i = bisect.bisect_left(arr, x)
        if i < len(arr) and i != -1 and arr[i] == x:
            return i
        else:
            return -1

    def find_right_most_value(self, arr, x):
        i = bisect.bisect_right(arr, x)
        if len(arr) + 1 > i > 0 and arr[i - 1] == x:
            return i - 1
        else:
            return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.find_left_most_value(nums, target), self.find_right_most_value(nums, target)]
