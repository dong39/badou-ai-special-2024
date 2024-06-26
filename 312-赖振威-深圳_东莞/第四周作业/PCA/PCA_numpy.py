# coding=utf-8

# 导入numpy库，并用np作为别名，numpy是Python中用于科学计算的一个库
import numpy as np

# 设置打印选项，将精度设置为 8
np.set_printoptions(precision=100)


# 定义一个名为PCA的类，用于实现主成分分析算法
class PCA():
    # 初始化方法，接收一个参数n_components表示要保留的主成分数量
    def __init__(self, n_components):
        # 将传入的参数n_components赋值给类的实例变量self.n_components
        self.n_components = n_components

    # 定义fit_transform方法，用于拟合数据并进行降维
    def fit_transform(self, X):
        print('输入的矩阵是：\n', X)
        print('矩阵大小:', X.shape)  # (6, 4)  查看输入的矩阵大小

        # 获取数据集X的特征数量，即变量self.n_features_
        self.n_features_ = X.shape[1]  # 打印列数/特征值

        print('矩阵各维度均值', X.mean(axis=0))

        # 中心化/零均值矩阵
        X = X - X.mean(axis=0)  # axis=0 按列算平均值  1就是按行算平均值
        print('中心化/零均值矩阵\n', X)

        # 计算协方差矩阵，协方差矩阵是原始数据集的转置与自身的点积，再除以样本数量
        # 求协方差矩阵  将输入的X矩阵的转置的X矩阵和X矩阵相乘，然后除以样本数量，以得到协方差矩阵的估计值
        self.covariance = np.dot(X.T, X) / X.shape[0]  # 转置的X矩阵和X矩阵相乘 / 样本数量
        print('输入矩阵的协方差矩阵:\n', self.covariance)
        '''得到协方差矩阵的无偏估计值。这是因为协方差的计算通常除以样本数量减去1来得到无偏估计值，但在这种情况下，由于PCA的目标是降维，我们只需除以样本数量即可。'''

        # 求协方差矩阵的特征值和特征向量
        eig_vals, eig_vectors = np.linalg.eig(self.covariance)
        # 使用格式化字符串打印特征值
        # print('矩阵的特征值\n', ["%.16f" % val for val in eig_vals])
        print('矩阵的特征值\n', eig_vals)
        print(
            '------------------------------------------------------------------------------------------------------------')
        print('矩阵的特征向量\n', eig_vectors)
        '''
        2.2981839465325771e+02 表示的数值为 (2.2981839465325771 \times 10^{2})，即229.81839465325771。
        8.1594502236905697e+00 表示的数值为 (8.1594502236905697 \times 10^{0})，即8.1594502236905697。
        3.9445510764770014e-02 表示的数值为 (3.9445510764770014 \times 10^{-2})，即0.039445510764770014。
        2.0938207233980437e+00 表示的数值为 (2.0938207233980437 \times 10^{0})，即2.0938207233980437。
        '''

        print(
            '------------------------------------------------------------------------------------------------------------')
        # 获得降序排列特征值的序号
        idx = np.argsort(-eig_vals)
        print('获得降序排列特征值的序号\n', idx)

        print(
            '------------------------------------------------------------------------------------------------------------')
        # 降维矩阵   拿取eig_vectors所有索引值，然后按照索引数组 idx 的顺序进行了重新排列。换句话说，它按照特征值的重要性顺序排列了特征向量。
        # self.components_ = eig_vectors[:,idx]

        # 降维矩阵
        # 选择前n个主成分，即前n个最大的特征值对应的特征向量
        # 选择了 eig_vectors 矩阵中的所有行，但是只选择了按照前 self.n_components 个最重要特征值排序后的特征向量。
        self.components_ = eig_vectors[:, idx[:self.n_components]]
        print('降维矩阵\n', self.components_)
        print("X:\n",X)
        '''
        取前 n_components 个特征值对应的索引。
        然后，eig_vectors[:,idx[:self.n_components]] 就是从特征向量矩阵中选取这些索引对应的列，
        即选取与最大的特征值对应的前 n_components 个特征向量。
        这样做的目的是将数据映射到前 n_components 个主成分所构成的空间中，实现数据的降维。
        '''

        print(
            '------------------------------------------------------------------------------------------------------------')

        # 使用选定的主成分对原始数据进行投影，得到降维后的数据
        # 对X进行降维    其维度是(4, 2)  6行2列的矩（6，2）
        print('对X进行降维\n', np.dot(X, self.components_))
        print(
            '------------------------------------------------------------------------------------------------------------')

        return np.dot(X, self.components_)


# 调用
# 创建PCA类的实例，指定要保留的主成分数量为2
pca = PCA(n_components=2)

# 导入数据集X，维度为4，这里是一个示例数据集
X = np.array([
    [-1, 2, 66, -1],
    [-2, 6, 58, -1],
    [-3, 8, 45, -2],
    [1, 9, 36, 1],
    [2, 10, 62, 1],
    [3, 5, 83, 2]
])
# 使用PCA实例对数据集X进行拟合和降维
newX = pca.fit_transform(X)  # 根据特征值的大小，选取前 n_components 个特征向量，构成降维矩阵。
print('newX方法返回结果:\n', newX)  # 输出降维后的数据
