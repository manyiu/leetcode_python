from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.root = root
        self.curr = root

    def next(self) -> int:
        while True:
            if self.curr:
                self.stack.append(self.curr)
                self.curr = self.curr.left
            else:
                node = self.stack.pop()
                self.curr = node.right
                return node.val

    def hasNext(self) -> bool:
        return self.curr is not None or len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


class TestBSTIterator(unittest.TestCase):
    def test_next(self):
        root = TreeNode(7)
        root.left = TreeNode(3)
        root.right = TreeNode(15)
        root.right.left = TreeNode(9)
        root.right.right = TreeNode(20)
        bst = BSTIterator(root)
        assert bst.next() == 3
        assert bst.next() == 7
        assert bst.hasNext() is True
        assert bst.next() == 9
        assert bst.hasNext() is True
        assert bst.next() == 15
        assert bst.hasNext() is True
        assert bst.next() == 20
        assert bst.hasNext() is False
