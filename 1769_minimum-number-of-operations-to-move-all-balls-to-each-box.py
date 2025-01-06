from typing import List
import unittest


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)

        res = [0] * n

        leftCount, leftMove = 0, 0

        for i in range(n):
            res[i] += leftCount + leftMove
            leftMove = leftCount + leftMove
            if boxes[i] == "1":
                leftCount += 1

        rightCount, rightMove = 0, 0

        for j in range(n - 1, -1, -1):
            res[j] += rightCount + rightMove
            rightMove = rightCount + rightMove
            if boxes[j] == "1":
                rightCount += 1

        return res

    # def minOperations(self, boxes: str) -> List[int]:
    #     boxes_hash = {idx: int(box) for idx, box in enumerate(boxes)}

    #     n = len(boxes)

    #     res = [0] * n

    #     for i in range(n):
    #         curr = 0

    #         for j in boxes_hash:
    #             if i != j and boxes_hash[j] > 0:
    #                 curr += abs(i - j)

    #         res[i] = curr

    #     return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        input = "110"
        output = [1, 1, 3]
        self.assertEqual(Solution().minOperations(input), output)

    def test_2(self):
        input = "001011"
        output = [11, 8, 5, 4, 3, 4]
        self.assertEqual(Solution().minOperations(input), output)
