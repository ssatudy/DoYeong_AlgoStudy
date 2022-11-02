'''
9
5 12 7 10 9 1 2 3 11
13

5
10 2 6 3 5
8
'''

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
cnt = [0] * 2000001
ans = 0
for i in range(n):
    if cnt[x-arr[i]] >= 1:
        ans += 1
        cnt[arr[i]] += 1
    # elif cnt[x-arr[i]] == 0:
    else:
        cnt[arr[i]] = +1
print(ans)