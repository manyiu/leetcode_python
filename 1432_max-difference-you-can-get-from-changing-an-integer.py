import unittest


class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)
        max_num_str = num_str
        min_num_str = num_str
        max_num_found = False
        min_num_found = False

        for i in range(len(num_str)):
            if not max_num_found and num_str[i] != "9":
                max_num_str = max_num_str.replace(num_str[i], "9")
                max_num_found = True
            if not min_num_found and i == 0 and num_str[i] != "1":
                min_num_str = min_num_str.replace(num_str[i], "1")
                min_num_found = True
            elif (
                not min_num_found
                and i > 0
                and num_str[i] != "0"
                and num_str[i] != num_str[0]
            ):
                min_num_str = min_num_str.replace(num_str[i], "0")
                min_num_found = True
            if max_num_found and min_num_found:
                break

        return int(max_num_str) - int(min_num_str)


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        num = 555
        expected = 888
        solution = Solution()
        result = solution.maxDiff(num)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_example_2(self):
        num = 9
        expected = 8
        solution = Solution()
        result = solution.maxDiff(num)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")
