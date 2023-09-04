for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    A=max(a,b,c,d)
    sum=a+b+c+d-A
    if(A>sum):
        print("yes")
    else:
        print("no")
        
