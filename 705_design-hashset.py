import unittest


class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None


class MyHashSet:
    def __init__(self):
        self.set = [ListNode(0) for _ in range(10**4)]

    def add(self, key: int) -> None:
        index = key % len(self.set)
        cur = self.set[index]

        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next

        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = key % len(self.set)
        cur = self.set[index]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        index = key % len(self.set)
        cur = self.set[index]

        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next

        return False


class TestMyHashSet(unittest.TestCase):
    def test_1(self):
        hashSet = MyHashSet()
        hashSet.add(1)
        hashSet.add(2)
        self.assertEqual(hashSet.contains(1), True)
        self.assertEqual(hashSet.contains(3), False)
        hashSet.add(2)
        self.assertEqual(hashSet.contains(2), True)
        hashSet.remove(2)
        self.assertEqual(hashSet.contains(2), False)
