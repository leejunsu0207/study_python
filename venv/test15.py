import time

start_time = time.time()
def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

prime_count = 0

for i in range(2, 50001):
    if is_prime(i):
        prime_count = prime_count + 1
        print(i, end=", ")


end_time = time.time()

print("\n", end_time - start_time , "초 실행 했음")