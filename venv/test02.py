#반지름, 높이 값 입력
rad = int(input("반지릅 입력 : "))
hei = int(input("높이 입력 : "))
if(rad >= 0 and hei >= 0):

    # 부피, 겉넓이 계산
    vol = 1 / 3 * 3.14 * rad ** 2 * hei
    suf = 3.14 * rad ** 2 + 3.14 * rad * hei
    print("부피 == ", vol, sep="")
    print("겉넓이 == ", suf, sep="")
    print(vol, suf)

else:
    print("0이상 입력")