for i in range (int(input())):
    a=input()
    b=input()
    for j in range(len(a)):
        if(a[j]==b[j]):
            print("g",end='')
        else:
            print("b",end='')
    print("\n")
