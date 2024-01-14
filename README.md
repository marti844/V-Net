### 使用说明

1. 将图片放入VOCdevkit
2. 运行voc_annotation.py，生成train.txt和test.txt
3. 运行train.py，开始训练，在这里面可以设置很多参数。

### 文件说明

1. img文件夹，里面是一些测试图片
2. img_out文件夹，里面是测试图片的输出结果
3. logs文件夹，里面是训练的日志
4. model_data文件夹，里面是unet的预训练模型
5. utils文件夹，里面是一些工具文件
6. VOCdevkit文件夹，里面是数据集
7. cut_image.py，用于将细胞图片和标签切割成指定大小
8. get_miou.py，用于计算miou
9. json_to_dataset.py，用于将json文件转换成数据集
10. predict.py，用于预测，输入输出都是原图大小
11. summary.py，用于计算模型参数
12. train.py，用于训练，很多可选参数
13. unet.py，用于预测的unet模型
14. voc_annotation.py，用于生成train.txt和test.txt


### 所需环境
torch==1.2.0    
torchvision==0.4.0   


### 训练步骤
#### 一、训练voc数据集
1、将voc数据集放入VOCdevkit中（无需运行voc_annotation.py）。  
2、运行train.py进行训练。  

#### 二、训练自己的数据集
1、本文使用VOC格式进行训练。  
2、训练前将标签文件放在VOCdevkit文件夹下的VOC2007文件夹下的SegmentationClass中。    
3、训练前将图片文件放在VOCdevkit文件夹下的VOC2007文件夹下的JPEGImages中。    
4、在训练前利用voc_annotation.py文件生成对应的txt。    
5、注意修改train.py的num_classes为分类个数+1。    
6、运行train.py即可开始训练。  

#### 三、训练医药数据集
1、下载VGG的预训练权重到model_data下面。  
2、调整参数参数运行train.py即可开始训练。

### 预测步骤
1. 按照训练步骤训练。    
2. 在unet.py文件里面，在如下部分修改model_path、backbone和num_classes使其对应训练好的文件；**model_path对应logs文件夹下面的权值文件**。    
```python
_defaults = {
    #-------------------------------------------------------------------#
    #   model_path指向logs文件夹下的权值文件
    #   训练好后logs文件夹下存在多个权值文件，选择验证集损失较低的即可。
    #   验证集损失较低不代表miou较高，仅代表该权值在验证集上泛化性能较好。
    #-------------------------------------------------------------------#
    "model_path"    : 'model_data/unet_vgg_voc.pth',
    #--------------------------------#
    #   所需要区分的类的个数+1
    #--------------------------------#
    "num_classes"   : 21,
    #--------------------------------#
    #   所使用的的主干网络：vgg、resnet50   
    #--------------------------------#
    "backbone"      : "vgg",
    #--------------------------------#
    #   输入图片的大小
    #--------------------------------#
    "input_shape"   : [512, 512],
    #--------------------------------#
    #   blend参数用于控制是否
    #   让识别结果和原图混合
    #--------------------------------#
    "blend"         : True,
    #--------------------------------#
    #   是否使用Cuda
    #   没有GPU可以设置成False
    #--------------------------------#
    "cuda"          : True,
}
```
3. 运行predict.py，输入    
```python
img/street.jpg
```

### 评估步骤
1、设置get_miou.py里面的num_classes为预测的类的数量加1。  
2、设置get_miou.py里面的name_classes为需要去区分的类别。  
3、运行get_miou.py即可获得miou大小。  

