import os
import cv2
import numpy as np


def cut_one_jpg(crop_size, save_path, file, path='./'):
    # 读取图片
    image = cv2.imread(path + '/' + file)

    # 获取图片的大小
    height, width, _ = image.shape

    # 切割图片
    for i in range(0, height, crop_size[0]):
        for j in range(0, width, crop_size[1]):
            # 如果剩余空间小于512，那么从图像边缘反向切割
            if i + crop_size[0] > height and j + crop_size[1] > width:
                row = height - crop_size[0]
                col = width - crop_size[1]
                crop_img = image[row:, col:, :]
            elif i + crop_size[0] > height:
                row = height - crop_size[0]
                col = j
                crop_img = image[row:, col:col + crop_size[1], :]
            elif j + crop_size[1] > width:
                row = i
                col = width - crop_size[1]
                crop_img = image[row:row + crop_size[0], col:, :]
            else:
                row = i
                col = j
                crop_img = image[row:row + crop_size[0], col:col + crop_size[1], :]
            # 存储切割的图片
            cv2.imwrite(save_path + f"/{file[:-4]}_{row}_{col}.jpg", crop_img)


def cut_one_png(crop_size, save_path, file, path='./'):
    # 读取图片
    image = cv2.imread(path + '/' + file, cv2.IMREAD_GRAYSCALE)

    image[image != 0] = 1

    # 获取图片的大小
    height, width = image.shape

    # 切割图片
    for i in range(0, height, crop_size[0]):
        for j in range(0, width, crop_size[1]):
            # 如果剩余空间小于224，那么从图像边缘反向切割
            if i + crop_size[0] > height and j + crop_size[1] > width:
                row = height - crop_size[0]
                col = width - crop_size[1]
                crop_img = image[row:, col:]
            elif i + crop_size[0] > height:
                row = height - crop_size[0]
                col = j
                crop_img = image[row:, col:col + crop_size[1]]
            elif j + crop_size[1] > width:
                row = i
                col = width - crop_size[1]
                crop_img = image[row:row + crop_size[0], col:]
            else:
                row = i
                col = j
                crop_img = image[row:row + crop_size[0], col:col + crop_size[1]]
            # 存储切割的图片
            cv2.imwrite(save_path + f"/{file[:-4].replace('_1', '')}_{row}_{col}.png", crop_img)



def cut_jpg(crop_size=(224, 224), path=r'data/jpg', save_path=r'data/jpg_224'):
    files = os.listdir(path)
    for file in files:
        cut_one_jpg(crop_size, save_path, file, path)




def cut_png(crop_size=(224, 224), path=r'data/png', save_path=r'data/png_224'):
    files = os.listdir(path)
    for file in files:
        cut_one_png(crop_size, save_path, file, path)



if __name__ == '__main__':
    cut_jpg(crop_size=(512, 512), path=r'data/jpg', save_path=r'VOCdevkit/VOC2007/JPEGImages')
    cut_png(crop_size=(512, 512), path=r'data/png', save_path=r'VOCdevkit/VOC2007/SegmentationClass')








# import glob
#
# # 读取所有的切割图片
# image_files = glob.glob("data/jpg_224/*.jpg")
# # 按照文件名进行排序，确保图片的顺序正确
# image_files.sort()
#
#
# # 获取切割图片的数量
# num_images = len(image_files)
#
# # 读取第一张图片以获取图片的大小
# temp_img = cv2.imread(image_files[0])
# height, width, _ = temp_img.shape
#
# # 计算原始大图在行和列方向上的图片数量
# num_rows = 3648 // height
# num_cols = 5472 // width
#
# # 初始化一个空列表来存储所有的图片
# images = []
# for i in range(num_rows):
#     row_imgs = []
#     for j in range(num_cols):
#         # 检查是否为最后一行
#         if i == num_rows - 1:
#             img = cv2.imread(image_files[i * num_cols + num_cols - 1 - j])
#         else:
#             img = cv2.imread(image_files[i * num_cols + j])
#         row_imgs.append(img)
#     images.append(row_imgs)
#
# # 将图片在行和列方向上进行拼接
# merged_image = np.concatenate([np.concatenate(row_images, axis=1) for row_images in images], axis=0)
#
#
# # 将拼接后的图片保存
# cv2.imwrite("data/merged_image.jpg", merged_image)
#
# print(merged_image.shape)

