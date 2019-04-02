# -*- coding:utf-8 -*-
# @Time    : 2017/12/30 18:37
# @Author  : Harry
import os
import sys

# python2：
reload(sys)
sys.setdefaultencoding('utf-8')

# python3：
# imp.reload(sys)
# sys.setdefaultencoding('utf-8')


class WriteTxt(object):
    """
    将输出内容写到txt文件中
    """

    def __init__(self):
        self.string_name = "kxy_string.txt"
        self.chinese_name = 'kxy_chinese.txt'
        self.folder_path = self.get_folder_path()

    @staticmethod
    def get_folder_path():
        """
        获取txt的存储路径
        :return:返回路径
        """
        return os.path.abspath('.')

    def writing(self, txt_content, txt_name):
        """
        将txt_content中的内容写入到txt文件中
        :param txt_content:将要写入的内容
        :param txt_name:txt文件名字的判断来源
        :return:
        """
        txt_path = ""
        if txt_name == 1:
            txt_path = self.folder_path + "\\" + self.chinese_name
        elif txt_name == 2:
            txt_path = self.folder_path + "\\" + self.string_name
        else:
            print("sorry, it's error!")
        txt_file = open(txt_path, 'a')  # a的意思是继续追加，w的意思是覆盖原本内容
        txt_file.write(txt_content)
        txt_file.close()
