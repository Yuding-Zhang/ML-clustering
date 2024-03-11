import os
import sys

base_path = os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))
sys.path.append(base_path)

import matplotlib.pyplot as plt
import data_process
from algorithms.DensityPeakCluster import DensityPeakCluster


TEST_DATA = '../data/generatePoints_distance.txt'
COOR_DATA = '../data/generatePoints.txt'



