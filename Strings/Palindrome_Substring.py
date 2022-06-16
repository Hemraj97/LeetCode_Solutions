#https://leetcode.com/problems/palindromic-substrings
class Solution:
    def countSubstrings(self, s: str) -> int:
        count_pal = 0
        for i in range(len(s)):
            count_pal += self.check_palindrome(s,i,i)
            count_pal += self.check_palindrome(s,i,i+1)
        return count_pal
    
    def check_palindrome(self, s: str, l: int, r: int) -> int:
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count
        