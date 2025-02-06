N, M = map(int,input().split())
lst_a = []
lst_b = []

for n in range(N) :
    a = list(map(int,input().split()))
    lst_a.append(a)

for n in range(N) :
    b = list(map(int,input().split()))
    lst_b.append(b)

for n in range(N) :
    for m in range(M) :
        if m != M :
            print(lst_a[n][m] + lst_b[n][m], end= ' ')
        else :
            print(lst_a[n][m] + lst_b[n][m])
    print()      