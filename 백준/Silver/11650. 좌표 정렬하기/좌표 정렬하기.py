import sys

def input() :
    return sys.stdin.readline().strip()

N = int(input())

location = [input() for _ in range(N)]

location_list = [tuple(map(int, loc.split())) for loc in location]

A = sorted(location_list, key =lambda point : (point[0], point[1]))
for x, y in A :
    print(f"{x} {y}")