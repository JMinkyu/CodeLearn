while True:
    A, B, C = map(int, input().split())
    if A == 0 and B == 0 and C == 0:
        break
    # 세 변 중 가장 큰 값을 빗변으로 설정
    longest = max(A, B, C)
    if longest == A:
        if B**2 + C**2 == A**2:
            print("right")
        else:
            print("wrong")
    elif longest == B:
        if A**2 + C**2 == B**2:
            print("right")
        else:
            print("wrong")
    else:  # longest == C
        if A**2 + B**2 == C**2:
            print("right")
        else:
            print("wrong")