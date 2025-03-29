import heapq
from typing import List
import unittest


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7

        scores = []

        for num in nums:
            score = 0
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    score += 1
                    while num % i == 0:
                        num //= i
            if num >= 2:
                score += 1
            scores.append(score)

        left = [-1] * len(scores)
        right = [len(scores)] * len(scores)

        stack = []

        for i, score in enumerate(scores):
            while stack and scores[stack[-1]] < score:
                idx = stack.pop()
                right[idx] = i
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        max_heap = [(-n, i) for i, n in enumerate(nums)]
        heapq.heapify(max_heap)

        res = 1

        while k > 0:
            n, idx = heapq.heappop(max_heap)
            n *= -1

            left_count = idx - left[idx]
            right_count = right[idx] - idx

            count = left_count * right_count
            operation = min(k, count)

            res = (res * pow(n, operation, MOD)) % MOD
            k -= operation

        return res


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        nums = [8, 3, 9, 3, 8]
        k = 2
        output = 81
        self.assertEqual(Solution().maximumScore(nums, k), output)

    def test_example_2(self):
        nums = [19, 12, 14, 6, 10, 18]
        k = 3
        output = 4788
        self.assertEqual(Solution().maximumScore(nums, k), output)
