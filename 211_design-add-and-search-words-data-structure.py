import unittest


class WordDictionary:

    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word: str) -> None:
        curr = self

        for c in word:
            if c not in curr.children:
                curr.children[c] = WordDictionary()
            curr = curr.children[c]

        curr.end = True

    def search(self, word: str) -> bool:
        curr = self

        for i in range(len(word)):
            if word[i] == ".":
                for child in curr.children:
                    if curr.children[child].search(word[i + 1 :]):
                        return True
                return False
            else:
                if word[i] not in curr.children:
                    return False
                curr = curr.children[word[i]]

        return curr.end


class TestSolution(unittest.TestCase):

    def test_solution(self):
        obj = WordDictionary()

        obj.addWord("bad")
        obj.addWord("dad")
        obj.addWord("mad")

        self.assertFalse(obj.search("pad"))
        self.assertTrue(obj.search("bad"))
        self.assertTrue(obj.search(".ad"))
        self.assertTrue(obj.search("b.."))
        self.assertFalse(obj.search("b..."))
        self.assertFalse(obj.search("b...."))

        obj = WordDictionary()
        obj.addWord("a")
        self.assertTrue(obj.search("."))


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
