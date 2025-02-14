import unittest


class ProductOfNumbers:

    def __init__(self):
        self.prefixProduct = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefixProduct = [1]
        else:
            self.prefixProduct.append(self.prefixProduct[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefixProduct):
            return 0

        return self.prefixProduct[-1] // self.prefixProduct[-(k + 1)]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)


class TestSolution(unittest.TestCase):
    def test_1(self):
        productOfNumbers = ProductOfNumbers()
        productOfNumbers.add(3)
        productOfNumbers.add(0)
        productOfNumbers.add(2)
        productOfNumbers.add(5)
        productOfNumbers.add(4)
        self.assertEqual(productOfNumbers.getProduct(2), 20)
        self.assertEqual(productOfNumbers.getProduct(3), 40)
        self.assertEqual(productOfNumbers.getProduct(4), 0)
        productOfNumbers.add(8)
        self.assertEqual(productOfNumbers.getProduct(2), 32)
