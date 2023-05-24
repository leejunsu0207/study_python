num1 = int(input("첫번째 숫자 : "))
num2 = int(input("두번째 숫자 : "))
num3 = int(input("세번째 숫자 : "))

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)