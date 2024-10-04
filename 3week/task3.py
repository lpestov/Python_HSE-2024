"""
leetcode.com/problem-list/array
url: https://leetcode.com/problems/maximum-subarray/description/?envType=problem-list-v2&envId=array&favoriteSlug=&difficulty=MEDIUM
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = max_sum = nums[0]
        for num in nums[1:]:
            max_sum = max(num, max_sum + num)
            res = max(res, max_sum)

        return res


solution = Solution()
print(solution.maxSubArray([-2, 10, -3, 4, -1, 2, 1, -5, 4]))  # 6
