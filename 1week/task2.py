"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/zigzag-conversion/description/?envType=problem-list-v2&envId=string
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ""
        if numRows == 1:
            return s

        rows = [""] * min(numRows, len(s))
        current = 0
        going_down = False

        for char in s:
            rows[current] += char
            if current == 0 or current == numRows - 1:
                going_down = not going_down
            if going_down:
                current += 1
            else:
                current -= 1

        for row in rows:
            result += row

        return result


solution = Solution()
print(solution.convert("PAYPALISHIRING", 3))  # PAHNAPLSIIGYIR
