unsort_list=[123,456,135]
sorted_list=[]
def sorting():
    for idx_list value_list in enumerate(unsort_list):
        min_value=min(unsort_list)
        if value_list==min_value:
            sort_list.append(value_list)
            unsort_list.pop(idx_list)

while unsort_list:
    sorting()

print(unsort_list)
print(sort_list)