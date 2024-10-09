h, m = input().split()
h = int(h)
m = int(m)

if(45<= m <=59) :
    if(h == 0):
        print(h, m-45)
    else :
        print(h, m-45)
else :
    if(h == 0) :
        print(h+23, m+15)
    else :
        print(h-1, m+15)