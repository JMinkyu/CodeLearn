A = int(input())
B = int(input())
C = int(input())
result = list(str(A * B * C)) 
for i in range(0, 10) :
    print(result.count(f'{i}'))