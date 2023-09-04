for i in range (int(input())):
    a,b,c=map(int,input().split())
    d=a//3
    e=a*b
    if(a%3==0):
        d-=1
        print(e+d*c)
     
    else:
         print(e+d*c)
    
