#https://www.geeksforgeeks.org/convert-sentence-equivalent-mobile-numeric-keypad-sequence/
class Solution:
	def keypad_sequence(self,s):
		res = ""
		str_key = [	"2", "22", "222",
       			"3", "33", "333",
       			"4", "44", "444",
       			"5", "55", "555",
       			"6", "66", "666",
       			"7", "77", "777", "7777",
       			"8", "88", "888",
       			"9", "99", "999", "9999" ]
		for i in s:
			if i == " ":
				res = res + '0'
			else:
				position = ord(i) - ord('A')
				res = res + str_key[position]
		return res
		
if __name__ == "__main__":
	A = Solution()
	s = "GEEKSFORGEEKS"
	print(A.keypad_sequence(s))



