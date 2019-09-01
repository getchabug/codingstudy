

class HP:
    def __init__(self):
        self.hp=0
        self.damage=0
    def healpoint(self,hp,damage):
        self.hp=hp
        self.damage=damage
        r=hp-damage
        if r <= 0:
            print("문명하셨습니다.")
        else:
            return r
fey=HP()
a=fey.healpoint(70,600)
print(a)




























