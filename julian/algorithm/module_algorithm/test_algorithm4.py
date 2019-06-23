from collections import Counter
test_dict = dict(Counter(["tom","jerry","tom","mike"]))
keys = list(test_dict.keys())
values = list(test_dict.values())
# print(values)
for value_idx, values_count in enumerate(values):
    # print(value_idx)
    # print(value_count)
    if values_count > 1:
        print(keys[value_idx])


from module_math import Math


test_class=Math()
a=['Tom','jerry','Mike','Tom']
print(test_class.every(a))