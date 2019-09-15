unsorted_list = [20,2,5,76,1]
sorted_list=[]
def sorting():
    for idx_list,value_list in enumerate(unsorted_list):
        min_value = min(unsorted_list)
        if value_list == min_value:
            sorted_list.append(value_lista)
            unsorted_list.pop(idx_list)
while(unsorted_list):
    sorting()
print(unsorted_list)
print(sorted_list)