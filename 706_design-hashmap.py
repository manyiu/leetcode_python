import unittest

class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    def __init__(self):
        self.hash = [ListNode(0, 0) for _ in range(10**4)]

    def put(self, key: int, value: int) -> None:
        index = key % len(self.hash)
        curr = self.hash[index]

        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % len(self.hash)
        curr = self.hash[index]

        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        
        return -1

    def remove(self, key: int) -> None:
        index = key % len(self.hash)
        curr = self.hash[index]

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

class TestSolution(unittest.TestCase):
    def test_1(self):
        hashMap = MyHashMap()
        hashMap.put(1, 1)
        hashMap.put(2, 2)
        self.assertEqual(hashMap.get(1), 1)
        self.assertEqual(hashMap.get(3), -1)
        hashMap.put(2, 1)
        self.assertEqual(hashMap.get(2), 1)
        hashMap.remove(2)
        self.assertEqual(hashMap.get(2), -1)