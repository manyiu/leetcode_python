from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = []

        if root:
            queue.append((float("-infinity"), float("infinity"), root))

        while queue:
            lowerLimit, upperLimit, node = queue.pop()
            if node.val <= lowerLimit or node.val >= upperLimit:
                return False
            if node.left:
                queue.append((lowerLimit, node.val, node.left))
            if node.right:
                queue.append((node.val, upperLimit, node.right))

        return True


class TestSolution(unittest.TestCase):
    def test_1(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        s = Solution()
        assert s.isValidBST(root) == True

    def test_2(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(6)
        s = Solution()
        assert s.isValidBST(root) == False

    def test_3(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(6)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(7)
        s = Solution()
        assert s.isValidBST(root) == False

    def test_4(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(7)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(8)
        s = Solution()
        assert s.isValidBST(root) == True

    def test_5(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(7)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(8)
        s = Solution()
        assert s.isValidBST(root) == False

    def test_6(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(7)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)
        s = Solution()
        assert s.isValidBST(root) == True

    def test_7(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(7)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(5)
        s = Solution()
        assert s.isValidBST(root) == False

    def test_8(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(7)
        root.right.left = TreeNode(8)
        root.right.right = TreeNode(9)
        s = Solution()
        assert s.isValidBST(root) == False
