from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
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

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]

        while stack:
            curr = stack.pop()

            if self.sameTree(curr, subRoot):
                return True

            if curr:
                stack.append(curr.left)
                stack.append(curr.right)

        return False


class TestSolution(unittest.TestCase):
    def test_1(self):
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        subRoot = TreeNode(4)
        subRoot.left = TreeNode(1)
        subRoot.right = TreeNode(2)
        s = Solution()
        assert s.isSubtree(root, subRoot) == True

    def test_2(self):
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(0)
        subRoot = TreeNode(4)
        subRoot.left = TreeNode(1)
        subRoot.right = TreeNode(2)
        s = Solution()
        assert s.isSubtree(root, subRoot) == False

    def test_3(self):
        root = TreeNode(1)
        root.left = TreeNode(1)
        subRoot = TreeNode(1)
        s = Solution()
        assert s.isSubtree(root, subRoot) == True

    def test_4(self):
        root = TreeNode(1)
        root.left = TreeNode(1)
        subRoot = TreeNode(2)
        s = Solution()
        assert s.isSubtree(root, subRoot) == False

    def test_5(self):
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        subRoot = TreeNode(1)
        s = Solution()
        assert s.isSubtree(root, subRoot) == True

    def test_6(self):
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        subRoot = TreeNode(2)
        s = Solution()
        assert s.isSubtree(root, subRoot) == False
