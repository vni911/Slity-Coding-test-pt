h, m = input().split()
t = int(input())
h = int(h)
m = int(m)
end_h = h+(t//60)
end_m = m+(t%60)

if(end_m >= 60) :
    '''
    m-하고 end_h+1
    '''
    if (end_h +1 >= 24) :
        print(end_h+1-24, end_m-60)
    else :
        print(end_h+1, end_m-60)
else :
    if(end_h >= 24) :
        print(end_h-24, end_m)
    else :
        print(end_h, end_m)