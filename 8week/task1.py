"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        left = 0
        min_queue = []
        max_queue = []
        max_length = 0

        for right in range(n):
            while min_queue and nums[right] < min_queue[-1]:
                min_queue.pop()
            min_queue.append(nums[right])

            while max_queue and nums[right] > max_queue[-1]:
                max_queue.pop()
            max_queue.append(nums[right])

            while max_queue[0] - min_queue[0] > limit:
                if nums[left] == min_queue[0]:
                    min_queue.pop(0)
                if nums[left] == max_queue[0]:
                    max_queue.pop(0)
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length


solution = Solution()
print(solution.longestSubarray([8, 2, 4, 7], 4))  # 2
