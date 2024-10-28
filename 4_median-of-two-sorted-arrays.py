from typing import List
import unittest


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        total = len(nums1) + len(nums2)
        half = (total + 1) // 2
        is_odd = total % 2 == 1

        l, r = 0, len(nums1) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            nums1Left, nums1Right = float("-infinity"), float("infinity")
            nums2Left, nums2Right = float("-infinity"), float("infinity")

            if i >= 0:
                nums1Left = nums1[i]

            if j >= 0:
                nums2Left = nums2[j]

            if i + 1 < len(nums1):
                nums1Right = nums1[i + 1]

            if j + 1 < len(nums2):
                nums2Right = nums2[j + 1]

            if nums1Left <= nums2Right and nums2Left <= nums1Right:
                if is_odd:
                    return max(nums1Left, nums2Left)
                else:
                    return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) / 2
            elif nums1Left > nums2Right:
                r = i - 1
            else:
                l = i + 1


# def test_10(self):
#         nums1 = [2, 5, 7, 8, 9]
#         nums2 = [1, 2, 8]
#         self.assertEqual(Solution().findMedianSortedArrays(nums1, nums2), 6.0)


class TestSolution(unittest.TestCase):
    def test_0(self):
        nums1 = [1, 3]
        nums2 = [2]
        self.assertEqual(Solution().findMedianSortedArrays(nums1, nums2), 2.0)

    def test_1(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        self.assertEqual(Solution().findMedianSortedArrays(nums1, nums2), 2.5)

    def test_2(self):
        nums1 = [0, 0]
        nums2 = [0, 0]
        self.assertEqual(Solution().findMedianSortedArrays(nums1, nums2), 0.0)

    def test_3(self):
        nums1 = []
        nums2 = [1]
        self.assertEqual(Solution().findMedianSortedArrays(nums1, nums2), 1.0)

    def test_4(self):
        nums1 = [2]
        nums2 = []
        self.assertEqual(Solution().findMedianSortedArrays(nums1, nums2), 2.0)

    def test_5(self):
        nums1 = [1, 3]
        nums2 = [2, 7]
        self.assertEqual(Solution().findMedianSortedArrays(nums1, nums2), 2.5)

    def test_6(self):
        nums1 = [1, 2]
        nums2 = [3, 4, 5]
        self.assertEqual(Solution().findMedianSortedArrays(nums1, nums2), 3.0)

    def test_7(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        self.assertEqual(Solution().findMedianSortedArrays(nums1, nums2), 3.5)

    def test_8(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5]
        self.assertEqual(Solution().findMedianSortedArrays(nums1, nums2), 3.0)

    def test_9(self):
        nums1 = [1, 2]
        nums2 = [3, 4, 5]
        self.assertEqual(Solution().findMedianSortedArrays(nums1, nums2), 3.0)

    def test_10(self):
        nums1 = [2, 5, 7, 8, 9]
        nums2 = [1, 2, 8]
        self.assertEqual(Solution().findMedianSortedArrays(nums1, nums2), 6.0)

    def test_11(self):
        nums1 = [2]
        nums2 = [1, 3, 4, 5, 6]
        self.assertEqual(Solution().findMedianSortedArrays(nums1, nums2), 3.5)
