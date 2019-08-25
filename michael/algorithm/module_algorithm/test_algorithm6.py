list_name = ['Tom', 'Jarry', 'Tom', 'Mark']
duplicate_name = list()
for idx_list,name_list in enumerate(list_name):
    for idx_list2, name_list2 in enumerate(list_name):
        if idx_list==idx_list2:
            continue
        elif name_list == name_list2:
            duplicate_name.append(name_list2)
print(set(duplicate_name))