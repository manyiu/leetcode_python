from typing import List, Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        result = []

        if root:
            queue.append(root)

        while queue:
            nextQueue = []
            levelValues = []

            for node in queue:
                levelValues.append(node.val)
                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)

            queue = nextQueue
            result.append(levelValues)

        return result


class TestSolution(unittest.TestCase):
    def test_1(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        s = Solution()
        assert s.levelOrder(root) == [[3], [9, 20], [15, 7]]

    def test_2(self):
        root = TreeNode(1)
        s = Solution()
        assert s.levelOrder(root) == [[1]]

    def test_3(self):
        root = None
        s = Solution()
        assert s.levelOrder(root) == []
