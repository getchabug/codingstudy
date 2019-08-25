num_list = [1,2,3,4,5,6,7]#num_list는 1,2,3,4,5,6,7
def search_list(num_list,want_num):
    for idx_number,value_number in enumerate(num_list):#리스트 num_list의모든값을 차례로
        if want_num == value_number:#만약 want_num과value_number이같다면
            return idx_number#위치를 출력
    return -1#끝까지 비교해도 없으면 -1을출력
print("Match Index = %s"%(search_list(num_list,7)))