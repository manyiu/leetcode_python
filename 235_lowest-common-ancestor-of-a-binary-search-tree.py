import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        curr = root

        while True:
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right
            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left
            else:
                return curr


class TestSolution(unittest.TestCase):
    def test_1(self):
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)
        p = root.left
        q = root.right
        s = Solution()
        assert s.lowestCommonAncestor(root, p, q) == root

    def test_2(self):
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)
        p = root.left
        q = root.left.right
        s = Solution()
        assert s.lowestCommonAncestor(root, p, q) == p

    def test_3(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        p = root
        q = root.left
        s = Solution()
        assert s.lowestCommonAncestor(root, p, q) == p

    def test_4(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        p = root.left
        q = root
        s = Solution()
        assert s.lowestCommonAncestor(root, p, q) == q

    def test_5(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        p = root.left
        q = root.right
        s = Solution()
        assert s.lowestCommonAncestor(root, p, q) == root

    def test_6(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        p = root
        q = root.right
        s = Solution()
        assert s.lowestCommonAncestor(root, p, q) == root
