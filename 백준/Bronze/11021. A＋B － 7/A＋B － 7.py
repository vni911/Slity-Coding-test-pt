a = int(input())
list = []
for i in range(a) :
    b, c = input().split()
    b = int(b)
    c = int(c)
    list.append(b+c)
for k in range(a) :
    print(f"Case #{k+1}: {list[k]}")