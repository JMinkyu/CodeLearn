import sys

def input() :
    return sys.stdin.readline()

N = int(input())
A = list(map(int, input().split()))
B = [i /max(A)*100 for i in A]
print(sum(B)/len(B))