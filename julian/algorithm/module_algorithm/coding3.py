#-*- coding: utf-8 -*-
num_list = [1,2,3,4,5,6,7]#리스트 설정

def search_list(num_list, want_num):#
    for idx_number, value_number in enumerate(num_list):#리스트  num_list의모든값을 차례로
        if want_num == value_number:#리스트에 찾는갌이 있다
            return idx_number#위치를 돌려준다

    return -1 #끝까지 비교해도 없으면 -1

print("Match Index = %s" %(search_list(num_list, 7)))#
