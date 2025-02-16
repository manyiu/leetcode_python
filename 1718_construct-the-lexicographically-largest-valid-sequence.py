from typing import List
import unittest


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [-1] * (2 * n - 1)
        used = set()

        def backtrack(i):
            if i == len(res):
                return True
            
            for num in range(n, 0, -1):
                if num in used:
                    continue
                if num > 1 and (i + num >= len(res) or res[i + num] != -1):
                    continue
        
                used.add(num)

                res[i] = num

                if num > 1:
                    res[i + num] = num

                j = i + 1

                while j < len(res) and res[j] != -1:
                    j += 1
                
                if backtrack(j):
                    return True

                used.remove(num)
                res[i] = -1
                if num > 1:
                    res[i + num] = -1
        
        backtrack(0)

        return res

class TestSolution(unittest.TestCase):
    def test_1(self):
        n = 3
        output = [3,1,2,3,2]
        self.assertEqual(Solution().constructDistancedSequence(n), output)

    def test_2(self):
        n = 5
        output = [5,3,1,4,3,5,2,4,2]
        self.assertEqual(Solution().constructDistancedSequence(n), output)