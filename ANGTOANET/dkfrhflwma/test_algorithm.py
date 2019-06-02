#--*-- coding: utf--*--
#module_algorithn 디렉토리에서 만든 module__math.py의
#Math 클래스를 호출
from module_math import Math

#Math 클래스를 호출해서 calculate 변수로 받음
calculate=Math()

#Math클래스를 선언한 calculate 변수로 클래스 기능을 사용
print(calculate.sum_n(1000))
