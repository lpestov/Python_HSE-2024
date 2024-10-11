"""
leetcode.com/problem-list/array
url: https://leetcode.com/problems/shuffle-an-array/description/?envType=problem-list-v2&envId=array&difficulty=MEDIUM
"""

import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums

    def reset(self) -> List[int]:
        return self.array

    def shuffle(self) -> List[int]:
        shuffled = list(self.array)
        random.shuffle(shuffled)
        return shuffled


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
