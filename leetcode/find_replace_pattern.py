'''
Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.
'''
from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        final_list = []
        for word in words:
            visited, mapping, i = {}, {}, 0
            while i < len(word):
                pattern_in_mapping = pattern[i] in mapping
                if (pattern_in_mapping and mapping[pattern[i]] != word[i]) or (
                        not pattern_in_mapping and word[i] in visited):
                    break
                else:
                    mapping[pattern[i]], visited[word[i]] = word[i], True
                i += 1
            if i == len(word):
                print('visited',visited)
                print('mapping',mapping)
                final_list.append(word)
        return final_list


print(Solution().findAndReplacePattern(words=["abc", "deq", "mee", "aqq", "dkd", "ccc"], pattern="abb"))
print(Solution().findAndReplacePattern(words=["a","b","c"], pattern="a"))
