import os
import shutil
import time

import cv2
import numpy as np
from PIL import Image

from unet import Unet
from cut_image import cut_one_jpg

if __name__ == "__main__":

    mode = "predict"
    # -------------------------------------------------------------------------#
    #   count               指定了是否进行目标的像素点计数（即面积）与比例计算
    #   name_classes        区分的种类，和json_to_dataset里面的一样，用于打印种类和数量
    # -------------------------------------------------------------------------#
    count = False

    name_classes    = ["background","aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
    unet = Unet()


    # 如果存在img_tmp则删除
    if os.path.exists('img_tmp'):
        shutil.rmtree('img_tmp')
    os.mkdir('img_tmp')


    crop_size = (512, 512)
    path = r'img'
    save_path = r'img_tmp'
    file = '2 copy.jpg'

    img = cv2.imread(os.path.join(path, file))

    merge_img = np.zeros((img.shape[0], img.shape[1]))

    cut_one_jpg(crop_size=crop_size, path=path, save_path=save_path, file=file)
    image_files = os.listdir("img_tmp")
    for image_file in image_files:
        image = Image.open("img_tmp/" + image_file)
        r_image = unet.detect_image(image, count=count, name_classes=name_classes)

        _, row, col = image_file.split('_')
        row = int(row)
        col = int(col.replace(".jpg", ""))
        merge_img[row:row + crop_size[0], col:col + crop_size[1]] = r_image


    merge_img[merge_img == 1] = 255

    cv2.imwrite("img_out/" + file.replace(".jpg", ".png"), merge_img)




