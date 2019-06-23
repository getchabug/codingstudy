from collections import Counter
test_dict = dict(Counter(["Tom","Jerry","Mike","Tom"]))
keys = list(test_dict.keys())
values = list(test_dict.values())
#print(values)
for value_idx, value_count in enumerate(values):
    #print(value_idx)
    #print(value_count)
    if value_count > 1:
        print(keys[value_idx])





