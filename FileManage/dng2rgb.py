import os
import rawpy
import imageio

import file_manage


def dng2rgb(file_name):
    with rawpy.imread(file_name) as raw:
        rgb = raw.postprocess()
        return rgb


def dng2jpeg_batch(dng_dir):
    dng_files = file_manage.list_files(dng_dir, '.DNG', True)
    for file in dng_files:
        print('Transforming: ' + file)
        rgb = dng2rgb(file)
        filename = os.path.splitext(file)[0]
        imageio.imsave(filename + '.jpeg', rgb)


dng2jpeg_batch('E:\Projects\data')