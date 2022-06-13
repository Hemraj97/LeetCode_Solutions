#https://www.geeksforgeeks.org/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/
class Solution:
	def biggest_number(self, arr):
		l = len(str(max(arr))) + 1
		exval = list()
		ans = ''
		for i in range(len(arr)):
			x = str(arr[i]) * l
			exval.append((x[:l:],arr[i]))
		exval.sort(reverse = True)
		#print(f"exval {exval}")
		for i in range(len(exval)):
			ans += str(exval[i][1])
		return ans
		

if __name__ == "__main__":
	A = Solution()
	arr = [54, 546, 548, 60]
	res = A.biggest_number(arr)
	print(res)