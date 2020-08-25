# 用numpy实现简单的神经网络
import numpy as np
# N为多少训练数据；D_in输入数据的维度；H是中间神经元个数；D_out输出数据的维度。
N, D_in, H, D_out = 64, 1000, 100, 10
# 随机创建训练数据
x = np.random.randn(N, D_in)
y = np.random.randn(N, D_out)
# 权重
w1 = np.random.randn(D_in, H)
w2 = np.random.randn(H, D_out)
# 学习率
learning_rate = 1e-6
for t in range(500):
    # 前向传播
    h = x.dot(w1)  # x是N*D_in大小的矩阵，w1是D_in*H大小的矩阵，运算之后会得到h为N*H的矩阵
    h_relu = np.maximum(h, 0)  # relu激励函数
    y_pred = h_relu.dot(w2)  # y_pred为神经网络预测的输出值
    # 计算损失，使用minSqrtLoss
    loss = np.square(y_pred - y).sum()
    print(t, loss)
    # 反向传播，计算gradient
    grad_y_pred = 2.0 * (y_pred - y)
    grad_w2 = h_relu.T.dot(grad_y_pred)
    grad_h_relu = grad_y_pred.dot(w2.T)
    grad_h = grad_h_relu.copy()
    grad_h[h < 0] = 0
    grad_w1 = x.T.dot(grad_h)
    # 更新权重
    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2
