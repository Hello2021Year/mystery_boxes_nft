import os
import random


def shuffle(filepath):
    file_list = []
    files = os.listdir(filepath)
    for filename in files:
        tmp_file = filepath + "/" + filename
        sub_files = os.listdir(tmp_file)
        file_list = file_list + sub_files

    return file_list

# 获取所有的文件名，并进行shuffle
file_list = shuffle('image')
random.shuffle(file_list)