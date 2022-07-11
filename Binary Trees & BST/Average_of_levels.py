#https://leetcode.com/problems/average-of-levels-in-binary-tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        lvl = [root]
        while lvl:
            ans.append(sum(n.val for n in lvl) / float(len(lvl)))
            lvl = [c for n in lvl for c in [n.left, n.right] if c]
        return ans