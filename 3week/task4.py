"""
leetcode.com/problem-list/array
url: https://leetcode.com/problems/rotate-image/description/?envType=problem-list-v2&envId=array&favoriteSlug=&difficulty=MEDIUM
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()


solution = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution.rotate(matrix)
