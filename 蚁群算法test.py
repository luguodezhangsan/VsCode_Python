# -*- coding: utf-8 -*-
import random
import copy
import sys
import math
import tkinter  #//GUI模块
import threading  #//多线程编程
import time
from functools import reduce

(ALPHA, BETA, RHO, Q) = (1.5, 2.0, 0.9, 100.0)
# 城市数，蚁群
(city_num, ant_num) = (30, 30)
distance_x = [
    24, 37, 54, 25, 7, 2, 68, 71, 54, 83, 64, 18, 22, 83, 21, 25, 24, 58, 71, 74, 87, 18, 13, 82, 62, 58, 45, 41, 44, 42
]
distance_y = [
    44, 84, 67,62, 64, 99, 58, 44, 62, 69, 60, 54, 60, 46, 58, 38, 42, 69, 71, 78, 76, 40, 40, 7, 32, 35, 21, 26, 35, 20
]
# 城市距离和信息素
distance_graph = [[0.0 for col in range(city_num)] for raw in range(city_num)]
pheromone_graph = [[1.0 for col in range(city_num)] for raw in range(city_num)]

print(distance_graph)
print(pheromone_graph)