from itertools import product
from typing import List

"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=problem-list-v2&envId=string
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []

        for digit in digits:
            result.append(mapping[digit])

        return ["".join(comb) for comb in product(*result)]


solution = Solution()

print(
    solution.letterCombinations("23")
)  # ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
