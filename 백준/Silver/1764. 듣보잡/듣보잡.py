import sys

def input() :
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

noname_list = set(input() for _ in range(N))
nosee_list = set(input() for _ in range(M))
nonamesee_list = sorted(noname_list & nosee_list)

print(len(nonamesee_list))
for name in nonamesee_list :
    print(name)