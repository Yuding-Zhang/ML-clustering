import matplotlib.pyplot as plt
from algorithms.Kmeans import KMeansCluster
import numpy as np


TEST_DATA = '../data/generatePoints_distance.txt'
COOR_DATA = '../data/generatePoints.txt'


def main():
    k = 6
    dataset = KMeansCluster.data_process(COOR_DATA)  # 导入数据
    k_points = KMeansCluster.generate_k(dataset, k)  # 初始化随机选取聚类中心
    assignments = KMeansCluster.assign_points(dataset, k_points)  # 对数据进行第一次聚类
    old_assignments = None
    print('Data process done!')

    while assignments != old_assignments:
        new_centers = KMeansCluster.update_centers(dataset, assignments)  # 更新聚类中心
        old_assignments = assignments
        assignments = KMeansCluster.assign_points(dataset, new_centers)  # 再次划分类别
    print('Clustering done!')
    center = new_centers
    print(center)
    temp_plot = zip(assignments, dataset.keys())

    with open(COOR_DATA, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        coords = dict()
        for line in lines:
            p, x, y = line.strip().split()
            p, x, y = int(p), float(x), float(y)
            coords[p] = [x, y]
    for i in range(len(center)):
        c = center[i]
        plt.plot(c[0], c[1], 'ok', markersize=5, alpha=0.8)

    color = {0: 'r', 1: 'b', 2: 'g', 3: 'k', 4: 'c', 5: 'm', 6: 'y'}
    for p in temp_plot:
        for i in range(len(center)):
            c = coords[p[1]]
            try:
                if p[0] == i:
                    plt.scatter(c[0], c[1], c=color[i], alpha=0.6, s=1)
            except KeyError:
                raise 'Key map does not exist!'

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot Result')
    plt.savefig('../images/KMeans/generate_data_result.png')
    plt.close()

    temp = zip(assignments, dataset)
    y, x = zip(*temp)
    plt.scatter(x, y)
    plt.ylabel('Cluster Number')
    plt.xlabel('Point Number')
    plt.title(r'$k=$' + str(k))
    plt.savefig('../images/KMeans/generate_data_cluster_KMeans_test.png')


if __name__ == '__main__':
    main()

