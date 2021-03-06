import numpy as np
# 波士顿房价数据
from sklearn.datasets import load_boston
# 正规方程/梯度下降
from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# 均方误差   metrics算法性能衡量包
from sklearn.metrics import mean_absolute_error


def main():
    # 矩阵运算[必须得是2维]
    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    b = [[2], [1], [3], [4]]
    res = np.dot(a, b)
    print(res)
    pass


# 线性回归
def line_test():
    # 获取数据
    lb = load_boston()
    # 分割数据集到训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(lb.data, lb.target, test_size=0.25)
    print(y_train, '\n', y_test)

    # 进行数据标准化处理(特征值与目标值都得标准化-目标值根据特征值求出[参考公式]) [两个标准化api:特征值[多列]/目标值[因为只有一列]]
    # 特征是
    std_x = StandardScaler()
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)
    # 目标值
    std_y = StandardScaler()

    std_y.fit_transform(y_train.reshape(-1, 1))  # 等同于以下写法 n行1列
    # std_y.fit_transform(y_train.reshape(len(y_train),1))
    std_y.transform(y_test.reshape(-1, 1))
    # estimator预测
    print('*' * 100)
    # 正规方程求解方式预测结果
    lr = LinearRegression()
    lr.fit(x_train, y_train)

    print(lr.coef_)

    # 进行预测结果
    res = lr.predict(x_test)
    print('结果：\n', res)
    # 将标准化结果转为真实结果
    print('真实结果：\n', std_y.inverse_transform(res))

    # 均方误差测试 真实值测试
    print('均方误差测试：\n', mean_absolute_error(std_y.inverse_transform(y_test), std_y.inverse_transform(res)))
    pass


# 梯度下降测试
def sgd_test():
    # 获取数据
    lb = load_boston()
    # 分割数据集到训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(lb.data, lb.target, test_size=0.25)
    print(y_train, '\n', y_test)

    # 进行数据标准化处理(特征值与目标值都得标准化-目标值根据特征值求出[参考公式]) [两个标准化api:特征值[多列]/目标值[因为只有一列]]
    # 特征值 标准化
    std_x = StandardScaler()
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)

    # 目标值 标准化
    std_y = StandardScaler()
    # 参数得是二维
    y_train = std_y.fit_transform(y_train.reshape(-1, 1))
    y_test = std_y.transform(y_test.reshape(-1, 1))

    # 梯度下降进行预测
    sg = SGDRegressor()

    sg.fit(x_train, y_train)

    print(sg.coef_)

    # 进行预测
    x_predict_res = sg.predict(x_test)
    # 将标准化结果反转为非标准化之前的
    stand_pre = std_y.inverse_transform(x_predict_res)
    print(stand_pre)

    # 真实样本 分割数据集的预测结果 与 梯度下降的结果
    print('均方误差测试：\n', mean_absolute_error(std_y.inverse_transform(y_test), std_y.inverse_transform(x_predict_res)))

    pass


# 岭回归
def ridge():
    # 获取数据
    lb = load_boston()
    # 分割数据集到训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(lb.data, lb.target, test_size=0.25)
    print(y_train, '\n', y_test)

    # 进行数据标准化处理(特征值与目标值都得标准化-目标值根据特征值求出[参考公式]) [两个标准化api:特征值[多列]/目标值[因为只有一列]]
    # 特征值 标准化
    std_x = StandardScaler()
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)

    # 目标值 标准化
    std_y = StandardScaler()
    # 参数得是二维
    y_train = std_y.fit_transform(y_train.reshape(-1, 1))
    y_test = std_y.transform(y_test.reshape(-1, 1))

    # 岭回归 alpha[0~1 1～10](超参数)正则化系数默认1.0
    ri = Ridge(alpha=1.0)

    ri.fit(x_train,y_train)

    # 回归系数
    print('回归系数：\n',ri.coef_)

    # 进行预测
    pre_res=ri.predict(x_test)
    # 展示真实数据
    res=std_y.inverse_transform(pre_res)

    print('均方误差测试：\n', mean_absolute_error(std_y.inverse_transform(y_test), res))


    pass


if __name__ == '__main__':
    # main()
    # line_test()
    # sgd_test()
    ridge()
