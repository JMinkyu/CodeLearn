N = int(input())
S, M, L, XL, XXL, XXXL = map(int, input().split())
T_shirt_size = [S, M, L, XL, XXL, XXXL]
T, P = map(int, input().split())

list_T = []
for i in range(len(T_shirt_size)) :
    if T_shirt_size[i] % T != 0 :
        list_T.append(T_shirt_size[i]//T + 1)
    else :
        list_T.append(T_shirt_size[i]//T)
sum_T = sum(list_T)

p_bundle = N//P
p_part = N % P

print(sum_T)
print(f"{p_bundle} {p_part}")