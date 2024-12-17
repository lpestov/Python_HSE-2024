"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque([root])
        flag = True
        while q:
            ans.append(
                [node.val for node in q] if flag else [node.val for node in q[::-1]]
            )
            flag = not flag
            q = [child for node in q for child in (node.left, node.right) if child]
        return ans
