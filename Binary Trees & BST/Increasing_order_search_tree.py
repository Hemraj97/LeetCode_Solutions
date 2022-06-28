#https://leetcode.com/problems/increasing-order-search-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        l = list()
        self.inorder(root, l)
        new_root = TreeNode(val=l[0])
        p = new_root
        for i in range(1,len(l)):
            new_root.right = TreeNode(val = l[i]) 
            new_root = new_root.right
        return p
            
    
    def inorder(self, root: TreeNode, l: List) -> TreeNode:
        if root is not None:
            self.inorder(root.left, l)
            l.append(root.val)
            self.inorder(root.right, l)
            
        