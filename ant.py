def creat_city():
    """
    input:
        num: 城市数量
        scale: 城市坐标范围x,y in (0, scale)
    return:
        V：城市的坐标集合
        E：城市的邻接矩阵
    """


    V = np.stack((x,y), axis=1)

#     inner = -2 *  V.dot(V.T)
#     xx = np.sum(V**2, axis=1, keepdims=True)
#     E = xx + inner + xx.T
#     E = E**0.5
    index = [i for i in range(num)]
    E = distance
    #为了防止蚂蚁出现自旋，邻接矩阵上的对角线取值尽量大一点。
    E[index,index] = 9999999
    return V,E
V, E = creat_city()
plt.scatter(V[:,0], V[:,1], alpha=0.6, c = "r")  # 绘制散点图，透明度为0.6（这样颜色浅一点，比较好看）
plt.show()
import heapq
import random

def a_res(samples, m):
    """
    :samples: [(item, weight), ...]
    :k: number of selected items
    :returns: [(item, weight), ...]
    """

    heap = [] # [(new_weight, item), ...]
    for sample in samples:
        wi = sample[1]
        if wi==0:
            continue
        ui = random.uniform(0, 1)
        ki = ui ** (1/wi)

        if len(heap) < m:
            heapq.heappush(heap, (ki, sample))
        elif ki > heap[0][0]:
            heapq.heappush(heap, (ki, sample))

            if len(heap) > m:
                heapq.heappop(heap)

    return [item[1] for item in heap]
def possibility(eta, gamma, other_city, cur_city):
    """
    返回候选城市集合中，从start到各候选城市的概率，只返回有路径的
    """   
    alpha = 1
    beta = 5
    start_city = cur_city[-1]

    t_i = gamma[start_city]  
    n_i = eta[start_city]
    
    temp = (t_i**alpha * n_i**beta)
    temp[cur_city] = 0
    add = temp.sum()
    p_ij = temp/add
    
    return p_ij
def rotate(l, n):
    '''
    旋转列表。
    '''
    return l[n:] + l[:n]

def get_path_dis(root, E):
    """
    获取该路径距离。
    """
    dis = E[root[:-1], root[1:]].sum()
    return dis + E[root[0],root[-1]]

def MMAS(V, E, M, num, islocal=True):
    """
    最大最小蚁群算法
    V : 点集
    E: 邻接矩阵，点之间的连接性，
    M: 蚂蚁数量
    num：迭代次数
    """
    #相关参数
    global_best_path=None   #当前最优路径
    global_best_dis = 99999999
    cur_city = None
    other_city = [i for i in range(len(V))]
    lo = 0.8   #信息素挥发率
    e = num #精英路径权重
    
    tao_min = 0.1 / num
    tao_max = 1

    #信息素启发值
    eta = 1/E
    eta[np.isinf(eta)] = 0
    
    #信息素浓度
    E_mean = E[E>0].mean()
    gamma = np.full(E.shape,tao_max) 
    
    V_index = [i for i in range(len(V))]

    for i in range(num):
        epoch_gamma = np.zeros_like(gamma) #保存每一轮的各路径信息素累积量
        local_best_path=None   #每一次迭代当前最优路径
        local_best_dis = 99999999
        for j in range(M):
            cur_city = [j%len(V)]
            other_city = [i for i in range(len(V))]
            other_city.remove(cur_city[-1])
            while(other_city):
                p_ij = possibility(eta, gamma, other_city, cur_city)
                next_city = int(a_res(np.stack((V_index,p_ij),axis=1), 1)[0][0])
                if next_city not in other_city:
                    next_city = int(a_res(np.stack((V_index,p_ij),axis=1), 1)[0][0])
                
                epoch_gamma[cur_city[-1],next_city] += gamma[cur_city[-1],next_city]
                cur_city.append(next_city)
                other_city.remove(next_city)
            epoch_dis = get_path_dis(cur_city, E)
            if epoch_dis < local_best_dis:
                local_best_dis = epoch_dis
                local_best_path = cur_city

        if local_best_dis < global_best_dis:
            global_best_dis = local_best_dis
            global_best_path = local_best_path
         #信息素更新   
        gamma = (1 - lo) * gamma
        if islocal:
            for i,j in np.stack((local_best_path[1:] + local_best_path[:1], local_best_path), axis=1):
                gamma[i,j] += e / local_best_dis
        else:
            for i,j in np.stack((global_best_path[1:] + global_best_path[:1], global_best_path), axis=1):
                gamma[i,j] += e / global_best_dis
        gamma[gamma>tao_max] = tao_max
        gamma[gamma<tao_min] = tao_min
    
    print("The shortest distance is {}m and the best path is: ".format(global_best_dis), end="")
    best_path = rotate(global_best_path, global_best_path.index(0))
    for index in best_path:
        print(" city_" + str(index) + " ->", end="")
    print("city_0.\n")
    
    return best_path
root = MMAS(V, E, 50, 100)
path = V[root]
path = np.append(path, [path[0]], axis=0)
plt.plot(path[:,0], path[:,1], marker="o", mfc="r")
plt.show()