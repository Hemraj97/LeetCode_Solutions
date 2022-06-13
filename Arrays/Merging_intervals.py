#https://www.geeksforgeeks.org/merging-intervals/
class Solution:
	def merging_intervals(self, arr):
		arr.sort(key = lambda x:x[0])
		res = list()
		for i in range(len(arr)-1):
			if arr[i][1] > arr[i+1][0]:
				if res:
					res.pop() 
				arr[i+1][0] = arr[i][0]
				arr[i+1][1] = arr[i][1] if arr[i][1] > arr[i+1][1] else arr[i+1][1]
				res.append(arr[i+1])
			else: 
				res.append(arr[i])
		return res 

if __name__ == "__main__":
	A = Solution()
	arr =  [[6, 8], [1, 9], [2, 4], [4, 7]] 
	print(A.merging_intervals(arr))
