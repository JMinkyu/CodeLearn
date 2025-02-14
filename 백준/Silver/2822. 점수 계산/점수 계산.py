import sys

def input() :
    return sys.stdin.readline()

dic = {}
num_list = []
lst = []

for i in range(1, 9) :
    num = int(input())
    num_list.append(num)
    dic[i] = num

num_list.sort(reverse=True)

print(sum(num_list[:5]))

dic_sorted = sorted(dic.items(), key = lambda x : x[1],reverse=True)[:5]

for n in range(len(dic_sorted)) :
    lst.append(dic_sorted[n][0])
lst.sort()
for n in range(len(lst)) :
    if n != len(lst) :
        print(lst[n], end = ' ')
    else :
        print(lst[n])
