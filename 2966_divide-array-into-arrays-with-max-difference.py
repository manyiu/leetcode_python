from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()

        for i in range(n // 3):
            if nums[i * 3 + 2] - nums[i * 3] <= k:
                res.append(nums[i * 3 : i * 3 + 3])
            else:
                return []

        return res
