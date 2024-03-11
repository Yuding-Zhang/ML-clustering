import os
import sys

base_path = os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))
sys.path.append(base_path)

import matplotlib.pyplot as plt
import data_process
from algorithms.Kmeans import KMeansCluster

GENERATE_POINTS_DIST = '../data/generatePoints_distance.txt'
GENERATE_POINTS = '../data/generatePoints.txt'

k = 6  # 设定kmeans分6类


def main():
    dataset = KMeansCluster.data_process(GENERATE_POINTS)  # 导入数据
    k_points = KMeansCluster.generate_k(dataset, k)  # 初始化随机选取聚类中心
    assignments = KMeansCluster.assign_points(dataset, k_points)  # 对数据进行第一次聚类
    old_assignments = None
    print('Data process done!')

    while assignments != old_assignments:
        new_centers = KMeansCluster.update_centers(dataset, assignments)  # 更新聚类中心
        old_assignments = assignments
        assignments = KMeansCluster.assign_points(dataset, new_centers)  # 再次划分类别
    print('Clustering done!')
    return zip(assignments, dataset)


if __name__ == '__main__':
    temp = main()
    y, x = zip(*temp)
    plt.scatter(x, y)
    plt.ylabel('Cluster No.')
    plt.xlabel('Point Number')
    plt.title(r'$kmeans=$' + str(k))
    plt.savefig('../images/KMeans/result.png')
    plt.show()
