# import sys

# def helper(x,a,b):
#     val = 0
#     num = 0
#     res = 0
#     if a / al < b / bl:
#         num = (x - 1) // al + 1
#         val = a * num
#     else:
#         num = x // bl 
#         res = x - num * bl
#         val = num * b
#         if res > 0:
#             va = ((res - 1) // al + 1) * a
#             vb = b
#             val += min(va, vb)
#     return val

# if __name__ == '__main__':
#     n = int(input())
#     al = 500
#     bl = 1500
#     for i in range(n):
#         line = sys.stdin.readline().strip()
#         x, a, b = map(int, line.split())
#         print(helper(x, a, b))

import sys

def helper(s):
    n = len(s)
    m = n if n % 2 == 0 else n-1
    for i in range(m, 0, -2):
        count = 0
        for j in range(n - i + 1):
            if s[j] == s[j+i]:
                count += 1
            else:
                count = 0
        if count == i:
            return i
    return 0

if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    print(helper(s))
                