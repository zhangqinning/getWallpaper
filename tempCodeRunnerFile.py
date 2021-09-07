# encoding=utf-8
# coding=utf-8
import requests
import json

if __name__ == '__main__':
    imagesUrl = "https://api.ihansen.org/img/detail?"
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'
    }
    params = {
        'page':0,
        'perPage':10,
        'index':'',
        'orderBy':'',
        'favorites':'',
        'tag':'night'
    }
    payload={}
    tags = {
        '风景':'landscape',
        '城市':'',
        '春天':'',
        '色彩':'',
        '黑白':'',
        '艺术':'',
        '天空':'',
        '森林':'',
        '散景':'',
        '夜空':'',
        '地平线':'',
        '灯光':'',
        '公益':'',
        '桥':'',
        '庙宇':'',
        '建筑':'',
        '云朵':'',
        '山峰':'',
        '大海':'',
        '冰雪':'',
        '雪景':'',
        '星空':'',
        '动物':''
    }
    response = requests.request("GET",imagesUrl,headers=headers,data=payload)
    images = json.loads(response.text)

    for imageInfo in images:
        print(json.dumps(imageInfo).__getitem__("info"))
        print("\n")


    