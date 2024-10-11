"""
leetcode.com/problem-list/array
url: https://leetcode.com/problems/find-and-replace-pattern/description/?envType=problem-list-v2&envId=array&difficulty=MEDIUM
"""

from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def matches(word: str) -> bool:
            w_to_p = {}
            p_to_w = {}

            for w, p in zip(word, pattern):
                if w not in w_to_p:
                    w_to_p[w] = p
                if p not in p_to_w:
                    p_to_w[p] = w

                if w_to_p[w] != p or p_to_w[p] != w:
                    return False

            return True

        return [word for word in words if matches(word)]


solution = Solution()
words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "abb"
print(solution.findAndReplacePattern(words, pattern))  # ['mee', 'aqq']
