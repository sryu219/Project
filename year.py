year = int(input("연도를 입력하세요"))

if year % 4 == 0:
    print("윤년")
    if year % 100 == 0:
        print("평년")
    elif year % 400 ==0:
        print("윤년")
else:
    print("윤년이 아닙니다")
