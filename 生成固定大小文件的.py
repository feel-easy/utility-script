#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import random

def genSizeFile(fileName, fileSize):
    #file path
    filePath=fileName

    # 生成固定大小的文件
    # date size
    ds=0
    with open(filePath, "w", encoding="utf8") as f:
        while ds<fileSize:
            f.write(str(round(random.uniform(-1000, 1000),2)))
            f.write("\n")
            ds=os.path.getsize(filePath)
    # print(os.path.getsize(filePath))


if __name__ == '__main__':
    name = input('请输入文件名：')
    size = int(input('请输入大小：'))
    genSizeFile(name, size * 1023 * 1024)
