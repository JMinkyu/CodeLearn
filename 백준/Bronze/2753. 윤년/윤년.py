Year = input()
Year = int(Year)

if Year % 4 == 0 and Year % 100 != 0:
    print("1")
elif Year % 400 == 0 : 
    print("1")
else :
    print("0")