from typing import List, Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        stack = []
        result = []

        while curr or stack:
            if curr:
                stack.append(curr.right)
                result.append(curr.val)
                curr = curr.left
            else:
                curr = stack.pop()

        return result


class TestPreorderTraversal(unittest.TestCase):
    def test_preorder_traversal(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        assert Solution().preorderTraversal(root) == [1, 2, 3]
        assert Solution().preorderTraversal(None) == []
        root = TreeNode(1)
        root.left = TreeNode(2)
        assert Solution().preorderTraversal(root) == [1, 2]
        root = TreeNode(1)
        root.right = TreeNode(2)
        assert Solution().preorderTraversal(root) == [1, 2]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        assert Solution().preorderTraversal(root) == [1, 2, 3]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(5)
        assert Solution().preorderTraversal(root) == [1, 2, 3, 4, 5]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        assert Solution().preorderTraversal(root) == [1, 2, 3, 4, 5]
