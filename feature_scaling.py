import numpy as np

def auto_norm(dataset):  #对数据进行归一化，返回归一后矩阵，范围，最小值
    minval = dataset.min(0)
    maxval = dataset.max(0)
    ranges = maxval - minval
    for i in range(0, len(ranges)):
        if ranges[i] ==0:
            ranges[i] = 1
    norm_data = np.zeros (np.shape(dataset))
    m = dataset.shape[0]
    norm_data = dataset - np.tile(minval, (m,1))
    norm_data = norm_data/np.tile(ranges, (m,1))
    return norm_data, ranges, minval



