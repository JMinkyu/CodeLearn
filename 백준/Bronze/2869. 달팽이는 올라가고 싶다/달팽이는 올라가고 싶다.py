import math
# A, B, V 변수 받기
A, B, V = map(int, input().split())

day = math.ceil((V-A)/(A-B)) + 1

print(day)