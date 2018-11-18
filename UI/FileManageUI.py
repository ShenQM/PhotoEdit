# Time: 2018/11/18
# Author: Shen Quanmin
# Email: chen_qm@163.com
import sys

from PySide2 import QtCore, QtGui, QtWidgets

from UI import FileManage_ui

from FileManage import file_manage, dng2raw


class FileManageUI(QtWidgets.QWidget, FileManage_ui.Ui_FileManage):
    def __init__(self):
        super(FileManageUI, self).__init__()
        self.setupUi(self)

        self.pushButton_open_folder.clicked.connect(self.open_folder)

        self.pushButton_rename.clicked.connect(self.rename)

        self.pushButton_dng2raw.clicked.connect(self.dng2raw)

    def open_folder(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Open Folder",
                QtCore.QDir.currentPath())
        self.lineEdit_file_path.setText(directory)

    def rename(self):
        print(self.lineEdit_file_path.text())
        file_manage.add_pre_suffix(self.lineEdit_file_path.text(), extension='',
                                   prefix=self.lineEdit_prefix.text(), suffix=self.lineEdit_suffix.text(),
                                   recursive=False)

    def dng2raw(self):
        dng2raw.dng2raw_batch(self.lineEdit_file_path.text(), self.checkBox_dng2raw_recursive.isChecked())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    mainWindow = FileManageUI()
    mainWindow.show()
    sys.exit(app.exec_())
