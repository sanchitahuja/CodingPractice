'''
Construct Target Array With Multiple Sums

Given an array of integers target. From a starting array, A consisting of all 1's, you may perform the following procedure :

    let x be the sum of all elements currently in your array.
    choose index i, such that 0 <= i < target.size and set the value of A at index i to x.
    You may repeat this procedure as many times as needed.

Return True if it is possible to construct the target array from A otherwise return False.
'''
from typing import List
import heapq


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        max_heap = [-i for i in target]
        sum_values = sum(target)
        heapq.heapify(max_heap)

        while -max_heap[0] > 1:
            max_value = -heapq.heappop(max_heap)
            sum_values -= max_value
            if max_value <= sum_values or sum_values < 1:
                return False
            max_value = max_value % sum_values
            sum_values += max_value
            heapq.heappush(max_heap, -max_value)
        return True

print(Solution().isPossible(target=[1,1,1,2]))
