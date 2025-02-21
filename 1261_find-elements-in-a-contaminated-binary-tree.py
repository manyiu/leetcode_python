from typing import Optional
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.contain = set()

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return

            self.contain.add(node.val)

            if node.left:
                node.left.val = 2 * node.val + 1
                dfs(node.left)
            if node.right:
                node.right.val = 2 * node.val + 2
                dfs(node.right)

        root.val = 0
        dfs(root)

    def find(self, target: int) -> bool:
        return target in self.contain


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)


class TestFindElements(unittest.TestCase):
    def test_1(self):
        root = TreeNode(-1, right=TreeNode(-1))
        obj = FindElements(root)
        self.assertFalse(obj.find(1))
        self.assertTrue(obj.find(2))

    def test_2(self):
        root = TreeNode(-1, TreeNode(-1, TreeNode(-1), TreeNode(-1)), TreeNode(-1))
        obj = FindElements(root)
        self.assertTrue(obj.find(1))
        self.assertTrue(obj.find(3))
        self.assertFalse(obj.find(5))

    def test_3(self):
        root = TreeNode(-1, right=TreeNode(-1, TreeNode(-1, TreeNode(-1))))
        obj = FindElements(root)
        self.assertTrue(obj.find(2))
        self.assertFalse(obj.find(3))
        self.assertFalse(obj.find(4))
        self.assertTrue(obj.find(5))
