for i in range (int(input())):
    a=int(input())
    if(a<=10):
        print("LOWER DOUBLE")
    elif(10<a<=15):
        print("LOWER SINGLE")
    elif(15<a<=25):
        print('UPPER DOUBLE')
    else:
        print('UPPER SINGLE')
