"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/count-number-of-nice-subarrays/description/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""


class Solution:
    def numberOfSubarrays(self, nums, k):
        def atMost(k):
            count = 0
            left = 0
            odd_count = 0

            for right in range(len(nums)):
                if nums[right] % 2 != 0:
                    odd_count += 1

                while odd_count > k:
                    if nums[left] % 2 != 0:
                        odd_count -= 1
                    left += 1

                count += right - left + 1

            return count

        return atMost(k) - atMost(k - 1)


solution = Solution()
print(solution.numberOfSubarrays([1, 1, 2, 1, 1], 3))
