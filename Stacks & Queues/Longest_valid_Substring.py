#https://www.geeksforgeeks.org/length-of-the-longest-valid-substring/
class MyStack:
	def __init__(self):
		self.stack = []
		self.top = -1
		self.max = 100

	def isEmpty(self):
		if self.top == -1:
			return True
		else: return False

	def isFull(self):
		if self.top >= self.max:
			return True
		else: return False

	def push(self,ele):
		if self.isFull():
			print("Stack Overflow")
			return
		else:
			self.top += 1
			self.stack.append(ele)
			return

	def pop(self):
		if self.isEmpty():
			print("Stack Underflow")
			return
		else:
			val = self.stack.pop()
			self.top -= 1
			return val

	def stacktop(self):
		if self.isEmpty():
			print("Stack Underflow")
			return
		else: return self.stack[self.top] 

	def evaluate_substr(self,s):
		max_substr = 0
		# print("inside")
		self.push(-1)
		for i in range(len(s)):
			# print("inside")
			if s[i] == '(':
				self.push(i)
			elif s[i] == ')' and self.isEmpty() != True:
				self.pop()
				if self.isEmpty() != True:
					max_substr = max(i-self.stacktop(),max_substr)
			elif self.isEmpty() == True:
				self.push(i)
		return max_substr	


if __name__ == "__main__":
	A = MyStack()
	s = "()((())"
	print(A.evaluate_substr(s))
