from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                count += 1

            if count > 1 or (i + 1 < len(nums) and nums[i - 1] < nums[i + 1]) or (i - 1 > 0 and nums[i] < nums[i - 2]):
                return False
        return True


print(Solution().checkPossibility(nums=[3, 4, 2, 3]))
