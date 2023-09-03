for i in range (int(input())):
    L=list(map(int,input().split()))
    a=max(L)
    L.remove(a)
    print(max(L))
