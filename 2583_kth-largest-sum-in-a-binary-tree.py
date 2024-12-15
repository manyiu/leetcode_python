import heapq
from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        q = [root]
        maxHeap = []

        while q:
            next = []
            layerVal = 0

            for node in q:
                layerVal += node.val

                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)

            heapq.heappush(maxHeap, -layerVal)
            q = next

        heapq.heapify(maxHeap)

        for i in range(1, k + 1):
            if not maxHeap:
                break
            if i == k:
                return -heapq.heappop(maxHeap)
            else:
                heapq.heappop(maxHeap)

        return -1


class TestSolution(unittest.TestCase):
    def test_1(self):
        root = TreeNode(5)
        root.left = TreeNode(8)
        root.right = TreeNode(9)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(1)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(7)
        root.left.left.left = TreeNode(4)
        root.left.left.right = TreeNode(6)
        k = 2
        assert Solution().kthLargestLevelSum(root, k) == 13

    def test_2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        k = 1
        assert Solution().kthLargestLevelSum(root, k) == 3
