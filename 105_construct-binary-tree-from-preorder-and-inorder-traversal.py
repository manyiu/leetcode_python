from typing import List, Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        splitIndex = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1 : splitIndex + 1], inorder[:splitIndex])
        root.right = self.buildTree(
            preorder[splitIndex + 1 :], inorder[splitIndex + 1 :]
        )

        return root


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = Solution()
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        root = s.buildTree(preorder, inorder)
        assert root.val == 3
        assert root.left.val == 9
        assert root.right.val == 20
        assert root.right.left.val == 15
        assert root.right.right.val == 7

    def test_2(self):
        s = Solution()
        preorder = [-1]
        inorder = [-1]
        root = s.buildTree(preorder, inorder)
        assert root.val == -1

    def test_3(self):
        s = Solution()
        preorder = [1, 2, 3]
        inorder = [3, 2, 1]
        root = s.buildTree(preorder, inorder)
        assert root.val == 1
        assert root.left.val == 2
        assert root.left.left.val == 3

    def test_4(self):
        s = Solution()
        preorder = [1, 2, 3]
        inorder = [1, 2, 3]
        root = s.buildTree(preorder, inorder)
        assert root.val == 1
        assert root.right.val == 2
        assert root.right.right.val == 3

    def test_5(self):
        s = Solution()
        preorder = [1, 2, 3]
        inorder = [1, 3, 2]
        root = s.buildTree(preorder, inorder)
        assert root.val == 1
        assert root.right.val == 2
        assert root.right.left.val == 3
