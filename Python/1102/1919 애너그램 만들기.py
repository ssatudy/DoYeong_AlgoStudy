a = list(input())
b = list(input())

acnt = [0] * 26
bcnt = [0] * 26
for i in a:
    acnt[ord(i) - ord('a')] += 1
for j in b:
    bcnt[ord(j) - ord('a')] += 1
cnt = 0
for i in range(26):
    if acnt[i] != bcnt[i]:
        cnt += (abs(acnt[i] - bcnt[i]))
print(cnt)
