t = int(input())
list = []
for i in range(0,t) :
    a, b = input().split()
    a = int(a)
    b = int(b)
    list.append(a+b)
for i in range(0,t) :
    print(list[i])