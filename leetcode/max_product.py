'''
Maximum Product of Word Lengths
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

'''
from typing import List

from bitarray import bitarray


class Solution:
    def set_bit(self, value, bit):
        return value | (1 << bit)

    def clear_bit(self, value, bit):
        return value & ~(1 << bit)

    def maxProduct(self, words: List[str]) -> int:
        list_vals = []
        for word in words:
            val = 0
            for w in word:
                val = self.set_bit(val, ord(w))
            list_vals.append(val)
        max_element = 0
        for i in range(len(list_vals)):
            for j in range(i + 1, len(list_vals)):
                if list_vals[i] & list_vals[j] == 0:
                    print(words[i], words[j])
                    max_element = max(max_element, len(words[i]) * len(words[j]))
        return max_element


# print(Solution().maxProduct(words=["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))
print(Solution().maxProduct(words=["a","aa","aaa","aaaa"]))

