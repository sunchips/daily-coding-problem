import unittest
from typing import List


class C2:

    def __init__(self, input: List[int]):
        self.input = input

    def solve1(self) -> List[int]:
        """
        O(N) time. O(N) space.
        """
        prod = 1
        for num in self.input:
            prod *= num
        result = []
        for num in self.input:
            result.append(int(prod / num))
        return result

    def solve2(self) -> List[int]:
        """
        O(N) time. O(N) space. No division.
        """
        prefix_prod = []
        for num in self.input:
            if prefix_prod:
                prefix_prod.append(prefix_prod[-1] * num)
            else:
                prefix_prod.append(num)

        suffix_prod = []
        for num in reversed(self.input):
            if suffix_prod:
                suffix_prod.append(suffix_prod[-1] * num)
            else:
                suffix_prod.append(num)
        suffix_prod = list(reversed(suffix_prod))

        result = []
        for i in range(len(self.input)):
            if i == 0:
                result.append(suffix_prod[i + 1])
            elif i == len(self.input) - 1:
                result.append(prefix_prod[i - 1])
            else:
                result.append(prefix_prod[i - 1] * suffix_prod[i + 1])
        return result


class TestC2(unittest.TestCase):
    def test1(self):
        input = [1, 2, 3, 4, 5]
        output = [120, 60, 40, 30, 24]
        result1 = C2(input).solve1()
        result2 = C2(input).solve2()
        self.assertEquals(result1, output)
        self.assertEquals(result2, output)


if __name__ == "__main__":
    pass
