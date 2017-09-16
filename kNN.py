import error_rate_test
import read_data_file

#约会对象分类
#指定训练数据和测试数据文件
filename_traning =  'datingTestSet.txt'
filename_test = 'test1.txt'
k=3
num_column = 3   #文件内的列数（X的特征数）需要自己观察#
# 载入训练数据和测试数据
#X, y, y_num = read_data_file.Read_File(filename_traning, num_column)
#X_test, y_test, y_test_num = read_data_file.Read_File(filename_test, num_column)
#约会对象分类

#error_rate_test.prediction(X, y, X_test, y_test, k)


#手写数字分类
filepath_traning = 'trainingDigits'
filepath_test = 'testDigits'
k=3
X, y = read_data_file.read_directory_txt(filepath_traning)
X_test, y_test = read_data_file.read_directory_txt(filepath_test)



error_rate_test.prediction(X, y, X_test, y_test, k)