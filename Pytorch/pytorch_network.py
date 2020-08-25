# 用pytorch实现简单的神经网络
import torch
# N为多少训练数据；D_in输入数据的维度；H是中间神经元个数；D_out输出数据的维度。
N, D_in, H, D_out = 64, 1000, 100, 10
# 随机创建训练数据
x = torch.randn(N, D_in)
y = torch.randn(N, D_out)
# 权重
w1 = torch.randn(D_in, H)
w2 = torch.randn(H, D_out)
# 学习率
learning_rate = 1e-6
for t in range(500):
    # 前向传播
    h = x.mm(w1)  # x是N*D_in大小的矩阵，w1是D_in*H大小的矩阵，运算之后会得到h为N*H的矩阵
    h_relu = h.clamp(min = 0)  # relu激励函数
    y_pred = h_relu.mm(w2)  # y_pred为神经网络预测的输出值
    # 计算损失，使用minSqrtLoss
    loss = (y_pred - y).pow(2).sum().item()
    print(t, loss)
    # 反向传播，计算gradient
    grad_y_pred = 2.0 * (y_pred - y)
    grad_w2 = h_relu.t().mm(grad_y_pred)
    grad_h_relu = grad_y_pred.mm(w2.t())
    grad_h = grad_h_relu.clone()
    grad_h[h < 0] = 0
    grad_w1 = x.t().mm(grad_h)
    # 更新权重
    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2
