from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = [(0, root)]

        deepest = 0

        while queue:
            deep, node = queue.pop()

            if node:
                deep += 1

            deepest = max(deepest, deep)

            if node.left:
                queue.append((deep, node.left))
            if node.right:
                queue.append((deep, node.right))

        return deepest

    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     def dfs(head: Optional[TreeNode], deep: int) -> int:
    #         if not head:
    #             return deep
    #         return max(dfs(head.left, deep + 1), dfs(head.right, deep + 1))
    #     return dfs(root, 0)


class TestSolution(unittest.TestCase):

    def test_1(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        self.assertEqual(Solution().maxDepth(root), 3)

    def test_2(self):
        root = TreeNode(1)
        root.right = TreeNode(2)

        self.assertEqual(Solution().maxDepth(root), 2)

    def test_3(self):
        root = None

        self.assertEqual(Solution().maxDepth(root), 0)

    def test_4(self):
        root = TreeNode(0)

        self.assertEqual(Solution().maxDepth(root), 1)

    def test_5(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)

        self.assertEqual(Solution().maxDepth(root), 4)

    def test_6(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)

        self.assertEqual(Solution().maxDepth(root), 4)
