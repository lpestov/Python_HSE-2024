"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/minimum-size-subarray-sum/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        sum = 0
        ans = n + 1

        for i in range(n):
            sum += nums[i]
            while sum >= target:
                ans = min(ans, i - left + 1)
                sum -= nums[left]
                left += 1

        return 0 if ans == n + 1 else ans


solution = Solution()
print(solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # 2
