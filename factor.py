def d(x):
    result = 1
    for i in range(x):
        result += i
        print(i)
    return result

a= int(input("숫자:"))
print(d(a))
