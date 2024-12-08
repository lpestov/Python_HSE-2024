"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/submissions/1473575276/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Optional:
    pass


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, min_val, max_val):
            if not node:
                return max_val - min_val
            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)
            return max(
                dfs(node.left, min_val, max_val), dfs(node.right, min_val, max_val)
            )

        return dfs(root, root.val, root.val)
