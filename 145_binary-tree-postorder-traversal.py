from typing import List, Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        visit = [False]
        result = []

        while stack:
            curr, visited = stack.pop(), visit.pop()
            if curr:
                if visited:
                    result.append(curr.val)
                else:
                    stack.append(curr)
                    visit.append(True)
                    stack.append(curr.right)
                    visit.append(False)
                    stack.append(curr.left)
                    visit.append(False)

        return result


class TestPostorderTraversal(unittest.TestCase):
    def test_postorder_traversal(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        assert Solution().postorderTraversal(root) == [3, 2, 1]
        assert Solution().postorderTraversal(None) == []
        root = TreeNode(1)
        root.left = TreeNode(2)
        assert Solution().postorderTraversal(root) == [2, 1]
        root = TreeNode(1)
        root.right = TreeNode(2)
        assert Solution().postorderTraversal(root) == [2, 1]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        assert Solution().postorderTraversal(root) == [2, 3, 1]
