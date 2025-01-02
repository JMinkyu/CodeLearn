my_list = []
n = int(input())
while n !=0 :
    my_list.append(n)
    try :
        n = int(input())
    except :
        break

print(max(my_list))
print(my_list.index(max(my_list))+1)