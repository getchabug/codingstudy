sorted_list = [1,20,30,40,60,70]

search_list = 80

if search_list not in sorted_list:
    print(-1)
for idx_value, value in enumerate(sorted_list):
    if search_list == value:
        print(idx_value)


