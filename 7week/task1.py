"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/swap-for-longest-repeated-character-substring/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""

from collections import Counter


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        counter = Counter(text)
        n = len(text)
        groups = []
        max_length = 0

        i = 0
        while i < n:
            char = text[i]
            j = i
            while j < n and text[j] == char:
                j += 1
            groups.append((char, j - i))
            i = j

        for k, (char, length) in enumerate(groups):
            max_length = max(max_length, length)

            if (
                k > 0
                and k < len(groups) - 1
                and groups[k - 1][0] == groups[k + 1][0]
                and length == 1
            ):
                combined_length = groups[k - 1][1] + groups[k + 1][1]
                if combined_length < counter[groups[k - 1][0]]:
                    combined_length += 1
                max_length = max(max_length, combined_length)

            if length < counter[char]:
                max_length = max(max_length, length + 1)

        return max_length


solution = Solution()
print(solution.maxRepOpt1("aaabaaa"))
