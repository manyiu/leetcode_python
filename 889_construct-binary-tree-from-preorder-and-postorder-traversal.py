from typing import List, Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None

        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root

        left_val = preorder[1]
        left_subtree_size = postorder.index(left_val) + 1

        left_preorder = preorder[1 : 1 + left_subtree_size]
        left_postorder = postorder[:left_subtree_size]

        right_preorder = preorder[1 + left_subtree_size :]
        right_postorder = postorder[left_subtree_size:-1]

        root.left = self.constructFromPrePost(left_preorder, left_postorder)
        root.right = self.constructFromPrePost(right_preorder, right_postorder)
        return root


class TestSolution(unittest.TestCase):
    def test_1(self):
        preorder = [1, 2, 4, 5, 3, 6, 7]
        postorder = [4, 5, 2, 6, 7, 3, 1]
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, TreeNode(6), TreeNode(7)),
        )
        self.assertEqual(Solution().constructFromPrePost(preorder, postorder), root)

    def test_2(self):
        preorder = [1]
        postorder = [1]
        root = TreeNode(1)
        self.assertEqual(Solution().constructFromPrePost(preorder, postorder), root)
