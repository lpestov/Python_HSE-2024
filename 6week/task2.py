"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/repeated-dna-sequences/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""

from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        sequences = {}
        for i in range(len(s) - 9):
            sequence = s[i : i + 10]
            sequences[sequence] = sequences.get(sequence, 0) + 1

        return [sequence for sequence, count in sequences.items() if count > 1]


solution = Solution()
print(
    solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
)  # ["AAAAACCCCC", "CCCCCAAAAA"]
