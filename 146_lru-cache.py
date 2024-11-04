import unittest


class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def unlink(self):
        self.prev.next = self.next
        self.next.prev = self.prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hash = {}

    def get(self, key: int) -> int:
        if key in self.hash:
            node = self.hash[key]
            node.unlink()
            self.enqueue(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            node = self.hash[key]
            node.val = value
            node.unlink()
            self.enqueue(node)
        else:
            self.length += 1
            node = Node(key, value)
            self.hash[key] = node
            self.enqueue(node)

            if self.length > self.capacity:
                self.dequeue()
                self.length -= 1

    def dequeue(self):
        node = self.head.next
        key = node.key
        del self.hash[key]
        node.unlink()

    def enqueue(self, node: Node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node


class TestLRUCache(unittest.TestCase):
    def test(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)
        cache.put(4, 4)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
