"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-all-anagrams-in-a-string/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        p_counter = {}
        for char in p:
            p_counter[char] = p_counter.get(char, 0) + 1

        s_counter = {}
        for char in s[: len(p)]:
            s_counter[char] = s_counter.get(char, 0) + 1

        result = []
        for i in range(len(s) - len(p)):
            if s_counter == p_counter:
                result.append(i)

            s_counter[s[i]] -= 1
            if s_counter[s[i]] == 0:
                del s_counter[s[i]]

            s_counter[s[i + len(p)]] = s_counter.get(s[i + len(p)], 0) + 1

        if s_counter == p_counter:
            result.append(len(s) - len(p))

        return result


solution = Solution()
print(solution.findAnagrams("cbaebabacd", "abc"))  # [0, 6]
