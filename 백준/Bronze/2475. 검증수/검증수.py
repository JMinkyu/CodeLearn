def Cal(a, b, c, d, e) :
    Add = a**2+b**2+c**2+d**2+e**2
    result = Add%10
    print(result)    

A, B, C, D, E = map(int,input().split())
Cal(A, B, C, D, E)
