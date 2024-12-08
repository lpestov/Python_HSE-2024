"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/submissions/1473575693/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Optional:
    pass


class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, total):
            if not node:
                return total
            node.val += dfs(node.right, total)
            return dfs(node.left, node.val)

        dfs(root, 0)
        return root
