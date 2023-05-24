hei_list = [1, 4, 14, 35, 76]


#반지름, 높이 값 입력
rad = int(input("반지릅 입력 : "))

if(rad >= 0):

    for hei in hei_list:
        # 부피, 겉넓이 계산
        vol = 1 / 3 * 3.14 * rad ** 2 * hei
        suf = 3.14 * rad ** 2 + 3.14 * rad * hei
        print("부피 == ", vol, sep="")
        print("겉넓이 == ", suf, sep="")
        print(vol, suf)

else:
    print("0이상 입력")

