from typing import List
import unittest


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for triplet in triplets:
            invalid = False
            matched = []

            for i in range(len(target)):
                if triplet[i] > target[i]:
                    invalid = True
                    break
                if triplet[i] == target[i]:
                    matched.append(i)

            if not invalid:
                for i in matched:
                    good.add(i)

        return len(good) == len(target)


class TestSolution(unittest.TestCase):
    def test_1(self):
        triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
        target = [2, 7, 5]
        assert Solution().mergeTriplets(triplets, target) == True

    def test_2(self):
        triplets = [[3, 4, 5], [4, 5, 6]]
        target = [3, 2, 5]
        assert Solution().mergeTriplets(triplets, target) == False

    def test_3(self):
        triplets = [[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]]
        target = [5, 5, 5]
        assert Solution().mergeTriplets(triplets, target) == True

    def test_4(self):
        triplets = [[3, 5, 1], [10, 5, 7]]
        target = [3, 5, 7]
        assert Solution().mergeTriplets(triplets, target) == False
