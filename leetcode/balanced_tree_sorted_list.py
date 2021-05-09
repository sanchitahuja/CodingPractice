'''

Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBSTUtil(self, start, end, tree_list) -> TreeNode:
        print('Start', start, 'end', end)
        if start > end:
            return None
        elif start == end:
            return tree_list[start]
        else:
            mid = (start + end + 1) // 2
            print('mid', mid)
            tree_list[mid].left = self.sortedListToBSTUtil(start, mid - 1, tree_list)
            tree_list[mid].right = self.sortedListToBSTUtil(mid + 1, end, tree_list)
            print('Returning mid', tree_list[mid].val, 'left', tree_list[mid].left.val if tree_list[mid].left else None,
                  'right', tree_list[mid].right.val if tree_list[mid].right else None)
            return tree_list[mid]

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        curr = head
        tree_list = []
        while curr is not None:
            tree_list.append(TreeNode(val=curr.val))
            curr = curr.next
        for i in tree_list:
            print(i.val)
        return self.sortedListToBSTUtil(0, len(tree_list) - 1, tree_list)


nodes = []
prev = None
for i in [-10, -3, 0, 5, 9]:
    n = ListNode(i)
    if prev is not None:
        prev.next = n
    nodes.append(n)
    prev = n

Solution().sortedListToBST(nodes[0])
