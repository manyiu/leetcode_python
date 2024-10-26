import unittest


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0 or val < self.min_stack[len(self.min_stack) - 1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[len(self.min_stack) - 1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.min_stack[len(self.min_stack)-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class TestMinStack(unittest.TestCase):
    def test(self):
        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)
        self.assertEqual(minStack.getMin(), -3)
        minStack.pop()
        self.assertEqual(minStack.top(), 0)
        self.assertEqual(minStack.getMin(), -2)
        minStack.pop()
        minStack.pop()
        minStack.push(1)
        self.assertEqual(minStack.top(), 1)
        self.assertEqual(minStack.getMin(), 1)