# encoding=utf-8
# coding=utf-8
import requests
import json
import os
import sys
from os import listdir
from os.path import isfile, join
from PIL import Image
reload(sys)
sys.setdefaultencoding("utf-8")

if __name__ == '__main__':
    catalogues = {
        # '风景',
        # '城市',
        # '春天',
        # '色彩',
        # '黑白',
        # '艺术',
        # '天空',
        # '森林',
        # '散景',
        # '夜空',
        # '地平线',
        # '灯光',
        # '公路',
        # '桥',
        # '庙宇',
        # '建筑',
        # '云朵',
        # '山峰',
        # '大海',
        # '冰雪',
        # '雪景',
        # '星空',
        '动物'
    }

    size = (1242,2688)
    riato = float(size[0])/size[1]

    for cate in catalogues:
        folder = os.getcwd()+'/wallpaper/'+cate+'/'
        outfolder = os.getcwd()+'/wallpaper_crop/'+cate+'/'
        if not os.path.exists(folder):
            continue
        if not os.path.exists(outfolder):
            os.makedirs(outfolder)
        pngs = [ f for f in listdir(folder) if isfile(join(folder,f)) ]
        for png in pngs:
            pndPath =os.getcwd()+'/wallpaper/'+cate+'/'+png
            outPath =os.getcwd()+'/wallpaper_crop/'+cate+'/'+png
            print(pndPath)
            if pndPath.endswith('.DS_Store'):
                continue
            im = Image.open(pndPath)
            img_size = im.size
            x = 0
            y =0
            w = size[0]
            h = size[1]
            img_riato = float(img_size[0])/img_size[1]
            print("图片宽度和高度分别是{}".format(img_size))
            if img_riato > riato:
                h = img_size[1]
                w = float(h)/size[1]*size[0]
                y = 0
                if (img_size[0]>size[0]):
                    x = (float(img_size[0])- w)/2 
                    print('x:' +str(x)+' y:'+str(y)+' w:'+str(w)+' h:'+str(h) +' img_r:'+str(img_riato)+' r:'+str(riato))
                    cropImage = im.crop((x, y, x+w, y+h))
                    resize = cropImage.resize((size[0],size[1]))
                    cropImage.save(outPath)
                else:
                    x = float(x)/2 - float(img_size[0])/2
                    print('x:' +str(x)+' y:'+str(y)+' w:'+str(w)+' h:'+str(h) +' img_r:'+str(img_riato)+' r:'+str(riato))
                    cropImage = im.crop((x, y, x+w, y+h))
                    cropImage.save(outPath)
            else :
                w = img_size[0]
                h = float(w)/size[0]*size[1]
                x = 0
                if (img_size[1]>size[1]):
                    y = float(img_size[1])/2 - float(h)/2
                    print('x:' +str(x)+' y:'+str(y)+' w:'+str(w)+' h:'+str(h) +' img_r:'+str(img_riato)+' r:'+str(riato))
                    cropImage = im.crop((x, y, x+w, y+h))
                    resize = cropImage.resize((size[0],size[1]))
                    resize.save(outPath)
                else :
                    y = float(h)/2 - float(img_size[1])/2
                    print('x:' +str(x)+' y:'+str(y)+' w:'+str(w)+' h:'+str(h) +' img_r:'+str(img_riato)+' r:'+str(riato))
                    cropImage = im.crop((x, y, x+w, y+h))
                    cropImage.save(outPath)

            # if img_size[0]>size[0] and img_size[1]>size[1]:
            #     if img_size[0]>img_size[1]:
            #         x = img_size[0]/2-size[0]/2  
            #         y = 0
            #         h = img_size[1]
            #         w = h/size[1]*size[0]
            #     else :
            #         x = 0
            #         y = img_size[1]/2-size[1]/2  
            #         w = img_size[0]
            #         h = w/size[0]*size[1]
            #     print(" >> x "+str(x)+" y "+ str(y) +" w "+str(w)+" h "+str(h) )
            #     cropImage = im.crop((x, y, x+w, y+h))
            #     resize = cropImage.resize((size[0],size[1]))
            #     cropImage.save(pndPath)
            # else:
            #     if (img_size[0]/img_size[1]) >1:
            #         x = img_size[0]/2-size[0]/2  
            #         y = 0
            #         h = img_size[1]
            #         w = h/size[1]*size[0]
            #     else :
            #         x = 0
            #         y = img_size[1]/2-size[1]/2  
            #         w = img_size[0]
            #         h = w/size[0]*size[1]
            #     print("<< x "+str(x)+" y "+ str(y) +" w "+str(w)+" h "+str(h) )
            #     cropImage = im.crop((x, y, x+w, y+h))  
            #     cropImage.save(pndPath)


           
            # region = im.crop((x, y, x+w, y+h))
            # region.save("./crop_test1.jpeg")




    