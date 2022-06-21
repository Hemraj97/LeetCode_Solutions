#https://www.geeksforgeeks.org/stack-set-4-evaluation-postfix-expression/
class Solution:
	def EvaluatePostfix(self,postfix):
		stack = list()
		for i in postfix:
			if i.isdigit():
				stack.append(i)
			else:
				a = stack.pop()
				b = stack.pop()
				stack.append(eval(str(b) + i + str(a))) 
		return stack[0]

if __name__ == "__main__":
	A = Solution()
	postfix = "231*+9-"
	print(A.EvaluatePostfix(postfix))
