#https://leetcode.com/problems/valid-palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ''.join(ch for ch in s if ch.isalnum())
        if s_new.lower() == s_new.lower()[::-1]:
            return True
        else: return False