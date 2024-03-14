import os
import sys

base_path = os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))
sys.path.append(base_path)

import matplotlib.pyplot as plt
import data_process
from algorithms.DensityPeakCluster import DensityPeakCluster

TEST_DATA = '../data/generatePoints_distance_PLOT.txt'
TEST_PLOT_DATA = '../data/generatePoints_PLOT.txt'


def plot_points(center, temp, color, tag, style):
    with open(TEST_PLOT_DATA, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        coords = dict()
        for line in lines:
            p, x, y = line.strip().split()
            p, x, y = int(p), float(x), float(y)
            coords[p] = [x, y]
    for i in range(len(center)):
        c = coords[center[i]]
        plt.plot(c[0], c[1], 'ok', markersize=5, alpha=0.8)

    for p in temp:
        for i in range(len(center)):
            c = coords[p[0]]
            try:
                # 标号从1开始，故i + 1 熵的值没选好会有-1
                if tag == 2:
                    if p[1] == i + 1:
                        plt.scatter(c[0], c[1], c=color[i+1], marker=style[i+1], alpha=0.6, s=1)
                else:
                    plt.scatter(c[0], c[1], c=color[0], marker=style[0], alpha=0.6, s=1)
            except KeyError:
                raise 'Key map does not exist!'

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot Result')
    plt.savefig('../images/DPC/generate_data_result_{}.png'.format(tag))



def main():
    solution = data_process.ProcessData()
    dist, maxid = solution.data_process(TEST_DATA)
    # 通用数据使用以下一行求截断距离（耗时较长）
    # threshold = solution.threshold(dist, maxid) # 更换数据后这里需要重新计算
    threshold = 0.7828967189629044
    sort_dst = solution.CutOff(dist, maxid, threshold)
    # sort_dst = solution.Guasse(dist, maxid, threshold)
    min_dist, min_num = solution.min_distance(dist, sort_dst, maxid)
    pair_info, refer_info = solution.make_pair(sort_dst, min_dist, maxid)
    solution.show_pair_info(pair_info, threshold)
    print('Data process done!')

    clust = DensityPeakCluster()
    center, tag = clust.locate_center(refer_info, maxid, threshold)
    taginfo = clust.classify(tag, sort_dst, min_num, maxid)
    print('Clustering done!')
    print(center)  # [978, 1842, 1522, 438, 2077, 123]

    # show each cluster results
    # clust.analysis(center, taginfo, dist, maxid)

    # show cluster distribution info
    temp = sorted(taginfo.items(), key=lambda k: k[1])
    color = {0: 'r', 1: 'b', 2: 'g', 3: 'k', 4: 'c', 5: 'm', 6: 'y'}
    style = {0: 'o', 1: 'v', 2: '8', 3: 'p', 4: 'd', 5: '*', 6: 's'}
    # plot_points(center, temp, color, 1, style)
    plot_points(center, temp, color, 2, style)

    # y, x = zip(*temp)
    # plt.scatter(x, y)
    # plt.xlabel('Cluster Number')
    # plt.ylabel('Point Number')
    # plt.title(r'$d_c=$' + str(threshold))
    # plt.savefig('../images/DPC/generate_data_cluster_cutoff_test.png')


if __name__ == '__main__':
    main()
