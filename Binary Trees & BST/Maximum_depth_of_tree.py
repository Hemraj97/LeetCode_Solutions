#https://leetcode.com/problems/maximum-depth-of-n-ary-tree
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        most_depth = -1
        stack = [(root,1)]
        while stack:
            node, count = stack.pop()
            most_depth = max(most_depth,count)
            for child in node.children:
                stack.append((child,count+1))
        return most_depth