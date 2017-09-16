import numpy as np
import os

def convert_label_num(y):  #返回y的数字标记形式
    ids = list(set(y))
    y_label_num = np.zeros(np.size(y))
    for i in range(0, np.size(ids)):
        for j in range(0, np.size(y)):
            if ids[i] == y[j]:
                y_label_num[j] = i
    return y_label_num


def Read_File(filename, num_column):   #读取存在同一个txt文件中的X,y,及y数字标记#
    fr=open(filename, 'r')
    row_file=fr.readlines()
    num_row = len(row_file)
    mat_file = np.zeros((num_row, num_column))
    index = 0
    class_label = []
    fr.close()
    for line in row_file:
        line = line.strip()
        list = line.split('\t')
        mat_file[index, :] = list[0:num_column]
        class_label.append(list[-1])
        index +=1
    y_num = convert_label_num(class_label)
    return mat_file, class_label, y_num

#调用方法
#filename = 'datingTestSet.txt'
#num_column = 3
#X, y = Read_File(filename, num_column)


def read_directory_txt(filepath):   #读取文件夹内所有txt文件,返回X，y
    pathDir = os.listdir(filepath)
    X=[]
    y=[]
    for filename in pathDir:
        y.append(filename[0])
        fr = open(filepath+'/'+filename, 'r')
        x=[]
        for i in range(0, 32):
            row_file = fr.readline()
            for j in row_file:
                if j != '\n':
                    x.append(int(j))
        X.append(x)
    X= np.array(X)
    return X, y

#调用方法
#filepath = 'testDigits'
#X, y = read_directory_txt(filepath)
#print(np.shape(X))
#print(X.max(0))
