for i in range (int(input())):
    a,b=map(int,input().split())
    c=int(100*(a/100))
    a=100-c
    d=int(200*(b/100))
    b=200-d
    if(a<b):
        print("first")
    elif(a>b):
        print("second")
    else:
        print("both")
