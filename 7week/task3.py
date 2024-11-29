"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/grumpy-bookstore-owner/description/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""

from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        n = len(customers)

        base_satisfaction = 0
        for i in range(n):
            if grumpy[i] == 0:
                base_satisfaction += customers[i]

        additional_satisfaction = 0
        current_window_satisfaction = 0

        for i in range(n):
            if grumpy[i] == 1:
                current_window_satisfaction += customers[i]

            if i >= minutes:
                if grumpy[i - minutes] == 1:
                    current_window_satisfaction -= customers[i - minutes]

            additional_satisfaction = max(
                additional_satisfaction, current_window_satisfaction
            )

        return base_satisfaction + additional_satisfaction


solution = Solution()
print(
    solution.maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3)
)  # Output: 16
