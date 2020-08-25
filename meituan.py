#8.22 No.3 给定一堆货物重量，给出每次取出的货物位置，求每次取出后剩下的里面哪一堆最重

import sys

if __name__ == '__main__':
    n = int(input())
    line = sys.stdin.readline().strip()
    weight = list(map(int, line.split()))
    line = sys.stdin.readline().strip()
    order = list(map(lambda x: x-1, map(int, line.split())))
    res = []
    sums = [weight[0]]
    for i in range(1, n):
        sums.append(sums[i-1] + weight[i])
    for i in range(n):
        max_value = 0
        j = order[i] + 1
        while(j < n and sums[j] != 0):
            sums[j] -= sums[order[i]]
            j += 1
        sums[order[i]] = 0
        for k in range(i+1):
            max_value = max(max_value, sums[order[k]-1])
        max_value = max(max_value, sums[n-1])
        # res.append(max_value)
        print(max_value)
    # print(res)