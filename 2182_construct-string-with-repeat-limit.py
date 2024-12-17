import heapq
import unittest


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = {}

        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1

        maxHeap = []

        for c, freq in count.items():
            maxHeap.append((-ord(c), freq))

        heapq.heapify(maxHeap)

        res = ""

        while maxHeap:
            firstCh, firstFreq = heapq.heappop(maxHeap)
            firstCh = chr(-firstCh)

            if res and res[-1] == firstCh:
                if not maxHeap:
                    return res

                secondCh, secondFreq = heapq.heappop(maxHeap)
                secondCh = chr(-secondCh)

                res += secondCh
                secondFreq -= 1

                if secondFreq > 0:
                    heapq.heappush(maxHeap, (-ord(secondCh), secondFreq))

                heapq.heappush(maxHeap, (-ord(firstCh), firstFreq))

            else:
                for _ in range(min(repeatLimit, firstFreq)):
                    res += firstCh

                firstFreq -= min(repeatLimit, firstFreq)

                if firstFreq > 0:
                    heapq.heappush(maxHeap, (-ord(firstCh), firstFreq))

        return res

    # def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
    #     count = [0] * 26

    #     for c in s:
    #         count[ord(c) - ord("a")] += 1

    #     result = ""

    #     maxI = -1
    #     i = 25

    #     while i >= 0:
    #         ch = chr(i + ord("a"))

    #         if count[i] > 0 and (len(result) == 0 or result[len(result) - 1] != ch):
    #             if maxI > i:
    #                 result += ch
    #                 count[i] -= 1

    #                 i = maxI
    #                 maxI = -1
    #             else:
    #                 for _ in range(min(repeatLimit, count[i])):
    #                     result += chr(i + ord("a"))
    #                 count[i] -= min(repeatLimit, count[i])

    #                 if count[i] > 0:
    #                     maxI = i
    #                     i -= 1
    #         else:
    #             i -= 1

    #     return result


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "cczazcc"
        repeatLimit = 3
        output = "zzcccac"
        self.assertEqual(Solution().repeatLimitedString(s, repeatLimit), output)

    def test_2(self):
        s = "aababab"
        repeatLimit = 2
        output = "bbabaa"
        self.assertEqual(Solution().repeatLimitedString(s, repeatLimit), output)
