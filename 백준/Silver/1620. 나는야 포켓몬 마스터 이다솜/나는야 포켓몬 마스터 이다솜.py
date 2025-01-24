import sys

def input():
    return sys.stdin.readline().strip()

N, M  = map(int,input().split())
num_to_poke = {}
poke_to_num = {}

for i in range(1, N+1) :
    A = input()
    num_to_poke[i] = A
    poke_to_num[A] = i

for _ in range(M) :
    B = input()
    if B.isdigit() == True :
        print(num_to_poke[int(B)])
    else :
        print(poke_to_num[B])