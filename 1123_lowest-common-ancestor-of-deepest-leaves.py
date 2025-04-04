from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node) -> tuple[int, Optional[TreeNode]]:
            if not node:
                return 0, node

            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)

            if left_depth == right_depth:
                return left_depth + 1, node
            elif left_depth > right_depth:
                return left_depth + 1, left_lca
            else:
                return right_depth + 1, right_lca

        _, lca = dfs(root)

        return lca


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        root = TreeNode(3)
        root.left = TreeNode(5)
        root.right = TreeNode(1)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(2)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(8)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(4)

        output = Solution().lcaDeepestLeaves(root)

        self.assertEqual(output.val, 2)
        self.assertEqual(output.left.val, 7)
        self.assertEqual(output.right.val, 4)

    def test_example_2(self):
        root = TreeNode(1)

        output = Solution().lcaDeepestLeaves(root)

        self.assertEqual(output.val, 1)

    def test_example_3(self):
        root = TreeNode(0)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        root.left.right = TreeNode(2)

        output = Solution().lcaDeepestLeaves(root)

        self.assertEqual(output.val, 2)
