Grade = input()
score = 0.0

if Grade[0] == 'A':
    score += 4
elif Grade[0] == 'B' :
    score += 3
elif Grade[0] == 'C' :
    score += 2
elif Grade[0] == 'D' :
    score += 1

if Grade[0] == 'F':
    grade = 0.0
elif Grade[1] == '+':
    score += 0.3
elif Grade[1] == '-':
    score -= 0.3

print(score)
