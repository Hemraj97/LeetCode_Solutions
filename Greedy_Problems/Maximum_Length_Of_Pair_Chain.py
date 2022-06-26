#https://leetcode.com/problems/maximum-length-of-pair-chain/
class Solution:
    def findLongestChain(self, pairs):
        N = len(pairs)
        pairs.sort(key = lambda x: x[1])
        ans = 0
        cur = -math.inf
        for head, tail in pairs:
            if head > cur:
                cur = tail
                ans += 1
        return ans