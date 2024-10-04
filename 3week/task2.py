"""
leetcode.com/problem-list/array
url: https://leetcode.com/problems/spiral-matrix/description/?envType=problem-list-v2&envId=array&favoriteSlug=&difficulty=MEDIUM
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        res = []
        m, n = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, n - 1, 0, m - 1

        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res


solution = Solution()
print(solution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # [1,2,3,6,9,8,7,4,5]
