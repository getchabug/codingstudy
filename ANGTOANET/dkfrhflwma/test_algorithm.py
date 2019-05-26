#-*- coding: utf-8 -*-
#module algorithm에서 만든 math.py의 Math 클래스를 호출
from module_math import Math
# Math 클래스 호출해서 calculate 변수로 받음
calculate=Math()
# Math 클래스를 선언한 calculate 변수로 클래서 기능을 사용
print (calculate.add_2param(1,2))
print (calculate.mul_2param(2,6))