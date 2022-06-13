#https://www.geeksforgeeks.org/chocolate-distribution-problem/
#sort using quicksort
class Solution:
	def chocolate_distribution(self, arr, m):
		arr.sort()
		min_diff = arr[len(arr)-1] - arr[0]
		for i in range(len(arr)-m+1):
			diff = arr[i+m-1] - arr[i]
			min_diff = min(diff,min_diff)
		return min_diff

if __name__ == "__main__":
	a = Solution()
	arr = arr = [12, 4, 7, 9, 2, 23, 25, 41,
          30, 40, 28, 42, 30, 44, 48,
          43, 50]
	m = 7
	res = a.chocolate_distribution(arr,m)
	print(res)

