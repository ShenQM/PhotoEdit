# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/FileManage.ui',
# licensing of 'UI/FileManage.ui' applies.
#
# Created: Sun Nov 18 22:33:33 2018
#      by: pyside2-uic  running on PySide2 5.11.1a1.dev1542405709
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_FileManage(object):
    def setupUi(self, FileManage):
        FileManage.setObjectName("FileManage")
        FileManage.resize(597, 261)
        self.groupBox = QtWidgets.QGroupBox(FileManage)
        self.groupBox.setGeometry(QtCore.QRect(60, 80, 481, 131))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 451, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_prefix = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_prefix.setObjectName("lineEdit_prefix")
        self.horizontalLayout.addWidget(self.lineEdit_prefix)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_suffix = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_suffix.setObjectName("lineEdit_suffix")
        self.horizontalLayout.addWidget(self.lineEdit_suffix)
        self.pushButton_rename = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_rename.setObjectName("pushButton_rename")
        self.horizontalLayout.addWidget(self.pushButton_rename)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 80, 451, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_dng2raw_recursive = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.checkBox_dng2raw_recursive.setObjectName("checkBox_dng2raw_recursive")
        self.horizontalLayout_3.addWidget(self.checkBox_dng2raw_recursive)
        self.pushButton_dng2raw = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_dng2raw.setObjectName("pushButton_dng2raw")
        self.horizontalLayout_3.addWidget(self.pushButton_dng2raw)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton_dng2jpeg = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_dng2jpeg.setObjectName("pushButton_dng2jpeg")
        self.horizontalLayout_3.addWidget(self.pushButton_dng2jpeg)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(FileManage)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(70, 20, 451, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_file_path = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_file_path.setObjectName("lineEdit_file_path")
        self.horizontalLayout_2.addWidget(self.lineEdit_file_path)
        self.pushButton_open_folder = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_open_folder.setObjectName("pushButton_open_folder")
        self.horizontalLayout_2.addWidget(self.pushButton_open_folder)

        self.retranslateUi(FileManage)
        QtCore.QMetaObject.connectSlotsByName(FileManage)

    def retranslateUi(self, FileManage):
        FileManage.setWindowTitle(QtWidgets.QApplication.translate("FileManage", "File Manage", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("FileManage", "Operation", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("FileManage", "Prefix:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("FileManage", "Suffix:", None, -1))
        self.pushButton_rename.setText(QtWidgets.QApplication.translate("FileManage", "Rename", None, -1))
        self.checkBox_dng2raw_recursive.setText(QtWidgets.QApplication.translate("FileManage", "Recursive", None, -1))
        self.pushButton_dng2raw.setText(QtWidgets.QApplication.translate("FileManage", "DNG2RAW", None, -1))
        self.pushButton_dng2jpeg.setText(QtWidgets.QApplication.translate("FileManage", "DNG2JEPG", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("FileManage", "File Path:", None, -1))
        self.pushButton_open_folder.setText(QtWidgets.QApplication.translate("FileManage", "Open", None, -1))

