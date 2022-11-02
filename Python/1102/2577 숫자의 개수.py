a = int(input())
b = int(input())
c = int(input())
cnt = [0] * 10
abc = list(str(a * b * c))
# abc = list(abc)

for i in range(len(abc)):
    cnt[int(abc[i])] += 1

for i in range(10):
    print(cnt[i])