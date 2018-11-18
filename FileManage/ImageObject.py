# Time: 2018/11/11
# Author: Shen Quanmin
# Email: chen_qm@163.com

import os

import imageio
import matplotlib
import matplotlib.pyplot as plt
from skimage import io
import skimage


class ImageObject:
    def __init__(self, file_path=''):
        print('test')
        self.file_path = file_path
        self.org_image = io.imread(self.file_path)
        self.thumbnail = skimage.transform.resize(self.org_image, (90, 120), mode='reflect')
        # print('test')
        # plt.imshow(self.org_image)
        # plt.imshow(self.thumbnail)
        # plt.show()


if __name__ == '__main__':
    file_path = r'E:\Projects\EC1704\Calibration_Station\Dust_Inspection_20181101\data_20181102\160118529655\160118529655.PNG'
    image_obj = ImageObject(file_path=file_path)