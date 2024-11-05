from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     if not root:
    #         return None
    #     queue = [root]
    #     while queue:
    #         node = queue.pop()
    #         node.left, node.right = node.right, node.left
    #         if node.left:
    #             queue.append(node.left)
    #         if node.right:
    #             queue.append(node.right)
    #     return root


class TestSolution(unittest.TestCase):

    def test_1(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)

        Solution().invertTree(root)

        self.assertEqual(root.val, 4)
        self.assertEqual(root.left.val, 7)
        self.assertEqual(root.right.val, 2)
        self.assertEqual(root.left.left.val, 9)
        self.assertEqual(root.left.right.val, 6)
        self.assertEqual(root.right.left.val, 3)
        self.assertEqual(root.right.right.val, 1)

    def test_2(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)

        Solution().invertTree(root)

        self.assertEqual(root.val, 2)
        self.assertEqual(root.left.val, 3)
        self.assertEqual(root.right.val, 1)
