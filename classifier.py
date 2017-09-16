import numpy as np
import read_data_file
import graph_plot
import feature_scaling

#计算测试点离样本点的距离，返回距离的排序索引
def Distance_Index(X,x_test):
    distace = np.zeros(np.size(X, 0))
    m = np.size(X, 0)
    for i in range(0,m):
        distace[i] = (sum((x_test-X[i,:])**2))**0.5
    return  distace.argsort()

#返回离测试点最近的K个样本点对应的标签出现最多次数的标签名称
def Return_Label(X, y, x_test,k):
    sort_index = Distance_Index(X, x_test)
    ids = list(set(y))
    label_y = np.zeros(np.shape(ids))
    for i in sort_index[0:k]:
        for j in range(0,np.size(ids)):
            if y[i] == ids[j]:
                label_y[j] +=1
    b=np.argmax(label_y)
    return ids[b]
#调用方法示例：
#x1 = [3.0, 4.0]
#X, y = creatDateSet()
#k = 3
#Return_Label(X, y, x1, k)



#x1 = [20000, 0, 1.1]  #(示例方法)手动输入样本点，查看其分类

#filename = 'datingTestSet.txt'
#num_column = 3   #文件内的列数（X的特征数）需要自己观察#
#X, y, y_num = read_data_file.Read_File(filename, num_column)
#X_norm, X_range, X_min = feature_scaling.auto_norm(X)

#x_test = x1-X_min
#x_test = x_test/X_range
#result = Return_Label(X_norm, y, x_test, 20)
#print('The classified label of '+str(x1)+' is '+ result)


#graph_plot.plot_scatter_2D(X[:,1], X[:,2], y_num)