import sys
a = int(sys.stdin.readline())
list = []
for i in range(a) :
    b, c = map(int,sys.stdin.readline().split())
    b = int(b)
    c = int(c)
    list.append(b+c)
for k in range(a) :
    print(list[k])