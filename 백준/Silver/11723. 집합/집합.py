import sys

S = []

def input() :
    return sys.stdin.readline()

def add(num) :
    if num in S : pass
    else : S.append(num)

def remove(num) :
    if num in S : S.remove(num)
    else : pass

def check(num) :
    if num in S : print(1)
    else : print(0)

def toggle(num) :
    if num in S : S.remove(num)
    else :  S.append(num)

N = int(input())

for i in range(N) :

    command = input().split()

    if len(command) == 1 :
        if command[0] == 'all' :
            S = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        elif command[0] == 'empty' :
            S = []
    else :
        A, B = command
        B = int(B)
        if A == 'add' :
            add(B)
        elif A == 'check' :
            check(B)
        elif A == 'remove' :
            remove(B)
        elif A == 'toggle' :
            toggle(B)