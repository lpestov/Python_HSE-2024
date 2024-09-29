"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/palindromic-substrings/description/
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        def palindrome(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count

        res = 0
        for i in range(len(s)):
            res += palindrome(i, i)  # если 1 центр
            res += palindrome(i, i + 1)  # если 2 центра

        return res


solution = Solution()
print(solution.countSubstrings("abc"))  # 3
