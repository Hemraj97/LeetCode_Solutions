#https://practice.geeksforgeeks.org/problems/consecutive-elements2306/1
class Solution:
	def repeat_consecutive(self, s):
		res = s
		for i in range(len(s)-1):
			if s[i] == s[i+1]:
				res = res[:i] + res[i+1:]
		return res

if __name__ == "__main__":
	A = Solution()
	s = "aabaa"
	print(A.repeat_consecutive(s))