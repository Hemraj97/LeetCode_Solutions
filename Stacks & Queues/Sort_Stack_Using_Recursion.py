#https://www.geeksforgeeks.org/sort-a-stack-using-recursion/
class Solution:
	def sortstack(self, s):
		if len(s) != 0:
			temp = s.pop()
			self.sortstack(s)
			self.sortedinsert(s,temp)

	def sortedinsert(self, s, ele):
		if len(s) == 0 or ele > s[-1]:
			s.append(ele)
		else:
			temp = s.pop()
			self.sortedinsert(s, ele)
			s.append(temp)

if __name__ == "__main__":
	A = Solution()
	s = [1,3,2,4]
	A.sortstack(s)
	print(s)
