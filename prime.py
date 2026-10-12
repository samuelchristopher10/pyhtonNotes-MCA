x = int(input("Enter the upper limit: "))

for i in range(1, x + 1):
    if i % 2 != 0:
        continue
    print(i,"is even")
