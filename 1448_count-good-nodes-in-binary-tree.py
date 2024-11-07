import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = []
        result = 0

        if root:
            queue.append((root.val, root))

        while queue:
            weight, node = queue.pop()
            nextWeight = max(weight, node.val)
            if weight <= node.val:
                result += 1
            if node.left:
                queue.append((nextWeight, node.left))
            if node.right:
                queue.append((nextWeight, node.right))

        return result


class TestSolution(unittest.TestCase):
    def test_1(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.left.left = TreeNode(3)
        root.right = TreeNode(4)
        root.right.left = TreeNode(1)
        root.right.right = TreeNode(5)
        s = Solution()
        assert s.goodNodes(root) == 4

    def test_2(self):
        root = TreeNode(3)
        root.left = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(2)
        s = Solution()
        assert s.goodNodes(root) == 3

    def test_3(self):
        root = TreeNode(1)
        s = Solution()
        assert s.goodNodes(root) == 1

    def test_4(self):
        root = None
        s = Solution()
        assert s.goodNodes(root) == 0

    def test_5(self):
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        s = Solution()
        assert s.goodNodes(root) == 3

    def test_6(self):
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)
        root.right.left = TreeNode(1)
        root.right.right = TreeNode(1)
        s = Solution()
        assert s.goodNodes(root) == 7

    def test_7(self):
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)
        root.right.left = TreeNode(1)
        root.right.right = TreeNode(1)
        root.left.left.left = TreeNode(1)
        root.left.left.right = TreeNode(1)
        root.left.right.left = TreeNode(1)
        root.left.right.right = TreeNode(1)
        root.right.left.left = TreeNode(1)
        root.right.left.right = TreeNode(1)
        root.right.right.left = TreeNode(1)
        root.right.right.right = TreeNode(1)
        s = Solution()
        assert s.goodNodes(root) == 15
