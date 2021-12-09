# encoding=utf-8
# coding=utf-8
import os
from posixpath import basename
import sys
import threading
from os import listdir
from os.path import isfile, join
from PIL import Image
reload(sys)
sys.setdefaultencoding("utf-8")

size = (1242, 2688)
riato = float(size[0])/size[1]
dir = ""
images = []


def find_all_pic(dirName):
    if not os.path.exists(dirName):
        return
    if os.path.isdir(dirName):
        for file in listdir(dirName):
            find_all_pic(join(dirName, file))
    elif os.path.isfile(dirName) and (dirName.endswith(".png") or dirName.endswith(".jpg")):
        images.append(dirName)


def multi_thread():
    threads = []
    for image in images:
        threads.append(
            threading.Thread(target=cut_pic, args=(dir, image))
        )
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print("==== finish ====")


def mk_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def rm_if_exit(dir_name):
    if os.path.isdir(dir_name) and os.path.exists(dir_name):
        os.removedirs(dir_name)


def cut_pic(dir, path):
    base_name = os.path.basename(dir)
    paths = path.split("/"+base_name+"/")
    output_path = paths[0]+"/" + base_name + "_cutter"+"/"+paths[1]
    mk_dir(os.path.dirname(output_path))
    print(output_path)

    source_img = Image.open(path)
    img_size = source_img.size
    x = 0
    y = 0
    img_riato = float(img_size[0])/img_size[1]
    print("处理开始 => 原图尺寸{}".format(img_size))
    if img_riato > riato:
        h = img_size[1]
        w = float(h)/size[1]*size[0]
        y = 0
        if (img_size[0] > size[0]):
            x = (float(img_size[0]) - w)/2
            crop_img = source_img.crop((x, y, x+w, y+h))
            resize = crop_img.resize((size[0], size[1]))
            resize.save(output_path)
        else:
            x = float(x)/2 - float(img_size[0])/2
            crop_img = source_img.crop((x, y, x+w, y+h))
            crop_img.save(output_path)
    else:
        w = img_size[0]
        h = float(w)/size[0]*size[1]
        x = 0
        if (img_size[1] > size[1]):
            y = float(img_size[1])/2 - float(h)/2
            crop_img = source_img.crop((x, y, x+w, y+h))
            resize = crop_img.resize((size[0], size[1]))
            resize.save(output_path)
        else:
            y = float(h)/2 - float(img_size[1])/2
            crop_img = source_img.crop((x, y, x+w, y+h))
            crop_img.save(output_path)
    print("完成处理 =>{}".format(output_path))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("缺少参数：路径")
        sys.exit(0)
    dir = sys.argv[1]
    if len(sys.argv) == 4:
        size = (int(sys.argv[2]), int(sys.argv[3]))
        riato = float(size[0])/size[1]
    find_all_pic(dir)
    multi_thread()
