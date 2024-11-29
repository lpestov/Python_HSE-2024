"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/fruit-into-baskets/description/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""

from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(k):
            if k < 0:
                return 0
            count = 0
            left = 0
            current_sum = 0

            for right in range(len(nums)):
                current_sum += nums[right]

                while current_sum > k:
                    current_sum -= nums[left]
                    left += 1

                count += right - left + 1

            return count

        return atMost(goal) - atMost(goal - 1)


solution = Solution()
print(solution.numSubarraysWithSum([1, 0, 1, 0, 1], 2))
