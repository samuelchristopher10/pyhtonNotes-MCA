t=int(input("Enter any numbers:"))
total=0
even=0
odd=0
i=1
for i in range(1, t+1):
    if (i%2==0):
        print(i,"is even number")
        even += i
    else:
        print(i,"is odd number")
        odd += i
    total += i
    i+=1
print("Sum of all numbers is:", total)
print("Sum of even numbers is:", even)
print("Sum of odd numbers is:", odd)