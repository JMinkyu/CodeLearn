import sys

def input() :
    return sys.stdin.readline()

N = int(input())

member_list = []

for n in range(N) :
    a, b = input().split()
    member_list.append((int(a), b, n))

member_sort = sorted(member_list, key = lambda x : (x[0], x[2]))

for i in range(N) :
    print(f"{member_sort[i][0]} {member_sort[i][1]}")