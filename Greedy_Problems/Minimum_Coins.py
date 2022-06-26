#https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/
class Solution():
	def min_coins(self, rs, ch):
		rs.sort(reverse = True)
		no_of_coins, count = 0, 0
		while count < len(rs) and ch != 0:
			if ch - rs[count] >= 0:
				ch -= rs[count]
				no_of_coins += 1
			else:
				count += 1
		if count < len(rs):
			return no_of_coins
		else: return -1

if __name__ == "__main__":
	A = Solution()
	rs = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
	ch = 121
	print(A.min_coins(rs,ch))
