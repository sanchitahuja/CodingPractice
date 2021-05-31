
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

from collections import deque
from typing import List

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        stack = deque()
        stack.appendleft(root)

        while len(stack) > 0:
            curr = stack.popleft()
            l = len(curr.children)
            for c in range(l-1, -1, -1):
                stack.appendleft(curr.children[c])

            ans.append(curr.val)
        return ans


