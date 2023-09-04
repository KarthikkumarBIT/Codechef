for i in range(int(input())):
    a=int(input())
    b=list(map(int,input().split()))
    m=1
    for j in range(0,a-1):
        if b[j]!=b[j+1]:
            m+=1
    print(m)



