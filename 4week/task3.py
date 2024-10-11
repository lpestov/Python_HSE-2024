"""
leetcode.com/problem-list/array
url: https://leetcode.com/problems/find-all-duplicates-in-an-array/?envType=problem-list-v2&envId=array&difficulty=MEDIUM
"""

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            index = abs(num) - 1

            if nums[index] < 0:
                res.append(abs(num))
            else:
                nums[index] *= -1
        return res


solution = Solution()
print(solution.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))  # [2, 3]
