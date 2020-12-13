from imutils import paths 
import numpy as np 
import cv2
import os
import random
import argparse
import pickle

## 转换标签
def transform_label(img_file_name):
    
    ## 原标签
    provinces = ["皖", "沪", "津", "渝", "冀", "晋", "蒙", "辽", "吉", "黑", "苏", "浙", "京", "闽", "赣", "鲁", "豫", "鄂", "湘", "粤", "桂", "琼", "川", "贵", "云", "藏", "陕", "甘", "青", "宁", "新", "警", "学", "O"]
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                'X', 'Y', 'Z', 'O']
    ads = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'O']

    ## 图片名是按照 - 分隔的四部分数据
    area, tilte_degree, bounding_box_coordinates, vertical_locations, LPRNumber,_,__ = img_file_name.split('-',6)

    ## 每个数据内部又是用 _ 分割
    leftup_point, rightbottom_point = bounding_box_coordinates.split("_",1)
    
    ## 坐标内又是用 & 分割xy， 以下得到矩阵左上角xy和右下角xy，因此表示方式目前是xyxy, 而非xywh，后续可以自行修改
    leftup_point_x = int(leftup_point.split('&',1)[0])
    leftup_point_y = int(leftup_point.split('&',1)[1])

    right_point_x = int(rightbottom_point.split("&",1)[0])
    right_point_y = int(rightbottom_point.split("&",1)[1])

    provinces_index, alphabet_index, ads_index_list = LPRNumber.split("_", 6)

    province = provinces[int(provinces_index)]
    alphabet = alphabets[int(alphabet_index)]
    ad_list = [ads[int(x)] for x in ads_index_list]


    ## 展示最终结果，代码中应该用不到，仅供自己查看确认程序无误
    final_label = province + '·' + alphabet + ''.join(ad_list)
    print(final_label)


## 裁切图片得到局部车牌图像并保存
def crop(img_file_name, up_y, down_y, left_x, right_x):
    img = cv2.imread(img_file_name)  ## 图片经过cv2读入后变为一个张量，shape: [height, width, 3]，3即RGB三个通道
    img_crop = img[up_y:down_y + 1, left_x: right_x + 1,:]  ## 裁切时第三维颜色通道保留
    
    
    save_dir = 'your_direction/' + 'figure label' + '.jpg'
    cv2.imencode(".jpg", img_crop)[1].tofile(dir)  ## 如果save_dir文件名中有中文，例如此处已经将数据集的标注转换为京A11111，则需要用这个方式保存，如果没有中文可直接cv2.imwrite()保存










