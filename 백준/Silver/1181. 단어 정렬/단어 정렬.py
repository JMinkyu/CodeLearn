import sys

def input() :
    return sys.stdin.readline().strip()
def len_test(*msg):
    return len(*msg)

N = int(input())
words = [input() for _ in range(N)]

A = list(set(words))
AL_A = sorted(A)
len_A = sorted(AL_A, key = len_test)

for text in len_A:
    print(text)
