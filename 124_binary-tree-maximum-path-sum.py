from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(node) -> int:
            nonlocal res
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            leftMax = max(left, 0)
            rightMax = max(right, 0)

            res = max(res, node.val + leftMax + rightMax)

            return node.val + max(leftMax, rightMax)

        dfs(root)
        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        s = Solution()
        assert s.maxPathSum(root) == 6

    def test_2(self):
        root = TreeNode(-10)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        s = Solution()
        assert s.maxPathSum(root) == 42

    def test_3(self):
        root = TreeNode(-3)
        s = Solution()
        assert s.maxPathSum(root) == -3

    def test_4(self):
        root = TreeNode(2)
        root.left = TreeNode(-1)
        s = Solution()
        assert s.maxPathSum(root) == 2

    def test_5(self):
        root = TreeNode(1)
        root.left = TreeNode(-2)
        root.right = TreeNode(3)
        s = Solution()
        assert s.maxPathSum(root) == 4
