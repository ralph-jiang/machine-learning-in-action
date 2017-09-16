import numpy as np
import feature_scaling
import classifier

#预测测试数据结果
def prediction(X, y, X_test, y_test, k):

    X_norm, X_range, X_min = feature_scaling.auto_norm(X)  # 归一化训练数据

    # 归一化测试数据
    norm_data_test = np.zeros(np.shape(X_test))
    m = X_test.shape[0]
    X_test_norm = X_test - np.tile(X_min, (m, 1))
    X_test_norm = X_test_norm / np.tile(X_range, (m, 1))

    #对测试数据进行分类并比较其预测标签和实际标签
    y_pre = []
    error_count = 0
    for i in range(0, np.size(X_test_norm, 0)):
        x_test = X_test_norm[i,:]
        y_pre.append(classifier.Return_Label(X_norm, y, x_test, k))
        print('The real label of ' + str(X_test[i]) + ' is ' + y_test[i],
             ', and the classified label of '+str(X_test[i])+' is ' + y_pre[i] +'!')
        if y_test[i] != y_pre[i]:
            error_count +=1

    precision = error_count/np.size(y_test)
    print('The prediction error rate is '+str(precision))


