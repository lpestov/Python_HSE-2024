"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/integer-to-roman/description/?envType=problem-list-v2&envId=hash-table&difficulty=MEDIUM
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        for value, symbol in [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]:
            while num >= value:
                num -= value
                roman += symbol
        return roman


solution = Solution()
print(solution.intToRoman(3))  # 'III
