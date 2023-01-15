
# remove_n = np.random.randint(1, num, size = 16)
remove_n = [1, 2, 9, 14, 20, 23, 29, 35] # 设置任务点/障碍点

obstacle_x = []
obstacle_y = []
for i in range(len(remove_n)):
    obstacle_x.append(x[remove_n[i]])
    obstacle_y.append(y[remove_n[i]])
x = np.delete(x, remove_n)
y = np.delete(y, remove_n)
distance = np.delete(distance, remove_n, 0)
distance = np.delete(distance, remove_n, 1)
num = len(x)
x2 = x
y2 = y
obstacle_x2 = obstacle_x
obstacle_y2 = obstacle_y