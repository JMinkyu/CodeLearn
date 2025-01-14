import sys

def input():
    return sys.stdin.readline().strip()

def int_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

N = int(input())  # 점수의 개수

# 점수 입력 받기
grade = [int(input()) for _ in range(N)]

# 점수 리스트 정렬
grade.sort()

# trim 값 계산 (15%)
trim = int_round(N * 0.15)

# trim이 0일 경우 전체 리스트를 사용하고, 그렇지 않으면 트리밍된 점수 사용
trimmed_grades = grade[trim: -trim] if trim > 0 else grade

# 빈 리스트인 경우를 방지하고 평균 계산
if len(trimmed_grades) > 0:
    print(int_round(sum(trimmed_grades) / len(trimmed_grades)))
else:
    print(0)  # 트리밍 후 리스트가 비었을 경우