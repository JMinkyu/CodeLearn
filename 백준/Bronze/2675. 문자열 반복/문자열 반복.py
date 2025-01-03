T = int(input())

for i in range(T) :
    num, text = input().split()
    num = int(num)
    list_text = list(text)
    for j in range(len(list_text)) :
        print(list_text[j] * num, end ='')
    print('')