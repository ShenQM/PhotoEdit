# Time: 2018/11/11
# Author: Shen Quanmin
# Email: chen_qm@163.com

import os
import math

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QPixmap, QImage
from skimage import img_as_ubyte
import matplotlib.pyplot as plt

from FileManage import FileList


def image2QPixelmap(image):
    image = img_as_ubyte(image)
    img = QImage(image.data, image.shape[1], image.shape[0],
                 image.strides[0], QImage.Format_RGB888)
    pixmap = QPixmap.fromImage(img)
    return pixmap


class WorkWidget(QtWidgets.QWidget):
    def __init__(self):
        super(WorkWidget, self).__init__()
        folder = r'E:\Projects\data'
        self.load_folder(folder=folder)
        # self.label = QtWidgets.QLabel(self)
        # self.label_1 = QtWidgets.QLabel(self)
        # file_path = r'E:\Projects\EC1704\Calibration_Station\Dust_Inspection_20181101\data_20181102\160118529655\160118529655.PNG'
        # self.pixmap = QtGui.QPixmap(file_path)
        # self.label.setPixmap(self.pixmap)
        # self.label_1.setPixmap(self.pixmap)
        #
        # self.layout = QtWidgets.QGridLayout(self)
        # self.layout.addWidget(self.label, 0, 0)
        # self.layout.addWidget(self.label_1, 0, 1)

    def load_folder(self, folder=''):
        if os.path.exists(folder):
            self.file_list = FileList.FileList(folder)
            self.scroll = QtWidgets.QScrollArea(self)
            self.scroll.setWidgetResizable(True)
            self.pixmap = []
            self.label = []
            self.widget = QtWidgets.QWidget(self)
            self.widget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            self.column_num = math.floor(1920/130)
            self.layout = QtWidgets.QGridLayout(0, self.column_num)
            self.layout.setHorizontalSpacing(10)
            self.layout.setVerticalSpacing(10)

            # self.column_num = 10
            print('{}_{}'.format(self.column_num, self.width()))
            r = 0
            c = 0
            for i in range(len(self.file_list.rgb_obj)):
                print(i)
                self.pixmap.append(image2QPixelmap(self.file_list.rgb_obj[i].thumbnail))
                #self.pixmap.append(QtGui.QPixmap(self.pixmap[i]))
                self.label.append(QtWidgets.QLabel(self))
                self.label[i].setPixmap(self.pixmap[i])
                r = math.floor(i/self.column_num)
                c = i % self.column_num
                self.layout.addWidget(self.label[i], r, c)
            print('{}_{}'.format(r, c))
            spacer = QtWidgets.QSpacerItem(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            self.layout.addItem(spacer, r+1, 0)
            self.scroll.setWidget(self.widget)
            self.scroll.resize(1920, 1080)
            print('{}_{}'.format(self.column_num, self.width()))



if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWin = WorkWidget()
    mainWin.showMaximized()
    sys.exit(app.exec_())
