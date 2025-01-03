N, X = map(int,input().split())
list_num = list(map(int, input().split()))

for i in range(len(list_num)) :
    if list_num[i] < X :
        print(list_num[i], end= " ")