import os

import rawpy


def dng2raw(file_name):
    if os.path.exists(file_name) and (os.path.splitext(file_name)[1] == ".dng"
                                      or os.path.splitext(file_name)[1] == ".DNG"
                                      or os.path.splitext(file_name)[1] == ".GPR"):
        print("processing: " + file_name)
        with rawpy.imread(file_name) as raw:
            cfa_raw = raw.raw_image.copy()
            sz = cfa_raw.shape
            cfa_raw.tofile(file_name+"H"+str(sz[0])+"W"+str(sz[1])+"B2.raw")


def dng2raw_batch(path, recursive=True):
    if os.path.exists(path):
        if recursive:
            for root, dirs, files in os.walk(path):
                for name in files:
                    file_path = os.path.join(root, name)
                    dng2raw(file_path)
                    print(file_path)
        else:
            lists = os.listdir(path)
            for line in lists:
                file_path = os.path.join(path, line)
                if not os.path.isdir(file_path):
                    dng2raw(file_path)


file_dir = r'F:\DCIM'
dng2raw_batch(file_dir, True)