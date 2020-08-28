# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2020/08/28 23:35:40
@Author  :   Wicos 
@Version :   1.0
@Contact :   wicos@wicos.cn
@site    :   wicos.me
'''

# here put the import lib
import os
from PIL import Image
import json

def readJson(filePath):
    with open(filePath,'rb') as fp:
        a = json.load(fp)
    return a

def writeJson(filepath,msg):
    with open(filepath,'w+',encoding='utf-8') as fp:
        json.dump(msg, fp, indent=4)

class ZIPPIC():
    def __init__(self,floder):
        self.floder_path = floder
        self.success_task = []
        self.fail_task = []
        self.floder = self.get_dir()
        self.set_log() 
        self.log = readJson("log.json")
    
    def set_log(self):
        with open("log.json",'w+') as fp:
            json.dump({"success":[],"failed":[]}, fp, indent=4)
        

    def get_dir(self):
        if os.name == 'nt':
            dirs = os.getcwd().replace("\\","/") + "/" + self.floder_path
        if os.name == "posix":
            dirs = os.getcwd() + "/" + self.floder_path
        print("操作目录:",dirs)
        return dirs

    def get_all_pic(self):
        all_pic = []
        for i,j,k in os.walk(self.floder):
            if len(k) != 0:
                i = i.replace("\\","/")
                for m in k:
                    ddir = i + "/" + m
                    panduan = os.path.splitext(ddir)[1]
                    if panduan in [".jpg",".jpeg",".png",".PNG",".JPG"]:
                        all_pic.append(ddir)
        return all_pic

    def zip_pic(self,old_filepath,new_filepath):
        try:
            sImg = Image.open(old_filepath)
            w, h = sImg.size
            dImg = sImg.resize((w, h), Image.ANTIALIAS)
            dImg.save(new_filepath)
            #print("success{}".format(old_filepath))
            self.success_task.append(old_filepath)
        except:
            self.fail_task.append(old_filepath)
    
    def zip_all_pic(self):
        pic_list = self.get_all_pic()
        for i in pic_list:
            self.zip_pic(i,i)
        self.log["success"] = self.success_task
        self.log['failed'] = self.fail_task
        writeJson("log.json",self.log)
        print("日志文件储存在当前目录的log.json中")

a = ZIPPIC("wp-content/uploads")
a.zip_all_pic()