i = int(input("Enter a number: "))
j = int(input("Enter another number: "))
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
k = int(input("Enter your choice (1/2/3/4): "))
if k == 1:
    print(i, "+", j, "=", i + j)
elif k == 2:
    print(i, "-", j, "=", i - j)
elif k == 3:
    print(i, "*", j, "=", i * j)
elif k == 4:
    if j != 0:
        print(i, "/", j, "=", i / j)
    else:
        print("Error: Division by zero is not allowed.")
