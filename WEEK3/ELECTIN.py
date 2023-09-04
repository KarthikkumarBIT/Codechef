for i in range (int(input())):
    a,b=map(int,input().split())
    count=0
    l=list(map(int,input().split()))
    for j in l:
        if j>=b:
            count+=1
    print(count)
    
