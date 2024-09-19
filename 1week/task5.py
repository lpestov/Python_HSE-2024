"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/custom-sort-string/description/
"""


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        return "".join(
            sorted(s, key=lambda x: order.index(x) if x in order else len(order))
        )


solution = Solution()
print(solution.customSortString("cba", "abcd"))  # cbad
