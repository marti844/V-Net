import torch

# 加载预训练权重
pretrained_weights = torch.load('unet_vgg_voc.pth')  # 替换成你的预训练权重文件路径

# 初始化计数变量
conv_layer_count = 0
fc_layer_count = 0
pooling_layer_count = 0
activation_layer_count = 0
batch_norm_layer_count = 0
attention_layer_count = 0

# 遍历加载的权重字典的键，查找不同类型的层
for key in pretrained_weights.keys():
    if 'conv' in key:
        conv_layer_count += 1
    elif 'fc' in key:
        fc_layer_count += 1
    elif 'pool' in key:
        pooling_layer_count += 1
    elif 'activation' in key:
        activation_layer_count += 1
    elif 'batchnorm' in key:
        batch_norm_layer_count += 1
    elif 'attention' in key:
        attention_layer_count += 1

print("Number of Convolutional Layers:", conv_layer_count)
print("Number of Fully Connected Layers:", fc_layer_count)
print("Number of Pooling Layers:", pooling_layer_count)
print("Number of Activation Layers:", activation_layer_count)
print("Number of Batch Normalization Layers:", batch_norm_layer_count)
print("Number of Attention Mechanism Layers:", attention_layer_count)
