# torch和numpy功能的比较
import torch
import numpy as np

np_data = np.arange(6).reshape((2, 3))
torch_data = torch.from_numpy(np_data)  # numpy to torch(tensor)
torch2array = torch_data.numpy()  # torch(tensor) to numpy(array)
print(
    "\nnp_data:", np_data,
    "\ntorch_data:", torch_data,
    "\ntorch2array:", torch2array
)
