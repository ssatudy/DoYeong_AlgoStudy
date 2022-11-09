import sys;

sys.stdin = open('0000sample.txt')

from collections import deque

n,k = map(int,input().split())
p = list(range(1,n+1))
print(p)
Q = deque(p)
print(Q)
dap = []
while Q:
    for _ in range(k-1):
        Q.append(Q.popleft())
    yosep = str(Q.popleft())
    dap.append(yosep)
print(dap)
print('<' + ', '.join(dap) + '>')