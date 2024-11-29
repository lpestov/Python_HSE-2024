"""
leetcode.com/problem-list/sliding-window/
url:https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""


class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        double_s = s + s
        pattern1 = []
        pattern2 = []
        for i in range(2 * n):
            if i % 2 == 0:
                pattern1.append("0")
                pattern2.append("1")
            else:
                pattern1.append("1")
                pattern2.append("0")

        mismatch1 = [0] * (2 * n)
        mismatch2 = [0] * (2 * n)
        for i in range(2 * n):
            if double_s[i] != pattern1[i]:
                mismatch1[i] = 1
            if double_s[i] != pattern2[i]:
                mismatch2[i] = 1

        prefix1 = [0] * (2 * n + 1)
        prefix2 = [0] * (2 * n + 1)
        for i in range(2 * n):
            prefix1[i + 1] = prefix1[i] + mismatch1[i]
            prefix2[i + 1] = prefix2[i] + mismatch2[i]

        min_flips = float("inf")

        for i in range(n, 2 * n + 1):
            flips1 = prefix1[i] - prefix1[i - n]
            flips2 = prefix2[i] - prefix2[i - n]
            min_flips = min(min_flips, flips1, flips2)

        return min_flips


solution = Solution()
print(solution.minFlips("111000"))  # 2
