# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''
    1 for node covered
    0 node has camera
    -1 node is not covered
    '''

    def min_camera_util(self, root):
        if root is None:
            return 1
        l = self.min_camera_util(root.left)
        r = self.min_camera_util(root.right)
        if l == -1 or r == -1:
            self.camera += 1
            return 0
        if l == 0 or r == 0:
            return 1
        return -1

    def minCameraCover(self, root: TreeNode) -> int:
        self.camera = 0
        return self.camera + 1 if self.min_camera_util(root) == -1 else self.camera


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

# root.right = TreeNode(5)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)


print(Solution().minCameraCover(root))
