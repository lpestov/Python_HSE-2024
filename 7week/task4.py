"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/fruit-into-baskets/description/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""

from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        left = 0
        count = {}
        max_fruits = 0

        for right in range(n):
            count[fruits[right]] = count.get(fruits[right], 0) + 1

            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits


solution = Solution()
print(solution.totalFruit([1, 2, 1]))  # 3
