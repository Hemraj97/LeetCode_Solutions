#https://leetcode.com/problems/decode-string
#Think of recursive way to do this
class Solution:
    def decodeString(self, s: str) -> str:
        l = list(s)
        stack, curNum, curString = [],0,''
        for i in range(len(l)):
            if l[i].isdigit():
                curNum = curNum*10 + int(l[i])
            if l[i].isalpha():
                curString += l[i]
            if l[i] == '[':
                stack += [curString,curNum]
                curString = ''
                curNum = 0
            if l[i] == ']':
                if stack:
                    num = stack.pop()
                    prev = stack.pop()
                    curString = prev + curString*num
        return curString