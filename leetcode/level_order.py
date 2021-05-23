'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


'''
from typing import List

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue, cur_queue, final_queue = deque(), [], []
        queue.append(root)
        queue.append(None)
        while queue:
            val = queue.popleft()
            print('val', val)
            if val:
                cur_queue.append(val.val)
                if val.left:
                    queue.append(val.left)
                if val.right:
                    queue.append(val.right)
            else:
                if cur_queue:
                    final_queue.append(cur_queue)
                    queue.append(None)
                cur_queue = []
        return final_queue


r = TreeNode(3)
# r.left = TreeNode(9)
# r.right = TreeNode(20)
# r.right.left = TreeNode(15)
# r.right.right = TreeNode(27)
x = Solution().levelOrder(None)
print('x',x)
for i in x:
    print([j.val if j else None for j in i ])
