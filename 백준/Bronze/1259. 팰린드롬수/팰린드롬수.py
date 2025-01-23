#팰린드롬수
import sys

def input() :
    return sys.stdin.readline()

while True :
    A = input()
    num = int(A)
    reverse_num = ''.join(map(str,list(A)[::-1]))
    if num == 0 :
        break
    elif num == int(reverse_num) :
        print('yes')
    else :
        print('no')