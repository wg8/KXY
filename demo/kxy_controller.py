# -*- coding:utf-8 -*-
# @Time    : 2017/12/30 18:37
# @Author  : Harry

from demo.kxy_chinese import KxyChinese
from demo.write_txt import WriteTxt
from demo.kxy_string import KxyString


class KxyController(object):

    @staticmethod
    def show_content(show_value):
        """
        功能：从kxy_chinese或者kxy_string中获取将要输出的字符串
            show_value 的值决定输出中文还是输出字符串
        :param show_value:=1,获取中文；=2，获取数字和字母的组合
        :return: 返回一个字符串
        """
        if show_value == 1:
            return KxyChinese().three_font()
        elif show_value == 2:
            return KxyString().output_string_list()
        else:
            return "sorry ,it's error!"

    @staticmethod
    def output_to_txt_file(print_content, file_name):
        """
        输入到txt文件中
        :param print_content: 将要输出的内容
        :param file_name: 判断是输出中文还是输出数字和字母的组合
        :return: 不返回任何值
        """
        WriteTxt().writing(txt_content=print_content, txt_name=file_name)
