"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/submissions/1465716956/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""


class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        min_len = [float("inf")] * n
        result = float("inf")

        left_sum, left_start = 0, 0
        for i in range(n):
            left_sum += arr[i]
            while left_sum > target:
                left_sum -= arr[left_start]
                left_start += 1
            if left_sum == target:
                min_len[i] = i - left_start + 1
            if i > 0:
                min_len[i] = min(min_len[i], min_len[i - 1])

        # Second pass: Find valid pairs using the right side
        right_sum, right_start = 0, n - 1
        for i in range(n - 1, -1, -1):
            right_sum += arr[i]
            while right_sum > target:
                right_sum -= arr[right_start]
                right_start -= 1
            if right_sum == target:
                right_len = right_start - i + 1
                if i > 0:
                    result = min(result, right_len + min_len[i - 1])

        return result if result != float("inf") else -1


arr = [3, 2, 2, 4, 3]
target = 3
sol = Solution()
print(sol.minSumOfLengths(arr, target))  # 2
