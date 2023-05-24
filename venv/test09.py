def prt_cone_vol(rad, hei):

    if(rad >= 0 and hei >= 0):
        # 부피, 겉넓이 계산
        vol = 1 / 3 * 3.14 * rad ** 2 * hei
        suf = 3.14 * rad ** 2 + 3.14 * rad * hei
        print("부피 == ", vol, sep="")
        print("겉넓이 == ", suf, sep="")
        print(vol, suf)
    else:
        print("0이상 입력")

rad = 30
hei = -40
prt_cone_vol(rad, hei)

def reverse(n1):
    while n1 != 0:
        digit = n1 % 10
        n1 = n1 // 10
        print(digit, end="")
    print()
reverse(987)

def prt_cone_vol1(rad, hei):

    if(rad >= 0 and hei >= 0):
        # 부피, 겉넓이 계산
        vol = 1 / 3 * 3.14 * rad ** 2 * hei
        suf = 3.14 * rad ** 2 + 3.14 * rad * hei
        return vol
    else:
        print("0이상 입력")

print(format(prt_cone_vol1(12,13), ">20.3f"), "입니다.")

def prt_cone_vol2(rad, hei):

    if(rad >= 0 and hei >= 0):
        # 부피, 겉넓이 계산
        vol = 1 / 3 * 3.14 * rad ** 2 * hei
        suf = 3.14 * rad ** 2 + 3.14 * rad * hei
        return vol, suf
    else:
        print("0이상 입력")

vol1, suf1 = prt_cone_vol2(19,20)
print(vol1)
print(suf1)


num1 = int(input("첫번째 숫자 : "))
num2 = int(input("두번째 숫자 : "))
num3 = int(input("세번째 숫자 : "))

def sort(num1, num2, num3):
    if(num1 > num2):
        num1, num2 = num2, num1
    if(num1 > num3):
        num1, num3 = num3, num1
    if(num2 > num3):
        num2, num3 = num3, num2
    print(num1, num2, num3)

sort(num1, num2, num3)
print("dddddddddddd", num1, num2, num3)


def prt_cone_vol3(rad = 20, hei = 30):
    if(rad >= 0 and hei >= 0):
        # 부피, 겉넓이 계산
        vol = 1 / 3 * 3.14 * rad ** 2 * hei
        suf = 3.14 * rad ** 2 + 3.14 * rad * hei
        rad, hei = 0, 0
        return vol, suf
    else:
        print("0이상 입력")

print(prt_cone_vol3())

def varSumAvg(*numbers):
    sum = 0
    count = 0
    for i in numbers:
        sum = sum + i
        count = count + 1
    return sum,  sum / count


print(varSumAvg(12, 23, 34, 23))
