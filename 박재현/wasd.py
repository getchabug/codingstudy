class eat:
	lastname="미카엘"
	def __init__(self,name):
		self.fullname=self.lastname+name
	def eat(self,eat):
		print("%s,%s먹다"%(self.fullname,eat))
	def full(self,eat):
		print("%s,%s를 먹고 배부르다"%(self.fullname,eat)) 
pey = eat("2007")
pey.eat("짜장면")
pey.full("짜장면")