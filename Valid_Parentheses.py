#https://leetcode.com/problems/valid-parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        l=list(s)
        c = list()
        for i in l:
            if i == '[' or i == '{' or i == '(':
                c.append(i)
            if i == ']' or i == ')' or i == '}':
                try:
                    if i == ']' and c.pop() != '[' or i == '}' and c.pop() != '{' or i == ')' and c.pop() != '(':
                        return False
                except: return False
        if len(c) == 0:
            return True
        else: return False