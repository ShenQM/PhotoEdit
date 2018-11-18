# Time: 2018/11/11
# Author: Shen Quanmin
# Email: chen_qm@163.com

import os

from FileManage import ImageObject


def get_file_list(path='', rgb_suffix=['.jpeg', '.jpg', '.JPEG'], raw_suffix=['.dng', '.DNG']):
    folder_list = []
    rgb_list = []
    raw_list = []
    unknown_list = []
    if os.path.exists(path=path):
        dirs = os.listdir(path)
        for file in dirs:
            file_name, file_suffix = os.path.splitext(file)
            full_path = os.path.join(path, file)
            if os.path.isdir(full_path):
                folder_list.append(full_path)
            elif file_suffix in rgb_suffix:
                rgb_list.append(full_path)
            elif file_suffix in raw_suffix:
                raw_list.append(full_path)
            else:
                unknown_list.append(full_path)
    return folder_list, rgb_list, raw_list, unknown_list


class FileList:
    def __init__(self, folder=''):
        self.file_list = []
        self.rgb_obj = []
        print(folder)
        self.create_image_list(folder=folder)

    def create_image_list(self, folder=''):
        folder_list, rgb_list, raw_list, unknown_list = get_file_list(folder)
        for file in rgb_list:
            self.rgb_obj.append(ImageObject.ImageObject(file))


if __name__ == '__main__':
    folder = r'E:\Projects\data'
    file_list = FileList(folder)