import torchvision
import numpy as np
import tensorflowjs as tfjs
import torch
from torch.autograd import Variable
from pytorch2keras.converter import pytorch_to_keras

pretrained_model = torchvision.models.densenet121(pretrained = True)
pretrained_model = pretrained_model.float()
img_size = 224
input_np = np.random.uniform(0, 1, (1, 3, img_size, img_size))
input_dummy = Variable(torch.FloatTensor(input_np))
k_model = pytorch_to_keras(pretrained_model, input_dummy, [(3, img_size, img_size,)], verbose=True, names="short")
tfjs.converters.save_keras_model(k_model, "DenseNet121")
