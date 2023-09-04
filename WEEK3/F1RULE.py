for i in range(int(input())):
    a,b=map(int,input().split())
    if(((a*7)/100+a>=b)):
        print("YES")
    else:
        print("NO")
