# 用pytorch实现简单的神经网络
import torch
print(torch.cuda.is_available())
# N为多少训练数据；D_in输入数据的维度；H是中间神经元个数；D_out输出数据的维度。
N, D_in, H, D_out = 64, 1000, 100, 10
# 随机创建训练数据
x = torch.randn(N, D_in)
y = torch.randn(N, D_out)
# 权重
w1 = torch.randn(D_in, H, requires_grad=True) # 声明存在grad
w2 = torch.randn(H, D_out, requires_grad=True)
# 学习率
learning_rate = 1e-6
for t in range(500):
    # 前向传播
    y_pred = x.mm(w1).clamp(min = 0).mm(w2)  # y_pred为神经网络预测的输出值
    # 计算损失，使用minSqrtLoss
    loss = (y_pred - y).pow(2).sum()
    print(t, loss.item())
    # 反向传播，计算gradient
    loss.backward()
    # 更新权重
    with torch.no_grad():# no_grad这个上下文管理器，在作用域内只做计算，不记录计算图。
        w1 -= learning_rate * w1.grad
        w2 -= learning_rate * w2.grad
        # 由于pytorch计算梯度每次计算会累加，故需要每次对grad进行清零
        w1.grad.zero_()
        w2.grad.zero_()
    
