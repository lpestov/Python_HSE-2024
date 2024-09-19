"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-palindromic-substring/description/?envType=problem-list-v2&envId=string
"""


class Solution:

    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s

        def palindrome(self, left, right) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        result = ""

        for i in range(len(s)):
            first = palindrome(self, i, i)
            second = palindrome(self, i, i + 1)
            result = max(result, first, second, key=len)
        return result


solution = Solution()
print(solution.longestPalindrome("babad"))  # bab
