'''

You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

    If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
    If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.

Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.



'''
import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        heap_sum = 0
        cur_sum = 0
        n = len(heights)
        i = 1
        while i < n:
            diff = heights[i] - heights[i - 1]
            if diff <= 0:
                pass
            else:
                cur_sum += diff
                if ladders <= 0:
                    pass
                elif len(heap) >= ladders:
                    min_element = heap[0]
                    if diff > min_element:
                        min_element = heapq.heappop(heap)
                        heapq.heappush(heap, diff)
                        heap_sum -= min_element
                        heap_sum += diff

                else:
                    heap_sum += diff
                    heapq.heappush(heap,diff)

                if cur_sum - heap_sum > bricks:
                    return i - 1
            i += 1
        return i - 1
'''
heights = [14,3,19,3]
bricks = 17
ladders = 0
'''


heights = [4,12,2,7,3,18,20,3,19]
bricks = 1
ladders = 0

print(Solution().furthestBuilding(heights=heights, bricks=bricks, ladders=ladders))