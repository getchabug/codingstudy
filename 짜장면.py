class HARIBO:
	lastname = "하리보"
	def __init__(self,name):
		self.fullname = self.lastname + name
	def noodle(self,eat):
		print("%s,%s을 먹다."% (self.fullname, eat))
	def	coding(self,study):
		print("%s,%s수업을 하다."%(self.fullname, study))

pey = HARIBO("3세")
pey.noodle("짜장면")
pey.coding("코딩")			