import math
n = list(map(int, input().split()))
sum = 0
for i in range(len(n)) :
    sum += pow(n[i], 2)
print(sum%10)