class Calculator:
	def __init__(self):
		self.result=0
	def adder(self,num):
		self.result+=num
		return self.result
#lucas
	def divide(self,num):
		self.result/=num
		return self.result 

	def jaegop(self,num):
		self.result**=num
		return self.result

	def multiply(self, num): #jisung 
		self.result*=num
		return self.resultn	

	def sub(self, num):#smart boy
		self.result-=num
		return self.result 
cal1=Calculator()
cal2=Calculator()
print(cal1.adder(3))
print(cal1.adder(4)) 
print(cal2.adder(3))
print(cal2.adder(7))
print(cal2.divide(5))
print(cal2.jaegop(3))
print(cal2.jaegop(7))
print(cal1.multiply(3))
print(cal1.multiply(4))
print(cal2.multiply(3))
print(cal2.multiply(7))
print("test")
print(cal1.sub(10))
print(cal1.sub(1))