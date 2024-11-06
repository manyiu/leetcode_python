from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node: Optional[TreeNode]):
            nonlocal res

            if not node:
                return 0

            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            res = max(res, leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)

        dfs(root)

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        s = Solution()
        assert s.diameterOfBinaryTree(root) == 3

    def test_2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        s = Solution()
        assert s.diameterOfBinaryTree(root) == 1

    def test_3(self):
        root = TreeNode(1)
        s = Solution()
        assert s.diameterOfBinaryTree(root) == 0

    def test_4(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.left.left.left.left = TreeNode(5)
        s = Solution()
        assert s.diameterOfBinaryTree(root) == 4
