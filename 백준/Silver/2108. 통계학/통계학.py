import sys

def input():
    return sys.stdin.readline().strip()

N = int(input())
lst = []

for _ in range(N):
    num = int(input())
    lst.append(num)

lst_sorted = sorted(lst)

# 산술평균
avg = round(sum(lst)/len(lst))

# 중앙값
median = lst_sorted[N//2]

# 최빈값
count_dict = {}
for num in lst:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

max_count = max(count_dict.values())

# 최빈값들 찾기
modes = []
for num, count in count_dict.items():
    if count == max_count:
        modes.append(num)

# 최빈값이 여러 개일 경우 두 번째로 작은 값, 아니면 그냥 최빈값 출력
mode = sorted(modes)[1] if len(modes) > 1 else modes[0]

# 범위
value_range = max(lst) - min(lst)

print(avg)
print(median)
print(mode)
print(value_range)