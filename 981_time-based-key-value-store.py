import unittest


class TimeMap:

    def __init__(self):
        # self.values = {
        #     "foo": [(1, "bar"), (2, "bar1")],
        #     "hello": [(2, "world"), (5, "world 2")]
        # }
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp, value))
        else:
            self.store[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        if key not in self.store:
            return res

        store = self.store[key]

        l, r = 0, len(store) - 1

        while l <= r:
            m = (l + r) // 2

            if store[m][0] <= timestamp:
                l = m + 1
                res = store[m][1]
            else:
                r = m - 1

        return res

    # Without res variable
    # def get(self, key: str, timestamp: int) -> str:
    #     if key not in self.store:
    #         return ""

    #     timeline = self.store[key]

    #     l, r = 0, len(timeline) - 1

    #     while l <= r:
    #         m = l + (r - l) // 2

    #         if timeline[m][0] > timestamp:
    #             r = m - 1
    #         else:
    #             l = m + 1

    #     return timeline[r][1] if r >= 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


class TestTimeMap(unittest.TestCase):
    def test_0(self):
        time_map = TimeMap()
        time_map.set("foo", "bar", 1)
        time_map.set("foo", "bar1", 2)
        time_map.set("hello", "world", 2)
        time_map.set("hello", "world 2", 5)
        self.assertEqual(time_map.get("foo", 1), "bar")
        self.assertEqual(time_map.get("foo", 3), "bar1")
        self.assertEqual(time_map.get("foo", 4), "bar1")
        self.assertEqual(time_map.get("foo", 5), "bar1")
        self.assertEqual(time_map.get("hello", 1), "")
        self.assertEqual(time_map.get("hello", 2), "world")
        self.assertEqual(time_map.get("hello", 3), "world")
        self.assertEqual(time_map.get("hello", 4), "world")
        self.assertEqual(time_map.get("hello", 5), "world 2")
        self.assertEqual(time_map.get("hello", 6), "world 2")
        self.assertEqual(time_map.get("hello", 7), "world 2")
