import matplotlib.pyplot as plt
import data_process
from algorithms.DensityPeakCluster import DensityPeakCluster

GIVEN_DATA = '../data/example_distances.dat'


def main():
    solution = data_process.ProcessData()
    dist, maxid = solution.data_process(GIVEN_DATA)
    # threshold = solution.threshold(dist, maxid)
    threshold = 0.0456  # 截断距离
    sort_dst = solution.CutOff(dist, maxid, threshold)  # cut-off方式计算局部密度 返回按照个数降序的序列
    # sort_dst = solution.Guasse(dist, maxid, threshold)  # gaussian方式计算局部密度 返回按照个数降序的序列
    min_dist, min_num = solution.min_distance(dist, sort_dst, maxid)  # 计算相对距离
    pair_info, refer_info = solution.make_pair(sort_dst, min_dist, maxid)  # 局部密度与相对距离对应
    solution.show_pair_info(pair_info, threshold)
    print('Data process done!')

    clust = DensityPeakCluster()
    center, tag = clust.locate_center(refer_info, maxid, threshold)  # 选取聚类中心 tag用来标记选定的六个点
    taginfo = clust.classify(tag, sort_dst, min_num, maxid)  # 分类
    print('Clustering done!')

    # show each cluster results
    clust.analysis(center, taginfo, dist, maxid)

    # show cluster distribution info
    temp = sorted(taginfo.items(), key=lambda k: k[1])
    y, x = zip(*temp)
    plt.scatter(x, y, c='black', s=10)
    plt.xlabel('Cluster No.')
    plt.ylabel('Point Number')
    plt.title(r'$d_c=$' + str(threshold))
    plt.savefig('../images/DPC/cluster_cutoff.png')
    plt.show()


if __name__ == '__main__':
    main()
