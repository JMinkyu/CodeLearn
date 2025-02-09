N = int(input())
sum_N = 0
sum_N3 = 0 

for i in range(1, N+1) :
    sum_N += i
    sum_N3 += i*i*i

print(sum_N)
print(sum_N * sum_N)
print(sum_N3)