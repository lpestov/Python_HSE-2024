"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/construct-k-palindrome-strings/description/
"""


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        if len(s) > k:
            odd = 0
            for i in set(s):
                if s.count(i) % 2 != 0:
                    odd += 1
            if odd > k:
                return False
            return True
        return False


solution = Solution()
print(solution.canConstruct("abc", 3))
