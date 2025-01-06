from string import ascii_lowercase
alist = ascii_lowercase
word = list(input())
for i in alist :
    if i in word :
        print(word.index(i), end = " ")
    else :
        print(-1, end=" ")