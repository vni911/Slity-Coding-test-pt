a = int(input())
list_b = []
list_c = []
list = []
for i in range(a) :
    b, c = input().split()
    b = int(b)
    c = int(c)
    list_b.append(b)
    list_c.append(c)
    list.append(b+c)
for k in range(a) :
    print(f"Case #{k+1}: {list_b[k]} + {list_c[k]} = {list[k]}")