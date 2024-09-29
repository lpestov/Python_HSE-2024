"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/score-of-parentheses/description/
"""


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for c in s:
            if c == "(":
                stack.append(0)
            else:
                last = stack.pop()
                stack[-1] += max(2 * last, 1)
        return stack[0]


solution = Solution()
print(solution.scoreOfParentheses("(()(()))"))  # 6
