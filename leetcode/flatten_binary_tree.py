# Definition for a binary tree node.
from typing import Union


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def to_list(self, root: TreeNode) -> Union[TreeNode, None]:
        if root is None:
            return None
        elif root.left is None and root.right is None:
            return root
        else:
            left = self.to_list(root.left)
            right = self.to_list(root.right)
            print('Root', root.val)
            print('left', left.val if left else None)
            print('right', right.val if right else None)
            if left:
                cur = left
                while cur.right is not None:
                    cur = cur.right
                cur.right = right
                root.right = left
                root.left = None
            else:
                root.right = right
                root.left = None
            return root

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        left = self.to_list(root.left)
        right = self.to_list(root.right)
        if left:
            cur = left
            while cur.right is not None:
                cur = cur.right
            cur.right = right
            root.right = left
            root.left = None
        else:
            root.right = right
            root.left = None


root = TreeNode(val=1)
root.left = TreeNode(val=2)
root.left.left = TreeNode(val=3)
root.left.right = TreeNode(val=4)
root.right = TreeNode(val=5)
root.right.right = TreeNode(val=6)

Solution().flatten(root)

cur = root
while cur is not None:
    print(cur.val)
    cur = cur.right
