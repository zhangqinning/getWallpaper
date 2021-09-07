# encoding=utf-8
# coding=utf-8
import requests
import json
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

if __name__ == '__main__':
    imagesUrl = "https://api.ihansen.org/img/detail?"
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'
    }
    page = 0
    perPage = 20
    params = {
        'page':0,
        'perPage':perPage,
        'index':'',
        'orderBy':'',
        'favorites':'',
        'tag':'night'
    }
    payload={}
    catalogues = {
        '风景':'landscape',
        '城市':'city',
        '春天':'spring',
        '色彩':'color',
        '黑白':'black-and-white',
        '艺术':'art',
        '天空':'sky',
        '森林':'forest',
        '散景':'bokeh',
        '夜空':'night',
        '地平线':'horizon',
        '灯光':'light',
        '公路':'road',
        '桥':'bridge',
        '庙宇':'temple',
        '建筑':'architecture',
        '云朵':'cloud',
        '山峰':'moutain',
        '大海':'ocean',
        '冰雪':'ice',
        '雪景':'snow',
        '星空':'star',
        '动物':'animal'
    }

    saveImageUrls = {}
    for catalogueKey in catalogues:
        tag= catalogues[catalogueKey]
        print(tag)
        params['tag'] = tag
        cataloguelist = list()
        for index in range(perPage):
            params['page'] = index
            response = requests.request("GET",imagesUrl,headers=headers,data=payload,params=params)
            images = json.loads(response.text)
            for imageInfo in images:
                info = json.dumps(imageInfo)
                infoJson = json.loads(info)
                try:
                    url = infoJson["info"]["urls"]["raw"]
                    print(url)
                except KeyError:
                    continue
                cataloguelist.append(url)
        saveImageUrls[catalogueKey]= cataloguelist
        
    # for catalogueKey in saveImageUrls:
    #     for url in saveImageUrls[catalogueKey]:
    #         print(catalogueKey + ' ' +url)

    for catalogueKey in saveImageUrls:
        folder = os.getcwd()+'/wallpaper/'+catalogueKey+'/'
        print(folder)
        if not os.path.exists(folder):
            os.makedirs(folder)
        index = 1

        for url in saveImageUrls[catalogueKey]:
            print(catalogueKey +' '+url)   
            response = requests.request("GET",url).content
            final = folder+str(index)+'.png'
            with open(final,'wb') as fp:
                fp.write(response)
            index = index + 1

    