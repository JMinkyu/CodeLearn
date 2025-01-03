value_list = []
for i in range(0, 10):
    num = int(input())
    num_value = num%42
    if num_value not in value_list :
        value_list.append(num_value)

print(len(value_list))