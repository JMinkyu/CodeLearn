T = int(input()) # 테스트 데이터 개수
for i in range(T) :
    # H : 전체 층수, W : 전체 넓이, N : 인원순서
    H, W, N = map(int, input().split())

    # 손님 층수
    room_high = N % H #  N/H의 나머지 값이 층수
    if room_high == 0 : # 나머지가 0이면 N값하고 동일
        room_high = H

    room_num = (N - 1)//H + 1 

    # 룸번호가 10보다 작으면 앞에 0하나 추가
    if room_num < 10 :
        room_num = f"0{str(room_num)}"
    print(f'{room_high}{room_num}')
