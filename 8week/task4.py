"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/jump-game-vii/description/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False] * n
        dp[0] = True
        pre = 0
        for i in range(1, n):
            if i >= minJump and dp[i - minJump]:
                pre += 1
            if i > maxJump and dp[i - maxJump - 1]:
                pre -= 1
            dp[i] = pre > 0 and s[i] == "0"
        return dp[-1]


solution = Solution()
print(solution.canReach("011010", 2, 3))  # True
