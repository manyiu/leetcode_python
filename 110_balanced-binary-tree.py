from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        visit = [False]
        depths = {None: 0}

        while stack:
            curr, visited = stack.pop(), visit.pop()
            if curr:
                if visited:
                    if abs(depths[curr.left] - depths[curr.right]) > 1:
                        return False
                    depths[curr] = 1 + max(depths[curr.left], depths[curr.right])
                else:
                    stack.append(curr)
                    visit.append(True)
                    stack.append(curr.left)
                    visit.append(False)
                    stack.append(curr.right)
                    visit.append(False)
        return True

    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     def dfs(node: Optional[TreeNode]):
    #         if not node:
    #             return (True, 0)

    #         left = dfs(node.left)
    #         right = dfs(node.right)

    #         balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

    #         return (balanced, 1 + max(left[1], right[1]))

    #     return dfs(root)[0]


class TestSolution(unittest.TestCase):
    def test_1(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        s = Solution()
        assert s.isBalanced(root) == True

    def test_2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.left.left.right = TreeNode(4)
        s = Solution()
        assert s.isBalanced(root) == False

    def test_3(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        root.right.right.right.right = TreeNode(5)
        s = Solution()
        assert s.isBalanced(root) == False

    def test_4(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.left.left.right = TreeNode(4)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        root.right.right.right.right = TreeNode(5)
        s = Solution()
        assert s.isBalanced(root) == False
