"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/description/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""

from itertools import groupby


class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        arr = groupby(word)

        ans = []

        count = 0

        for i, j in arr:
            ans.append([i, list(j)])

        for i in range(len(ans) - 4):
            if (
                ans[i][0] == "a"
                and ans[i + 1][0] == "e"
                and ans[i + 2][0] == "i"
                and ans[i + 3][0] == "o"
                and ans[i + 4][0] == "u"
            ):
                count = max(
                    count,
                    len(ans[i][1])
                    + len(ans[i + 1][1])
                    + len(ans[i + 2][1])
                    + len(ans[i + 3][1])
                    + len(ans[i + 4][1]),
                )

        return count


solution = Solution()
print(solution.longestBeautifulSubstring("aeeeiiooouuuaeiou"))
