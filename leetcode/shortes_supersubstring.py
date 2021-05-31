from typing import List

from itertools import permutations
class Solution:
    def all_perms(self, elements):
        if len(elements) <= 1:
            yield elements
        else:
            for perm in self.all_perms(elements[1:]):
                for i in range(len(elements)):
                    yield perm[:i] + elements[0:1] + perm[i:]

    def merge_string(self, s1: str, s2: str):
        for i in range(max(len(s1) - len(s2), 0), len(s1)):
            if len(s1) >= i and s1[i:] == s2[:len(s1) - i]:
                return s1 + s2[len(s1) - i:]
        return s1 + s2

    def shortestSuperstring2(self, words: List[str]) -> str:
        n = len(words)
        final_word, max_len = '', 1000
        for i in self.all_perms([x for x in range(n)]):
            final_str = words[i[0]]
            for j in range(1, len(i)):
                final_str = self.merge_string(final_str, words[i[j]])

            # print('i', i, 'len(final_str)', len(final_str))
            if len(final_str) < max_len:
                max_len = len(final_str)
                final_word = final_str

        return final_word

    def find_str_length(self, str1: str, str2: str):
        max_length = 0
        final_string = ''
        for i in range(1, min(len(str1), len(str2))):
            if str1[len(str1) - i:] == str2[:i]:
                if i > max_length:
                    max_length = i
                    final_string = str1 + str2[max_length:]

        for i in range(1, min(len(str1), len(str2))):
            if str2[len(str1) - i:] == str1[:i]:
                if i > max_length:
                    max_length = i
                    final_string = str2 + str1[max_length:]
        if final_string == '':
            final_string = str1 + str2

        return max_length, final_string
    def find_length(self, str1: str, str2: str):
        max_length = 0
        final_string = ''
        for i in range(1, min(len(str1), len(str2))):
            if str1[len(str1) - i:] == str2[:i]:
                if i > max_length:
                    max_length = i
                    final_string = str1 + str2[max_length:]
        return final_string if final_string else str1+str2

    def shortestSuperstringPermutation(self, words: List[str]) -> str:
        min_len = 10000
        final_str = ''
        for p in permutations(words):
            curr_str = ''
            for i in p:
                if curr_str == '':
                    curr_str = i
                else:
                    curr_str = self.find_length(curr_str,i)
            if len(curr_str)< min_len:
                final_str = curr_str
                min_len = len(curr_str)
        return final_str







    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        print(words)
        while n > 1:

            max_length, word_i, word_j, max_str = 0, -1, -1, ''
            for i in range(n):
                for j in range(i+1, n):
                    l, curr_str = self.find_str_length(words[i], words[j])

                    if l >= max_length:
                        max_length = l
                        max_str = curr_str
                        word_i = i
                        word_j = j

            words[word_i], words[0] = words[0],max_str
            words[word_j], words[n-1] = words[n-1], words[word_j]
            n -= 1
            print(words)
        return words[0]

    def merge(self, str1, str2):
        max_length = 0
        final_string = ''

        for i in range(1, min(len(str1), len(str2))):
            if str1[len(str1) - i:] == str2[:i]:
                if i > max_length:
                    max_length = i
                    final_string = str1 + str2[max_length:]

        for i in range(1, min(len(str1), len(str2))):
            if str2[len(str1) - i:] == str1[:i]:
                if i > max_length:
                    max_length = i
                    final_string = str2 + str1[max_length:]
        if final_string == '':
            final_string = str1 + str2
        return final_string if final_string else str1 + str2

    def shortestSuperstring2(self, words:List[str]):
        words = set(words)
        while len(words)>1:
            n = len(words)
            print(words)
            max_len = -1
            m_str, ii,jj='',0,0
            for i in range(n):
                for j in range(i+1, n):
                    merged_str = self.merge(words[i],words[j])
                    saved =(len(words[i])+len(words[j])) -  len(merged_str)
                    if  saved > max_len:
                        print(merged_str)
                        max_len = saved
                        m_str = merged_str
                        ii = i
                        jj = j
            words.add(m_str)
            words[jj] = words[n-1]
            n-=1
        return words[0]



# print(Solution().shortestSuperstring(words=["lasfmcoivpslmsv","jycxxeokajpfcgmhe","uqpflmkjycxxeoka","jpfcgmhebxqqoftauke","xqflasfmcoivpslm","qqoftauketrwooc","xeokajpfcgmhebxqqof","kajpfcgmhebxqqoftauk"]))
print(Solution().shortestSuperstring2(words = ["catg","ctaagt","gcta","ttca","atgcatc"]))
