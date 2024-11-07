from typing import List, Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        result = []

        if root:
            queue.append(root)

        while queue:
            nextQueue = []
            for node in queue:
                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)
            result.append(queue[-1].val)
            queue = nextQueue

        return result


class TestSolution(unittest.TestCase):
    def test_1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(5)
        root.right = TreeNode(3)
        root.right.right = TreeNode(4)
        s = Solution()
        assert s.rightSideView(root) == [1, 3, 4]

    def test_2(self):
        root = TreeNode(1)
        root.right = TreeNode(3)
        s = Solution()
        assert s.rightSideView(root) == [1, 3]

    def test_3(self):
        root = None
        s = Solution()
        assert s.rightSideView(root) == []
