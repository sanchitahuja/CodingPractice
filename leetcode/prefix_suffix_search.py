'''

Design a special dictionary which has some words and allows you to search the words in it by a prefix and a suffix.

Implement the WordFilter class:

    WordFilter(string[] words) Initializes the object with the words in the dictionary.
    f(string prefix, string suffix) Returns the index of the word in the dictionary which has the prefix prefix and the suffix suffix. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.


'''
from collections import defaultdict
from typing import List


class WordFilter:

    def __init__(self, words: List[str]):
        self.d = defaultdict(list)
        for index, w in enumerate(words):
            for i in range(1, min(10, len(w)) + 1):
                prefix = w[:i]
                for j in range(1, min(10, len(w)) + 1):
                    suffix = w[-j:]
                    self.d[(prefix, suffix)].append((index, len(w)))

    def f(self, prefix: str, suffix: str) -> int:
        if (prefix, suffix) in self.d:
            l = self.d[(prefix, suffix)]
            max_length = 0
            index = -1
            for i in l:
                if i[1] > max_length or (i[1] == max_length and i[0] > index):
                    max_length = i[1]
                    index = i[0]
            return index

        else:
            return -1
# ["WordFilter","f","f","f","f","f","f","f","f","f","f"]
x = ["bccbacbcba","a"],["ab","abcaccbcaa"],["a","aa"],["cabaaba","abaaaa"],["cacc","accbbcbab"],["ccbcab","bac"],["bac","cba"],["ac","accabaccaa"],["bcbb","aa"],["ccbca","cbcababac"]

obj = WordFilter(words=["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"])
print(obj.f(prefix='a', suffix='aa'))
print(obj.d[('a','aa')])
