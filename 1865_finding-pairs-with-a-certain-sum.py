from typing import Counter, List
import unittest


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1_count = Counter(nums1)
        self.nums2_count = Counter(nums2)
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        self.nums2_count[old_val] -= 1
        self.nums2[index] += val
        self.nums2_count[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        count = 0

        for num1, count1 in self.nums1_count.items():
            complement = tot - num1
            count2 = self.nums2_count.get(complement, 0)
            count += count1 * count2

        return count


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        nums1 = [1, 1, 2, 2, 2, 3]
        nums2 = [1, 4, 5, 2, 5, 4]
        obj = FindSumPairs(nums1, nums2)
        self.assertEqual(obj.count(7), 8)
        obj.add(3, 2)
        self.assertEqual(obj.count(8), 2)
        self.assertEqual(obj.count(4), 1)
        obj.add(0, 1)
        obj.add(1, 1)
        self.assertEqual(obj.count(7), 11)
