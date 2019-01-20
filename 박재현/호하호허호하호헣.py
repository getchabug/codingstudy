class Game:
	lastname = "오버"
	def __init__(self,name):
		self.fullname=self.lastname + name		
	def geonjang (self,where):
		print("%s,%s에 오신것을 환영합니다"%(self.fullname,where))
	def hero (name,choice):
		print("%s,%s선택"%(name,choice))
	def kill (name,eman):
		print("%s,%s처치"%(name,eman))
	def die (name,eman):
		print("%s,%s에게죽음"%(name,eman))
	def nodie(name,hi):
		print("%s,%s에게 부활됨"%(name,hi)

# pey = Game("워치")
pey.geonjang("리장 정원")
pey.hero("리퍼")
pey.kill("미카엘 2007 ,숨겨진트롤")
pey.die("김재원")
pey.nodie("미카엘2007,영웅은 죽지않아요")
