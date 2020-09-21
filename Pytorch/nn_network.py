# 使用pytorch.nn库实现神经网络
import torch
import torch.nn as nn

print(torch.cuda.is_available())
# N为多少训练数据；D_in输入数据的维度；H是中间层神经元个数；D_out输出数据的维度。
N, D_in, H, D_out = 64, 1000, 100, 10
# 随机创建训练数据
x = torch.randn(N, D_in)
y = torch.randn(N, D_out)
# 定义模型，GPU运行model = model.cuda()
model = nn.Sequential(
    nn.Linear(D_in, H),  # w_1 * x + b_1
    nn.ReLU(),
    nn.Linear(H, D_out)  # w_2 * h + b_2
)
# 初始化.
# nn.init.normal(model[0].weight)
# nn.init.normal(model[2].weight)
# 定义loss函数
loss_fn = nn.MSELoss(reduction="sum") 
# 学习率
learning_rate = 1e-4
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
for t in range(500):
    # 前向传播
    y_pred = model(x)  # y_pred为神经网络预测的输出值，直接帮做了model.forward()
    # 计算损失，使用minSqrtLoss
    loss = loss_fn(y_pred, y)
    print(t, loss.item())
    # 反向传播，计算gradient
    loss.backward()
    # 更新参数
    optimizer.step()
    optimizer.zero_grad()