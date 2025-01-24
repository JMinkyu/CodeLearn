import sys

def input() :
    return sys.stdin.readline().strip()

N = int(input())

lst = []
lst = list(map(int, input().split()))

query = int(input())

print(lst.count(query))