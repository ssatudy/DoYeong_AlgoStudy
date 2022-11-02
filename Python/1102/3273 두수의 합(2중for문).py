'''
9
5 12 7 10 9 1 2 3 11
13
'''
n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())
cnt = 0

for i in range(n - 1):
    for j in range(i+1, n):
        if arr[i] + arr[j] == x:
            cnt += 1
        if arr[i] + arr[j] > x:
            break


print(cnt)
