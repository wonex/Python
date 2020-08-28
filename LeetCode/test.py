# from time import time 

# def timer(fun):
#     def f(*args, **kwargs):
#         begin = time()
#         out = fun(*args, **kwargs)
#         print(time() - begin)
#         return out
#     return f

# @timer
# def add(x, y, z=10):
#     return x + y + z

# if __name__ == '__main__':
#     print(add(2, 3, 4))

import sys

def ifSame(s):
    length = len(s)
    i = 0
    j = length // 2
    res = True
    while (i < length // 2 and j < length):
        if s[i] != s[j]:
            res = False
            break
        i += 1
        j += 1
    return res

def helper(s):
    n = len(s)
    m = n if n % 2 == 0 else n-1
    for i in range(m, 0, -2):
        for j in range(n - i + 1):
            if ifSame(s[j:i+j]):
                return i
    return 0

if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    print(helper(s))