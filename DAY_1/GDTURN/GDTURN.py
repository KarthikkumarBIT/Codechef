n = int(input())
for i in range(n):
    input_str = input()
    d1, d2 = map(int, input_str.split())
    if d1 + d2 > 6:
        print("YES")
    else:
        print("NO")
