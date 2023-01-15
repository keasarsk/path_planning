import matplotlib.pyplot as plt
import math
import numpy as np
# 设置活动范围矩阵
def Distance(x1, y1, x2, y2):
    return math.sqrt(pow((x1- x2), 2) + pow((y1- y2), 2))
n = 6
x = []
y = []

dx = [-1, -1, 0, 1, 1, 1, 0, -1]  # 方向数组
dy = [0, -1, -1, -1, 0, 1, 1, 1]
node = [-1, -(n + 1), -n, -(n - 1), 1, n + 1, n, n - 1]
for i in range(n):
    for j in range(n):
        x.append(j + 0.5)
        y.append(i + 0.5)
x = np.array(x)
y = np.array(y)
num = len(x)
distance = np.zeros([num,num])

INF = 1000
for i in range(num):
    for j in range(num):
        distance[i, j] = INF
for i in range(len(x)):
    for j in range(8):
        new_x = x[i] + dx[j]
        new_y = y[i] + dy[j]
        if new_x > 0 and new_y > 0 and new_x < n and new_y < n:
            distance[i, i + node[j]] = Distance(x[i], y[i], new_x, new_y)
