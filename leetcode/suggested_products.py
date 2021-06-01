'''
Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed.
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
'''
from typing import List


class Solution:
    class Node:
        def __init__(self, char: str):
            self.char = char
            self.children = {}
            self.last_char = False

    def create_trie(self, products):
        trie = {}
        for product in products:
            if product[0] not in trie:
                cur = self.Node(product[0])
                trie[product[0]] = cur
            else:
                cur = trie[product[0]]
            for i in range(1, len(product)):
                if not (product[i] in cur.children):
                    child = self.Node(product[i])
                    cur.children[product[i]] = child
                else:
                    child = cur.children[product[i]]
                cur = child
            cur.last_char = True
        return trie

    def print_trie(self, trie, tabs):
        for i, j in trie.items():
            print('\t' * tabs, 'Char', i, 'Last:', j.last_char)
            if j.children:
                self.print_trie(j.children, tabs + 1)

    def get_words(self, cur: Node, final_list: list, cur_str: str):
        cur_str += cur.char
        if cur.last_char:
            final_list.append(cur_str)
        if cur.children:
            for i in cur.children.values():
                self.get_words(i, final_list, cur_str)

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = self.create_trie(products)
        final_list = []
        for i in range(1, len(searchWord) + 1):
            cur_str = (searchWord[:i])
            print('cur_str', cur_str)
            print('searchWord', searchWord)
            cur_list = []
            cur = trie.get(cur_str[0])
            for j in range(1, len(cur_str)):
                if not cur:
                    break
                else:
                    cur = cur.children.get(cur_str[j])
            if cur:
                self.get_words(cur, cur_list, str(cur_str[:-1]))
                print('cur_list', cur_list)
            final_list.append(cur_list)
        print(final_list)


Solution().suggestedProducts(products=["mobile", "mouse", "moneypot", "monitor", "mousepad"], searchWord='mouse')
