import random

hit_number = random.randint(1, 1001)

guess_count_list = range(1, 21, 1)

passfail = False

for guess_count in guess_count_list :

    guess = int(input("숫자를 맞혀보세요("+str(guess_count)+"번째 시도 : "))

    if hit_number == guess:
        passfail = True
        break;
    elif hit_number > guess:
        print(str(guess) + "보다 크다", end="")
    else:
        print(str(guess) + "보다 작다", end="")


if passfail == True:
    print("success")
else:
    print("fail")