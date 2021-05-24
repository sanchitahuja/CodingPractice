from typing import List


class Solution:
    def max_count(self, index, word, length):
        # print('index', index, 'word', word)
        if index == 0:
            return 0
        count = 0
        if word in length[index]:
            for i in range(len(word)):
                x = word[:i] + word[i + 1:]
                count = max(count, length[index - 1][x] if x in length[index - 1] else 0)
            count += 1

        return count

    def longestStrChain(self, words: List[str]) -> int:
        max_length = 0
        for i in words:
            max_length = max(max_length, len(i))

        length = [dict() for _ in range((max_length + 1))]
        for i in words:
            if len(i) == 1:
                length[len(i)][i] = 1
            elif len(i) == 0:
                length[len(i)][i] = 0
            else:
                length[len(i)][i] = None

        count = 0
        for l in range(2, len(length)):
            for i in length[l]:
                length[l][i] = self.max_count(l, i, length)
                count = max(count, length[l][i])

        return count


print(Solution().longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))
