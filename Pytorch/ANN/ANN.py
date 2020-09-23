import torch
import torch.nn as nn


class ANNModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.l1 = nn.Linear(input_dim, hidden_dim, bias=True)
        self.f1 = nn.ReLU()
        self.l2 = nn.Linear(hidden_dim, hidden_dim, bias=True)
        self.f2 = nn.ReLU()
        self.l3 = nn.Linear(hidden_dim, hidden_dim, bias=True)
        self.f3 = nn.ReLU()
        self.l4 = nn.Linear(hidden_dim, hidden_dim, bias=True)
        self.f4 = nn.ReLU()
        self.l5 = nn.Linear(hidden_dim, hidden_dim, bias=True)
        self.f5 = nn.ReLU()
        self.l6 = nn.Linear(hidden_dim, output_dim, bias=True)
        # self.f6 = nn.ReLU()


    def forward(self, inputs):
        outputs = self.l1(inputs)
        outputs = self.f1(outputs)
        outputs = self.l2(outputs)
        outputs = self.f2(outputs)
        outputs = self.l3(outputs)
        outputs = self.f3(outputs)
        outputs = self.l4(outputs)
        outputs = self.f4(outputs)
        outputs = self.l5(outputs)
        outputs = self.f5(outputs)
        outputs = self.l6(outputs)
        # outputs = self.f6(outputs)
        return outputs
