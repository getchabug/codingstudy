#-*- coding: utf-8 -*-
class HousePark:
	lastname ="박"
	def __init__(self, name):#초기화
			self.fullname = self.lastname +name
	def travel(self, where):#여행
		print("%s, %s여행을가다."%(self.fullname,where))
	def love(self,other):#사랑
		print("%s, %s 사랑에 빠졌네"%(self.fullname,other.fullname))
	def fight(self, other):#싸움
		print("%s, %s 싸우네"%(self.fullname, other.fullname))
	def __add__(self, other):#더하다
		print("%s, %s 결혼했네"%(self.fullname, other.fullname))
	def __sub__(self,other):#이혼
		print("%s, %s 이혼했네"%(self.fullname, other.fullname))
class HouseKim(HousePark):
	lastname = "김"
	def travel(self, where, day):#여행2
		print("%s, %s여행 %d일가네." % (self.fullname, where,day))
pey = HousePark("응용")
juilet = HouseKim("줄리엣")
pey.travel("부산")
juilet.travel("부산",3)
pey.love(juilet)
pey + juilet
pey.fight(juilet)
pey - juilet