class Calculator:
	def __init__(self,a,b,c,d,e):
		 self.a = a 
		 self.b = b
		 self.c = c 
		 self.d = d
		 self.e = e


	def sum(self):
		result = self.a + self.b + self.c + self.d + self.e
		return result

	def avg(self):
		result = (self.a * self.b * self.c * self.d * self.e)/5
		return result

cal = Calculator(1,2,3,4,5)
print(cal.sum())
print(cal.avg())










