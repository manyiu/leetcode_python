import unittest

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, a: int, b: int) -> bool:
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False
        
        if root_a < root_b:
            self.parent[root_b] = root_a
        else:
            self.parent[root_a] = root_b

        return True

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind(26)

        for a, b in zip(s1, s2):
            uf.union(ord(a)-ord('a'), ord(b)-ord('a'))

        result = []

        for char in baseStr:
            root = uf.find(ord(char) - ord('a'))
            result.append(chr(root + ord('a')))

        return ''.join(result)
        

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        s1 = "parker"
        s2 = "morris"
        baseStr = "parser"
        expected = "makkek"
        solution = Solution()
        result = solution.smallestEquivalentString(s1, s2, baseStr)
        self.assertEqual(result, expected)

    def test_example_2(self):
        s1 = "hello"
        s2 = "world"
        baseStr = "hold"
        expected = "hdld"
        solution = Solution()
        result = solution.smallestEquivalentString(s1, s2, baseStr)
        self.assertEqual(result, expected)