for i in range(int(input())):
    a,b=map(int,input().split())
    c=len(str(a*b))
    if(c==5):
        print("YES")
    else:
        print("NO")
