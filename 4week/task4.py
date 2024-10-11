"""
leetcode.com/problem-list/array
url: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/?envType=problem-list-v2&envId=array&difficulty=MEDIUM
"""

from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_num = min(nums)
        return sum([num - min_num for num in nums])


solution = Solution()
print(solution.minMoves([1, 2, 3]))  # 3
