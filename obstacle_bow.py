class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        road = []
        mark = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if mark[i][j] == 0 and grid[i][j] == 0:
                    self.dfs(mark, grid, road, i, j)
        return road

    # 深度优先搜索:时间优于宽度优先搜索
    def dfs(self, mark, grid, road, x, y):
        mark[x][y] = 1
#         road.append([x, y])
        dx = [-1, 1, 0, 0, -1, -1, 1, 1]  # 方向数组
        dy = [0, 0, 1, -1, 1, -1, -1, 1]
        m = len(grid)
        n = len(grid[0])
        p = 0
        # 遍历上下左右四个方向
        for i in range(8):
            newx = dx[i] + x
            newy = dy[i] + y
            if newx < 0 or newx >= m or newy >= n or newy < 0:
                continue
            if mark[newx][newy] == 0 and grid[newx][newy] == 0:
                road.append([x, y])
                self.dfs(mark, grid, road, newx, newy)
#                 p += 1
#                 if p > 2:
#                     road.append([x, y])
#                 if [newx, newy] not in road:
                road.append([newx, newy])

n = 8
s = Solution()
# nums = xy
flag = np.zeros([n, n])
a = np.random.randint(1,n,size=15)
b = np.random.randint(1,n,size=15)
# a = [1, 1, 2, 3, 3, 3, 3, 2]
# b = [3, 5, 3, 3, 4, 5, 5, 5]
flag[a, b] = 1
road = np.array(s.numIslands(flag))
X = []
Y = []
for i in range(len(road)):
    X.append(road[i, 0] + 0.5)
    Y.append(road[i, 1] + 0.5)
num = len(X)
ax=plt.subplot(111) #注意:一般都在ax中设置,不再plot中设置
ax.fill_between(np.array([0, 1]),0,1,facecolor='red')
n_x1 = np.array(a)
n_x2 = np.array(a) + 1
n_y1 = np.array(b)
n_y2 = np.array(b) + 1
# for i, p in enumerate(road):
#         plt.text(*p, '%d' % i)
for i in range(len(n_x1)):
    ax.fill_between(np.array([n_x1[i], n_x2[i]]), n_y1[i], n_y2[i],facecolor='green')
for i in range(num - 1):
    ax.arrow(X[i], Y[i], X[i + 1] - X[i], Y[i + 1] - Y[i],length_includes_head = True,head_width = 0.15,head_length = 0.15,ec = 'b')
plt.xlim(0, n)
plt.ylim(0, n)

ax.xaxis.set_major_locator(MultipleLocator(1))#设置y主坐标间隔 1
ax.yaxis.set_major_locator(MultipleLocator(1))#设置y主坐标间隔 1
ax.xaxis.grid(True,which='major')#major,color='black'
ax.yaxis.grid(True,which='major')#major,color='black'