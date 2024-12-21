Student = []
for i in range(0, 28) :
    N = int(input())
    Student.append(N)

for i in range(1, 31) :
    if i not in Student :
        print(i)