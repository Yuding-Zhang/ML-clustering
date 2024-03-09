from collections import defaultdict
from random import uniform
from math import sqrt


# kmeans 中需要的一些工具函数

def point_avg(dataset, points):
    """
    Accepts a list of points, each with the same number of dimensions.
    NB. points can have more dimensions than 2

    Returns a new point which is the center of all the points.
    计算距离均值，返回新的聚类中心
    """
    dimensions = len(dataset[points[0]])

    new_center = []

    for dimension in range(dimensions):
        dim_sum = 0  # dimension sum
        for p in points:
            dim_sum += dataset[p][dimension]

        # average of each dimension
        new_center.append(dim_sum / float(len(points)))

    return new_center


def distance(point_a, point_b):
    """
    计算两点之间的欧式距离
    """
    dimensions = len(point_a)

    _sum = 0
    for dimension in range(dimensions):
        difference_sq = (point_a[dimension] - point_b[dimension]) ** 2
        _sum += difference_sq
    return sqrt(_sum)


class KMeansCluster(object):
    def generate_k(self, k):
        """
        随机选取k类初始聚类中心
         """
        centers = []
        dimensions = len(self[0])
        min_max = defaultdict(int)

        # 获得所有二维点的x与y上下界
        for point in self:
            for i in range(dimensions):
                val = self[point][i]
                min_key = 'min_%d' % i
                max_key = 'max_%d' % i
                if min_key not in min_max or val < min_max[min_key]:
                    min_max[min_key] = val
                if max_key not in min_max or val > min_max[max_key]:
                    min_max[max_key] = val

        # 生成k个聚类中心
        for _k in range(k):
            rand_point = []
            for i in range(dimensions):
                min_val = min_max['min_%d' % i]
                max_val = min_max['max_%d' % i]

                rand_point.append(uniform(min_val, max_val))

            centers.append(rand_point)

        return centers

    def assign_points(self, centers):
        """
        分类打标签
         """
        assignments = []
        for point_number in self:
            shortest = float('inf')  # positive infinity
            shortest_index = 0
            for i in range(len(centers)):
                dis_val = distance(self[point_number], centers[i])
                if dis_val < shortest:
                    shortest = dis_val
                    shortest_index = i
            assignments.append(shortest_index)
        return assignments

    def update_centers(self, assignments):
        """
        更新聚类中心
         """
        new_means = defaultdict(list)
        centers = []
        for assignment, point_number in zip(assignments, self):
            new_means[assignment].append(point_number)

        for center_assignment in new_means.values():
            centers.append(point_avg(self, center_assignment))

        return centers

    # 数据处理
    def data_process(self):
        """
        :folder: data file path
        :rtype: dict pair distance
                MAX id number
                导入data
        """
        dataset = dict()
        with open(self, 'r') as data:
            for line in data:
                points_serial_number, points_x, points_y = line.strip().split()
                points_serial_number, points_x, points_y = int(points_serial_number), float(points_x), float(points_y)
                dataset[points_serial_number] = (points_x, points_y)
        return dataset
