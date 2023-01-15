from matplotlib.ticker import MultipleLocator, FormatStrFormatter
points = np.stack((x,y), axis=1)
num = len(x) - 1
# 原
# num = len(x)
xx = []
yy = []
for i in range(num+1):
    xx.append(x[road[i]])
    yy.append(y[road[i]])
ax=plt.subplot(111) #注意:一般都在ax中设置,不再plot中设置
ax.fill_between(np.array([0, 1]),0,1,facecolor='red')
n_x1 = np.array(obstacle_x) - 0.5
n_x2 = np.array(obstacle_x) + 0.5
n_y1 = np.array(obstacle_y) - 0.5
n_y2 = np.array(obstacle_y) + 0.5
for i, p in enumerate(points):
        plt.text(*p, '%d' % i)
for i in range(len(n_x1)):
    ax.fill_between(np.array([n_x1[i], n_x2[i]]), n_y1[i], n_y2[i],facecolor='green')
for i in range(num):
    ax.arrow(xx[i], yy[i], xx[i + 1] - xx[i], yy[i + 1] - yy[i],length_includes_head = True,head_width = 0.15,head_length = 0.15,ec = 'b')
plt.xlim(0, n)
plt.ylim(0, n)

ax.xaxis.set_major_locator(MultipleLocator(1))#设置y主坐标间隔 1
ax.yaxis.set_major_locator(MultipleLocator(1))#设置y主坐标间隔 1
ax.xaxis.grid(True,which='major')#major,color='black'
ax.yaxis.grid(True,which='major')#major,color='black'
plt.show()