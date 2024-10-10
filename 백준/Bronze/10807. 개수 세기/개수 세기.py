n = int(input())
number = list(map(int, input().split()))
num = int(input())
count = 0
for k in range(n) :
    if (number[k] == num):
        count += 1
print(count)