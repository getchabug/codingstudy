


class game:
    def __init__(self):
        self.power=0
        self.defence=0

    def baseball(self,power,defence):
        self.power=power
        self.defence=defence
        if power > defence:
            r=("홈런입니다")
            return r
        elif power < defence:
            r=("스트라이크!!")
            return r
        elif power == defence:
            r=("무승부!!")
            return r
fey=game()
t=fey.baseball(4,5)
print(t)




































