#-*- coding: utf-8
class Haribo:
	lastname = "하리보"
	def __init__(self, name):
		self.fullname=self.lastname +name
	def game(self,play):
		print("%s,%s게임을 시작 "%(self.fullname,play))
	def TV(self,watch):
		print("%s,%s 티비를 보다"%(self.fullname,watch))
	def breakfast(self, eat):
		print("%s, %s 아침을 먹다"%(self.fullname,eat))

pey = Haribo("3세")
pey.game("오버워치")
pey.TV("MBC")
pey.breakfast("씨리얼")