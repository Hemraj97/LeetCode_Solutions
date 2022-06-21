#https://www.geeksforgeeks.org/design-and-implement-special-stack-data-structure/
#Understand use of super
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
 
class SpecialStack(MyStack):
 
  def __init__(self):
    super().__init__()
    self.Min = MyStack() 
 
  # SpecialStack's member method to
  # insert an element to it. This method
  # makes sure that the min stack is also
  # updated with appropriate minimum
  # values
  def push(self, x):
 
    if self.isEmpty():
      super().push(x)
      self.Min.push(x)
    else:
      super().push(x)
      y = self.Min.pop()
      self.Min.push(y)
      if x <= y:
        self.Min.push(x)
      else:
        self.Min.push(y) 
 
  # SpecialStack's member method to 
  # remove an element from it. This
  # method removes self.top element from
  # min stack also.
  def pop(self):
 
    x = super().pop()
    self.Min.pop()
    return x 
 
  # SpecialStack's member method
  # to get minimum element from it.
  def getmin(self):
 
    x = self.Min.pop()
    self.Min.push(x)
    return x
 
# Driver code
if __name__ == '__main__':
   
  s = SpecialStack()
  s.push(10)
  s.push(20)
  s.push(30)
  print(s.getmin())
  s.push(5)
  print(s.getmin())
