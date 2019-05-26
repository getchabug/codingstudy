class game:
	def __init__(self):
		self.result = 0

	def gop(self, num):
		self.result *= num
		return self.result


cal1 = game()
cal2 = game()

print(cal1.gop(3))
print(cal1.gop(4))
print(cal2.gop(3))
print(cal2.gop(7))