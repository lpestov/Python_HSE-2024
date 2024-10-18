"""
leetcode.com/problem-list/array
url: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/?envType=problem-list-v2&envId=hash-table&difficulty=MEDIUM
"""

from typing import List


class Optional:
    pass


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        root_val = postorder.pop()
        root = TreeNode(root_val)

        root_idx = inorder.index(root_val)

        root.right = self.buildTree(inorder[root_idx + 1 :], postorder)
        root.left = self.buildTree(inorder[:root_idx], postorder)

        return root
