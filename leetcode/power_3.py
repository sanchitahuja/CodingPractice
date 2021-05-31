'''

Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.
'''
import math
import sys


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3433683820292512484657849089281 % n == 0


print(Solution().isPowerOfThree(243))
