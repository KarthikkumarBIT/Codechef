for i in range (int(input())):
    a,b=map(int,input().split())
    if a>=b:
        print((a*2)-b)

    else:
        print((a*2)-a)
