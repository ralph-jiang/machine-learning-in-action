import numpy as np
import os

filepath = 'testDigits'
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
    return X, y

