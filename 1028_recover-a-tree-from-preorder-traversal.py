from collections import defaultdict
from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        node_by_level = defaultdict(list)

        i = 0

        while i < len(traversal):
            start = i

            while i + 1 < len(traversal) and traversal[i] == "-":
                i += 1

            level = i - start

            j = i

            while j + 1 < len(traversal) and traversal[j + 1] != "-":
                j += 1

            val = int(traversal[i : j + 1])

            if level == 0:
                root = TreeNode(val)
                node_by_level[level].append(root)
            else:
                parent = node_by_level[level - 1][-1]

                node = TreeNode(val)

                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node

                node_by_level[level].append(node)

            i = j + 1

        return node_by_level[0][0]


class TestSolution(unittest.TestCase):
    def test_1(self):
        traversal = "1-2--3--4-5--6--7"
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(3), TreeNode(4)),
            TreeNode(5, TreeNode(6), TreeNode(7)),
        )
        self.assertEqual(Solution().recoverFromPreorder(traversal), root)

    def test_2(self):
        traversal = "1-2--3---4-5--6---7"
        root = TreeNode(
            1,
            TreeNode(
                2, TreeNode(3, TreeNode(4)), TreeNode(5, TreeNode(6), TreeNode(7))
            ),
        )
        self.assertEqual(Solution().recoverFromPreorder(traversal), root)

    def test_3(self):
        traversal = "1-401--349---90--88"
        root = TreeNode(1, TreeNode(401, TreeNode(349, TreeNode(90)), TreeNode(88)))
        self.assertEqual(Solution().recoverFromPreorder(traversal), root)
