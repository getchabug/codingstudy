num_list = [1,2,3,4,5,6,7]#num_list라는 함수에 [1,2,3,4,5,6,7]을 저장

def search_list(num_list, want_num):#num_list에 원하는 숫자가 있는지 찾는다
    for idx_number, value_number in enumerate(num_list):#num_list에 idx_number와 value_number를 센다
        if want_num == value_number:#만약 원하는 숫자가 value_number면
            return idx_number#idx_number를 입력하다

    return -1#끝까지 해도 없으면 -1을 한다

print("Match Index = %s" %(search_list(num_list, 7)))#num_list가 7인데 -1을 해야되므로 6이다