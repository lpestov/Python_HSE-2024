"""
leetcode.com/problem-list/array
url: https://leetcode.com/problems/pancake-sorting/description/?envType=problem-list-v2&envId=array&favoriteSlug=&difficulty=MEDIUM
"""

from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        n = len(arr)

        for i in range(n - 1, -1, -1):
            max_ind = i
            for j in range(i, -1, -1):
                if arr[j] > arr[max_ind]:
                    max_ind = j
            if max_ind != i:
                arr[: max_ind + 1] = arr[: max_ind + 1][::-1]
                result.append(max_ind + 1)
                arr[: i + 1] = arr[: i + 1][::-1]
                result.append(i + 1)
        return result


solution = Solution()
print(solution.pancakeSort([3, 2, 1]))  # [1, 3]
