'''

Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.
'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1) + 1
        m = len(word2) + 1
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                else:
                    if word1[i - 1] == word2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        for i in dp:
            print(i)
        return n + m - 2 * dp[-1][-1] - 2


print(Solution().minDistance("leetcode", "etco"))
