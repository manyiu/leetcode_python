import unittest


class Trie:

    def __init__(self):
        self.children = {}
        self.end = False

    def insert(self, word: str) -> None:
        curr = self

        while word:
            c = word[0]

            if c not in curr.children:
                curr.children[c] = Trie()
            if len(word) == 1:
                curr.children[c].end = True

            curr = curr.children[c]
            word = word[1:]

    def search(self, word: str) -> bool:
        curr = self

        while word:
            c = word[0]

            if c not in curr.children or (
                len(word) == 1 and curr.children[c].end != True
            ):
                return False
            elif len(word) == 1 and curr.children[c].end == True:
                return True

            curr = curr.children[c]
            word = word[1:]

    def startsWith(self, prefix: str) -> bool:
        curr = self

        while prefix:
            c = prefix[0]

            if c not in curr.children:
                return False

            curr = curr.children[c]
            prefix = prefix[1:]

        return True


class TestSolution(unittest.TestCase):

    def test_solution(self):
        obj = Trie()

        obj.insert("apple")
        self.assertTrue(obj.search("apple"))
        self.assertFalse(obj.search("app"))
        self.assertTrue(obj.startsWith("app"))
        obj.insert("app")
        self.assertTrue(obj.search("app"))


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
