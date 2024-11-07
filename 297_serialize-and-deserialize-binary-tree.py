import unittest


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        res = []
        stack = []
        curr = root

        while curr or stack:
            if curr:
                res.append(str(curr.val))
                stack.append(curr.right)
                curr = curr.left
            else:
                res.append("N")
                curr = stack.pop()

                if curr is None and not stack:
                    # For not missing the last "N" in the result
                    res.append("N")
        return ",".join(res)

    def deserialize(self, data):
        if not data:
            return None

        values = data.split(",")
        index = 0

        def dfs():
            nonlocal index
            if values[index] == "N":
                index += 1
                return None
            node = TreeNode(int(values[index]))
            index += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


class TestSolution(unittest.TestCase):
    def test_1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        s = Codec()
        res = s.serialize(root)
        assert res == "1,2,N,N,3,4,N,N,5,N,N"
        tree = s.deserialize(res)
        print(tree.val)
        print(tree.left.val)
        print(tree.right.val)
        assert tree.val == 1
        assert tree.left.val == 2
        assert tree.right.val == 3
        assert tree.right.left.val == 4
        assert tree.right.right.val == 5

    def test_2(self):
        root = None
        s = Codec()
        res = s.serialize(root)
        assert res == ""
        tree = s.deserialize(res)
        assert tree is None
