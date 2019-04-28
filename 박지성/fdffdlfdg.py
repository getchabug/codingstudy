class service:

	def __init__(self,name):
		self.name = name
	def sum(self,a,b):
		result = a + b
		print("%s야 %s + %s =%s란다."% (self.name,a,b,result))

pey = service("뚱이")
pey.sum(9999999999999,-877777777777777)	