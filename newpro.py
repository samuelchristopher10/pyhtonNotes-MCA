def rev(n):
    return int(str(n)[::-1])

x=int(input("Enter a number: "))
i=1
for i in range(1,12):
    print(x,"*",i,"=",x*i)
    i+=1
