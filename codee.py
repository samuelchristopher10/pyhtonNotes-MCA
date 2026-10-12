B=65
for i in range(B,B+26):
    for j in range(B,i+1):
        print(chr(i),end="")
    print(repr(chr(i)))