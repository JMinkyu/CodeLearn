T = int(input())

for n in range(T) :    
    result = list(input())
    total_score = 0
    score = 0
    for i in range(len(result)) :
        if result[i] == 'O' :
            score = score + 1
            total_score = total_score + score
        else :
            score = 0
            total_score = total_score + score
    print(total_score)