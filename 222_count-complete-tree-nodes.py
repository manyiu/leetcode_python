from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def countLeftDepth(node) -> int:
            d = 0
            while node:
                node = node.left
                d += 1
            return d

        def countRightDepth(node) -> int:
            d = 0
            while node:
                node = node.right
                d += 1
            return d

        leftDepth = countLeftDepth(root.left)
        rightDepth = countRightDepth(root.right)

        if leftDepth == rightDepth:
            return 2 ** (leftDepth + 1) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)


class TestSolution:
    def test_1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)

        assert Solution().countNodes(root) == 6

    def test_2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        assert Solution().countNodes(root) == 7

    def test_3(self):
        root = TreeNode(1)

        assert Solution().countNodes(root) == 1
