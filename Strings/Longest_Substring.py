#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        res = 0
        seq = dict()
        while right < len(s):
            if s[right] in seq.keys():
                seq[s[right]] += 1
            else:
                seq[s[right]] = 1
            
            
            while seq[s[right]] > 1:
                seq[s[left]] -= 1
                left += 1
                
            right += 1
            res =  max(res,right - left)
        return res