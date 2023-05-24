hei_list = [1, 4, 14]
rad_list = range(10, 40, 10)


for rad, hei in zip(rad_list, hei_list):
    # 부피, 겉넓이 계산
    vol = 1 / 3 * 3.14 * rad ** 2 * hei
    suf = 3.14 * rad ** 2 + 3.14 * rad * hei
    print("부피 == ", vol, sep="")
    print("겉넓이 == ", suf, sep="")
    print(vol, suf)

