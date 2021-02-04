#-*- coding:utf-8 -*-
import os
import chardet   #用于查看编码

def code_change(file_path):  
  with open(file_path, "rb") as temp:
    tem = temp.read()

  str_type = chardet.detect(tem)
  print(str_type,os.path.split(file_path)[-1])
  if str_type['encoding'] == None or str_type['encoding'] == 'utf-8':
    return 
  with open(file_path, "w",encoding='utf-8') as temp:
    temp.write(tem.decode(encoding=str_type['encoding']))

def path_code_change(dir_path):
  for root, dirs, files in os.walk(dir_path, topdown=False):
    for name in files:
      code_change(os.path.join(root, name))
    # for name in dirs:
    #     print(os.path.join(root, name))

  


if __name__ == "__main__":
  file_path = input('请输入文件路径：')
  if os.path.isfile(file_path):
    code_change(file_path)
  else:
    path_code_change(file_path)

    
  