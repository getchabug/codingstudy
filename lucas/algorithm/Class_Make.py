

class shpoping:
    def __init__(self):
        self.have_money=0
        self.price=0
    def shop(self,have_money,price):
        self.have_money=have_money
        self.price=price
        total=have_money-price
        if price <= have_money:
            r=("감사합니다 호갱님,거스름돈은 %s입니다"%total)
            return r
        else:
            r=("돈도 없는게어디서 절로꺼져!!")
            return r
fey=shpoping()
a=fey.shop(7000,600)
print(a)




























