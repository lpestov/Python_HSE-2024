"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/arithmetic-slices/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""

from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        count = 0
        start = 0

        while start < n - 2:
            diff = nums[start + 1] - nums[start]
            end = start + 2

            while end < n and nums[end] - nums[end - 1] == diff:
                count += 1
                end += 1

            start += 1

        return count


solution = Solution()
print(solution.numberOfArithmeticSlices([1, 2, 3, 4]))  # 3
