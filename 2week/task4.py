"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/palindrome-partitioning/description/
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(left: int, right: int) -> bool:
            return s[left : right + 1] == s[left : right + 1][::-1]

        def backtrack(start: int, path: List[str]):
            if start == len(s):
                res.append(path)
                return

            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    backtrack(end + 1, path + [s[start : end + 1]])

        res = []
        backtrack(0, [])
        return res


solution = Solution()
print(solution.partition("aab"))  # [["a","a","b"],["aa","b"]]
