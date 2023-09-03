for i in range (int(input())):
    a,b=map(int,input().split())
    if b>a :
        print("profit")
    
    elif a==b :
        print( "neutral")
    else:
        print("loss")
