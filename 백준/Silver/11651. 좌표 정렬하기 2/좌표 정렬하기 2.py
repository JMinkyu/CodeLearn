N = int(input())

location = [input() for _ in range(N)]

location_list = [tuple(map(int, loc.split())) for loc in location]

A = sorted(location_list, key = lambda x : (x[1], x[0]))

for x, y in A :
    print(f"{x} {y}")

