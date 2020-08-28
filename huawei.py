import sys

# #8.17 No.1 [0,0] 到 [m,n]的矩阵，逆时针输出个位是7，十位为奇数的数
# def if_print(n):
#     a = n % 10
#     b = (n // 10) % 10
#     return (a == 7 and b % 2 == 1)

# def rot(matric):
#     m = len(matric)
#     if m == 0:
#         return []
#     n = len(matric[0])
#     out = []
#     for i in range(n):
#         tmp = []
#         for j in range(m):
#             tmp.append(matric[j][i])
#         out.append(tmp)
#     return out

# if __name__ == '__main__':
#     line = sys.stdin.readline().strip()
#     m, n = map(int, line.split())
#     matric = []
#     val = 1
#     for i in range(m):
#         tmp = []
#         for j in range(n):
#             tmp.append((val,i,j))
#             val += 1
#         matric.append(tmp)
#     res = []
#     while len(matric):
#         for j in matric[0]:
#             if if_print(j[0]):
#                 res.append([j[1], j[2]])
#         matric = rot(matric[1:])
#     print(str(res).replace(' ', ''))

# #8.17 No.2 给定二叉树节点深度，确定二叉树的可能形状共有多少种
# def combination(n, k):
#     if n < k:
#         return 0
#     if n == k or k == 0:
#         return 1
    
#     k = min(n-k, k)
#     top = 1
#     for i in range(n, n-k, -1):
#         top *= i
#     down = 1
#     for i in range(1, k+1):
#         down *= i
    
#     return top // down

# if __name__ == '__main__':
#     n = int(input())
#     line = sys.stdin.readline().strip()
#     node = list(map(int, line.split()))
#     max_depth = max(node)
#     depth = [0] * (max_depth + 1)
#     for i in node:
#         depth[i] += 1
    
#     res = 1
#     for i in range(max_depth):
#         res *= combination(2 * depth[i], depth[i+1])
#     print(res)

# #8.17 No.3 俄罗斯方块，给出形如2202的数组，表示高度；给出消去之后最少剩多少行

# def helper(frame, brike):
#     """
#     未考虑悬空问题
#     """
#     res = []
#     for i in range(len(frame)):
#         res.append(int(frame[i]) + int(brike[i]))
#     return max(res) - min(res)

# if __name__ == '__main__':
#     frame = sys.stdin.readline().strip()
#     brike = sys.stdin.readline().strip()
#     m = len(frame)
#     n = len(brike)
#     res = 0
#     if m < n:
#         frame, brike = brike, frame
#         m, n = n, m
#     for i in range(m - n + 1):
#         brikes = '0' * i + brike + '0' * (m-n-i)
#         tmp = helper(frame, brikes)
#         if i == 0:
#             res = tmp
#         else:
#             res = min(res, tmp)
#     print(res)

if __name__ == '__main__':
    s, n = sys.stdin.readline().strip().split()
    n = int(n)
    res = ""
    for i in s:
        if ord(i) > 128:
            n -= 2
        else:
            n -= 1
        if n < 0:
            break
        res += i
    print(res)