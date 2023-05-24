import random

guess_str = input("1 ~ 45 번호 6개를 쉽표로 분리하여 입력 : ").split(", ")
guess_list = list()

for i in guess_str:
    guess_list.append(int(i))

lotto_list = random.sample(range(1, 46, 1), 6)

hit_count = 0

for iNum in guess_list:
    if iNum in lotto_list:
        hit_count = hit_count + 1


print("success" + str(hit_count))
print(":")