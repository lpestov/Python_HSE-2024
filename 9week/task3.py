"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/smallest-string-starting-from-leaf/description/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Optional:
    pass


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, path):
            if not node:
                return
            path.append(chr(node.val + ord("a")))
            if not node.left and not node.right:
                paths.append("".join(reversed(path)))
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()

        paths = []
        dfs(root, [])
        return min(paths) if paths else ""
