# -*- coding: utf-8 -*-

import numpy

"""
此类函数主要处理N阶3维矩阵
x轴指向屏幕外侧
y轴指向屏幕上方
z轴指向屏幕外
"""

def init_all_index(n):
    """
    初始化n阶3维矩阵的索引
    :return:
    """
    return range(0, n * n * n)

def side_xz_index(n, i):
    """
    获取n阶3维矩阵的第i个xz面的索引
    :param n:
    :param i:
    :return:
    """
    assert i < n
    return range(i * n * n, i * n * n + n * n)

def side_yz_index(n, i):
    """
    获取n阶3维矩阵的第i个yz面的索引
    :param n:
    :param i:
    :return:
    """
    assert i < n
    return [x for x in range(i, n * n * n, n)]

def side_xy_index(n, i):
    """
    获取n阶3维矩阵的第i个xy面的索引
    :param n:
    :param i:
    :return:
    """
    assert i < n
    li = []
    start = n * i
    li.append(start)

    for x in range(n * n - 1):
        if (x + 1) % n == 0:
            up = (n - 1) * n + 1
        else:
            up = 1
        start = start + up
        li.append(start)
    return li

def clockwise_rotate(mat):
    """
    顺时针旋转90度
    :param mat:
    :return:
    """
    return numpy.rot90(mat, -1)

def counterclockwise_rotate(mat):
    """
    逆时针旋转90度
    :param mat:
    :return:
    """
    return numpy.rot90(mat, 1)

def generate_2_matrix_byarray(n, li=None):
    """
    根据数组生成n阶二维矩阵
    :param n:
    :param li:
    :return:
    """
    assert n * n == len(li)
    mat = numpy.array(li)
    mat.resize(n, n)
    return mat

if __name__ == "__main__":
    N = 3
    all_indexs = init_all_index(N)
    print generate_2_matrix_byarray(N, side_xz_index(N, 0))
    print generate_2_matrix_byarray(N, side_xz_index(N, 1))
    print generate_2_matrix_byarray(N, side_xz_index(N, 2))
