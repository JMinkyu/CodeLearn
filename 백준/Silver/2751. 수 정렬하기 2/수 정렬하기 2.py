import sys

def input() :
    return sys.stdin.readline().strip()

N = int(input())
lst = []

for _ in range(N) :
    N = int(input())
    lst.append(N)

lst.sort()

for x in lst :
    print(x)