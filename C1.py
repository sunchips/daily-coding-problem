import unittest
from bisect import bisect_left
from typing import List


class C1:

    def __init__(self, input: List[int], k: int):
        self.input = input
        self.k = k

    def solve1(self) -> bool:
        """
        O(N) time. O(N) space.
        """
        seen = set()
        for num in self.input:
            if self.k - num in seen:
                return True
            seen.add(num)
        return False

    def solve2(self) -> bool:
        """
        O(N log(N)) time. O(1) space.
        """
        self.input.sort()  # O(N log(N))

        for idx, num in enumerate(self.input):  # O(N)
            target = self.k - num
            bs_idx = bisect_left(self.input, target)
            if bs_idx != len(self.input) and self.input[bs_idx] == target:
                if bs_idx == idx:
                    # check if more exist to the right
                    if bs_idx + 1 < len(self.input) and self.input[bs_idx + 1]:
                        return True
                else:
                    return True
        return False


class TestC1(unittest.TestCase):
    def test1(self):
        input = [10, 15, 3, 7]
        target = 17
        result1 = C1(input, target).solve1()
        result2 = C1(input, target).solve2()
        self.assertTrue(result1)
        self.assertTrue(result2)

    def test2(self):
        input = [1, 3, 6, 7, 9]
        target = 10
        result1 = C1(input, target).solve1()
        result2 = C1(input, target).solve2()
        self.assertTrue(result1)
        self.assertTrue(result2)

    def test3(self):
        input = [3, 2, 4, 1, 9]
        target = 12
        result1 = C1(input, target).solve1()
        result2 = C1(input, target).solve2()
        self.assertTrue(result1)
        self.assertTrue(result2)

    def test4(self):
        input = []
        target = 10
        result1 = C1(input, target).solve1()
        result2 = C1(input, target).solve2()
        self.assertFalse(result1)
        self.assertFalse(result2)

    def test5(self):
        input = [1, 2]
        target = 9
        result1 = C1(input, target).solve1()
        result2 = C1(input, target).solve2()
        self.assertFalse(result1)
        self.assertFalse(result2)


if __name__ == "__main__":
    pass
