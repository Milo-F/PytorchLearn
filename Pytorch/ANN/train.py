import torch
import numpy as np
from ANN import ANNModel

input_dim, hidden_dim, output_dim = 3, 140, 3
lr = 1e-3
train_rate, valid_rate, test_rate = 0.7, 0.1, 0.2
model = ANNModel(input_dim, hidden_dim, output_dim)
loss_fn = torch.nn.MSELoss(reduction = "sum")
optimizer = torch.optim.Adam(model.parameters(), lr)

# 创建随机数据
test_in = torch.randn(128, input_dim)
test_out = torch.randn(128, output_dim)

for times in range(500):
    pred_out = model.forward(test_in)
    loss = loss_fn(pred_out, test_out)
    print(times, loss.item())
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()









