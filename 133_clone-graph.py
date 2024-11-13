from typing import Optional
import unittest


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        oldToNew = {}
        queue = [node]

        while queue:
            curr = queue.pop(0)

            if curr not in oldToNew:
                oldToNew[curr] = Node()
            oldToNew[curr].val = curr.val

            for neighbor in curr.neighbors:
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                oldToNew[curr].neighbors.append(oldToNew[neighbor])

        return oldToNew[node]


class TestSolution(unittest.TestCase):
    def test_1(self):
        node = Node(1)
        node.neighbors = [Node(2), Node(4)]
        node.neighbors[0].neighbors = [node, node.neighbors[1]]
        node.neighbors[1].neighbors = [node, node.neighbors[0]]

        clone = Solution().cloneGraph(node)

        self.assertEqual(clone.val, 1)
        self.assertEqual(clone.neighbors[0].val, 2)
        self.assertEqual(clone.neighbors[1].val, 4)
        self.assertEqual(clone.neighbors[0].neighbors[0].val, 1)
        self.assertEqual(clone.neighbors[0].neighbors[1].val, 4)
        self.assertEqual(clone.neighbors[1].neighbors[0].val, 1)
        self.assertEqual(clone.neighbors[1].neighbors[1].val, 2)

    def test_2(self):
        node = Node(1)
        node.neighbors = [Node(2)]
        node.neighbors[0].neighbors = [node]

        clone = Solution().cloneGraph(node)

        self.assertEqual(clone.val, 1)
        self.assertEqual(clone.neighbors[0].val, 2)
        self.assertEqual(clone.neighbors[0].neighbors[0].val, 1)

    def test_3(self):
        node = Node(1)

        clone = Solution().cloneGraph(node)

        self.assertEqual(clone.val, 1)
        self.assertEqual(clone.neighbors, [])
