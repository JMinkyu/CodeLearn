import sys
def input():
    return sys.stdin.readline()

N, M = map(int, input().split())

tree_lst = list(map(int, input().split()))

left = 0
right = max(tree_lst)
answer = 0

while left <= right:
    mid = (left + right) // 2
    total = 0
    
    for tree in tree_lst :
        if tree > mid :
            total += tree - mid
    
    if total >= M :
        answer = mid
        left = mid + 1
    else :
        right = mid - 1
print(answer)
