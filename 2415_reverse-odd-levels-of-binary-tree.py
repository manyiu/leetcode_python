from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        level = 0
        stock = [root]

        while stock:
            level += 1

            nextStock = []

            for node in stock:
                if node.left:
                    nextStock.append(node.left)
                if node.right:
                    nextStock.append(node.right)

            if level % 2 == 1 and nextStock:
                for i in range((len(nextStock) + 1) // 2):
                    nextStock[i].val, nextStock[len(nextStock) - i - 1].val = (
                        nextStock[len(nextStock) - i - 1].val,
                        nextStock[i].val,
                    )

            stock = nextStock

        return root


class TestSolution(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        input = TreeNode(
            2,
            TreeNode(3, TreeNode(8), TreeNode(13)),
            TreeNode(5, TreeNode(21), TreeNode(34)),
        )
        output = TreeNode(
            2,
            TreeNode(5, TreeNode(8), TreeNode(13)),
            TreeNode(3, TreeNode(21), TreeNode(34)),
        )
        result = solution.reverseOddLevels(input)

        self.assertEqual(result.val, output.val)
        self.assertEqual(result.left.val, output.left.val)
        self.assertEqual(result.right.val, output.right.val)
        self.assertEqual(result.left.left.val, output.left.left.val)
        self.assertEqual(result.left.right.val, output.left.right.val)
        self.assertEqual(result.right.left.val, output.right.left.val)
        self.assertEqual(result.right.right.val, output.right.right.val)

    def test_2(self):
        solution = Solution()
        input = TreeNode(7, TreeNode(13), TreeNode(11))
        output = TreeNode(7, TreeNode(11), TreeNode(13))
        result = solution.reverseOddLevels(input)

        self.assertEqual(result.val, output.val)
        self.assertEqual(result.left.val, output.left.val)
        self.assertEqual(result.right.val, output.right.val)
