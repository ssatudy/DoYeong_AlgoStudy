'''
2
<<BP<A>>Cd-
ThIsIsS3Cr3t

1
<<BP<A>>Cd-

< 커서 왼쪽이동
> 커서 오른쪽 이동
- 백스페이스
'''
# import sys;
#
# sys.stdin = open('0000sample.txt')

from collections import deque
for _ in range(int(input())):
    word = list(input().rstrip())
    left = []
    right = []
    for i in word:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
    right.reverse()
    # print(left,right)
    print(''.join(left+right))
