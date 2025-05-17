from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, r = 0, len(nums) - 1

        i = 0

        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1


    # def merge(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     i, j = 0, 0
    #     res = []

    #     while i < len(nums1) and j < len(nums2):
    #         if nums1[i] <= nums2[j]:
    #             res.append(nums1[i])
    #             i += 1
    #         else:
    #             res.append(nums2[j])
    #             j += 1

    #     if i == len(nums1):
    #         res = res + nums2[j:]
    #     elif j == len(nums2):
    #         res = res + nums1[i:]

    #     return res
    
    # def mergeSort(self, nums: List[int]) -> List[int]:
    #     if len(nums) < 2:
    #         return nums

    #     m = len(nums) // 2
    #     a = nums[:m]
    #     b = nums[m:]

    #     return self.merge(self.mergeSort(a), self.mergeSort(b))

    # def sortColors(self, nums: List[int]) -> None:
    #     nums[:]= self.mergeSort(nums)
        