#https://leetcode.com/problems/longest-repeating-character-replacement/
#Sliding Window Problem
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_size = -1
        l = 0
        count = dict()
        res = 0
        max_freq = 0
        for r,ch in enumerate(s):
            if r == len(s):
                return res
            count[ch] = 1 + count.get(ch,0) 
            max_freq = max(count.values())
            if ((r - l + 1) - max_freq) <= k:
                res = max(res,r-l+1)
            else:
                count[s[l]] -= 1
                l += 1
        return res