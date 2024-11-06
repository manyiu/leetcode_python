from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            nodeP, nodeQ = stack.pop()

            if nodeP is None and nodeQ is None:
                continue

            if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                return False

            stack.append((nodeP.left, nodeQ.left))
            stack.append((nodeP.right, nodeQ.right))

        return True


class TestSolution(unittest.TestCase):
    def test_1(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)
        s = Solution()
        assert s.isSameTree(p, q) == True

    def test_2(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        q = TreeNode(1)
        q.right = TreeNode(2)
        s = Solution()
        assert s.isSameTree(p, q) == False

    def test_3(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(1)
        q = TreeNode(1)
        q.left = TreeNode(1)
        q.right = TreeNode(2)
        s = Solution()
        assert s.isSameTree(p, q) == False
