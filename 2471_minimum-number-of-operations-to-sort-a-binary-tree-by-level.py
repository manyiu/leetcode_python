from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        res = 0

        queue = [root]

        while queue:
            nextQueue = []
            values = []

            for node in queue:
                if node:
                    if node.left:
                        nextQueue.append(node.left)
                        values.append(node.left.val)
                    if node.right:
                        nextQueue.append(node.right)
                        values.append(node.right.val)

            sortedValues = sorted(values)
            valueIndex = {n: i for i, n in enumerate(values)}

            for i in range(len(values)):
                if values[i] != sortedValues[i]:
                    j = valueIndex[sortedValues[i]]

                    values[i], values[j] = values[j], values[i]
                    valueIndex[values[j]] = j

                    res += 1

            queue = nextQueue

        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        root = TreeNode(1)
        root.left = TreeNode(4)
        root.left.left = TreeNode(7)
        root.left.right = TreeNode(6)
        root.right = TreeNode(3)
        root.right.left = TreeNode(8)
        root.right.left.left = TreeNode(9)
        root.right.right = TreeNode(5)
        root.right.right.left = TreeNode(10)
        self.assertEqual(Solution().minimumOperations(root), 3)

    def test_2(self):
        root = TreeNode(1)
        root.left = TreeNode(3)
        root.left.left = TreeNode(7)
        root.left.right = TreeNode(6)
        root.right = TreeNode(2)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(4)
        self.assertEqual(Solution().minimumOperations(root), 3)

    def test_3(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right = TreeNode(3)
        root.right.left = TreeNode(6)
        self.assertEqual(Solution().minimumOperations(root), 0)
