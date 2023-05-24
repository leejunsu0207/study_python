

print(format("구구단", ">20s"))

print("  |", end="")
for j in range(1, 10):
    print("  ", j, end="")

print()
print("-----------------------------------------------------")

for i in range(1, 10):
    print(i, "|", end="")
    for k in range(1, 10, 1):
        print(format(i * k, ">4d"), end="")
    print()

