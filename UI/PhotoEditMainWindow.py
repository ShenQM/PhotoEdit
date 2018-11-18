# Time: 2018/11/08
# Author: Shen Quanmin
# Email: chen_qm@163.com

from PySide2 import QtCore, QtGui, QtWidgets


class PhotoEditMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(PhotoEditMainWindow, self).__init__()

        self.create_actions()

        self.create_menus()

    def create_actions(self):
        self.open_act = QtWidgets.QAction(QtGui.QIcon(':/images/open.png'),
                "&Open folder", self, shortcut=QtGui.QKeySequence.Open,
                statusTip="Open an existing file", triggered=self.open_folder)

    def create_menus(self):
        self.file_menu = self.menuBar().addMenu("&File")
        self.file_menu.addAction(self.open_act)

    def open_folder(self):
        # if self.maybeSave():
        dir = QtWidgets.QFileDialog.getExistingDirectory(self)
        print(dir)
        #     if fileName:
        #        self.loadFile(fileName)


if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWin = PhotoEditMainWindow()
    mainWin.show()
    sys.exit(app.exec_())
