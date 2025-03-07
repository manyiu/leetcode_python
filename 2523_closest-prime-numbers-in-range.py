from typing import List
import unittest


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime() -> List[int]:
            is_prime = [True] * (right + 1)
            is_prime[0] = is_prime[1] = False

            for i in range(2, int(right**0.5) + 1):
                if not is_prime[i]:
                    continue

                for j in range(i * 2, right + 1, i):
                    is_prime[j] = False

            primes = []

            for i in range(left, len(is_prime)):
                if is_prime[i]:
                    primes.append(i)

            return primes

        primes = isPrime()

        res = [-1, -1]
        min_diff = float("inf")

        for i in range(1, len(primes)):
            diff = primes[i] - primes[i - 1]
            if diff < min_diff:
                min_diff = diff
                res = [primes[i - 1], primes[i]]

        return res


# class Solution:
#     cache = {0: False, 1: False, 2: True}

#     def isPrime(self, n: int) -> bool:
#         if n in Solution.cache:
#             return Solution.cache[n]

#         for i in range(2, int(n**0.5) + 1):
#             if n % i == 0:
#                 Solution.cache[n] = False
#                 return False

#         Solution.cache[n] = True
#         return True

#     def closestPrimes(self, left: int, right: int) -> List[int]:
#         min_diff = float("inf")
#         prev = -1
#         res = [-1, -1]

#         for num in range(left, right + 1):
#             if self.isPrime(num):
#                 if prev != -1 and num - prev < min_diff:
#                     min_diff = num - prev
#                     res = [prev, num]
#                 prev = num

#         return res if min_diff != float("inf") else [-1, -1]


class TestSolution(unittest.TestCase):
    def test_1(self):
        left = 10
        right = 19
        output = [11, 13]
        self.assertEqual(Solution().closestPrimes(left, right), output)

    def test_2(self):
        left = 4
        right = 6
        output = [-1, -1]
        self.assertEqual(Solution().closestPrimes(left, right), output)
