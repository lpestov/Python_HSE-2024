"""
leetcode.com/problem-list/array
url: https://leetcode.com/problems/merge-intervals/description/?envType=problem-list-v2&envId=array&favoriteSlug=&difficulty=MEDIUM
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        res = []

        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])

        return res


solution = Solution()
print(solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # [[1,6],[8,10],[15,18]]
