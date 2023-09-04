a=int(input())
b=list(map(int,input().split()))
c=0
d=0
for i in range(a):
    if(i%2==0):
        c+=1
    else:
        d+=1 
if(c>d):
    print("READY FOR BATTLE")
else:
    print("NOT READY")
  
