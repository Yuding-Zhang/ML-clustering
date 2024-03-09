# ML-clustering

用于2024年春人工智能基础课程代码，包含三种聚类算法（KMeans HC DPC)及其可视化。

## Installation

- Create a conda environment with `python==3.9.12`. Install python packages in `requirements.txt`.

- ```shell
  pip install -r requirements.txt
  ```

## Download the dataset

可以根据个人需要下载dat、csv和txt的数据集到data文件目录下，修改相应文件的路径名称和数据处理代码。

## scripts文件目录

- 该文件目录下包含三种算法的main函数，用于调用algorithms文件目录下的算法和data_process文件，输出得到分类图片。
- images目录保存对应算法得到的结果图片
- ![generate_data_cluster_cutoff_test](F:\ML-clustering\images\DPC\generate_data_cluster_cutoff_test.png)

##  visualization文件目录

+ 该目录包含三种算法的test文件，用于测试算法以及得到聚类的散点图。
+ ![generatedPoints](F:\ML-clustering\images\generatedPoints.png)
+ ![generatedColoredPoints](F:\ML-clustering\images\generatedColoredPoints.png)
+ generate_points.py用于生成2400个随机的散点，数据保存在data中，test文件均对该数据进行操作。

## Reference

[stuntgoat/kmeans: K Means Clustering with Python (github.com)](https://github.com/stuntgoat/kmeans)

[jasonwbw/DensityPeakCluster: A cluster framework for 'Clustering by fast search and find of density peaks' in science 2014. (github.com)](https://github.com/jasonwbw/DensityPeakCluster)

[lanbing510/DensityPeakCluster: Python Code For 'Clustering By Fast Search And Find Of Density Peaks' In Science 2014. (github.com)](https://github.com/lanbing510/DensityPeakCluster)

