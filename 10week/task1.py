"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/house-robber-iii/description/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            left, left_skip = dfs(node.left)
            right, right_skip = dfs(node.right)
            return node.val + left_skip + right_skip, max(left, left_skip) + max(
                right, right_skip
            )

        return max(dfs(root))
