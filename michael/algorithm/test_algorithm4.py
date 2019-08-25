unsort_list=[5,3,8,1]
sort_list=[]
def sorting():
    min_value = min(unsort_list)
    for idx_list, value_list in enumerate(unsort_list):
        if value_list == min_value:
            sort_list.append(value_list)
            unsort_list.pop(idx_list)
while unsort_list:
    sorting()
print(sort_list)
print(unsort_list)