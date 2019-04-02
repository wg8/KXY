# -*- coding:utf-8 -*-
# @Time    : 2017/12/30 18:37
# @Author  : Harry
# 如果使用python3.5，请使用from tkinter import *
# 如果使用python2.7，请使用如下引用from Tkinter import *
from Tkinter import *
from demo.kxy_controller import KxyController


class Gui(object):
    def __init__(self):
        """
        定义全局变量
        """
        # 数字和字母checkButton(或checkBox)的初始状态
        self.check_button_string = 0
        # 生成三个字的按钮的checkButton(或者checkBox)的初始状态
        self.check_button_chinese = 0

        root = Tk()
        # 设置窗口的title
        root.wm_title(u'KXY语音评测文字随机生成工具v2.0.0')
        # 设置窗口的宽高
        root.geometry("400x480")
        # 设置Text窗口的宽高
        self.text_frame = Text(root, width=40, height=30)
        # 显示输出文本的text窗口，设置外边距为20px
        self.text_frame.pack(pady=20)

        # 用来表示checkButton或者checkBox的按钮是否选中
        self.check_box1_status = IntVar()
        self.check_box2_status = IntVar()

        # 生成中文的按钮
        Button(root, text=u"生成中文", command=self.print_three_chinese).pack(side=RIGHT, padx=10)
        # 输出txt的checkButton
        Checkbutton(root, text=u'输出txt', variable=self.check_box1_status).pack(side=RIGHT, padx=10)

        # 生成数字和字母的按钮
        Button(root, text=u"生成数英", command=self.print_string).pack(side=RIGHT, padx=10)
        # 输出txt的checkButton
        Checkbutton(root, text=u'输出txt', variable=self.check_box2_status).pack(side=RIGHT, padx=10)

        root.mainloop()

    def output_twenty_five_lines(self, chose_method, check_button_status):

        """
        循环25次输入25组字符串,并判断是否要写入txt文件的方法
        :param chose_method: 选择是输出三个中文，或者是输出string(数字和字母的组合)
            chose_method的值决定输出汉字或者输出数字和字母组合，1代表输出汉字，2代表输出组合
        :param check_button_status: 判断点击按钮前的check_button的状态是否选中
            如果选中即值为1，则输出到txt，如果未选中即值为0，不输出到txt文件
        :return: 不返回任何数值
        """

        for i in range(25):
            text = KxyController().show_content(show_value=chose_method)
            output_text = str(i + 1) + "." + text + "\n"
            if check_button_status == 1:
                KxyController().output_to_txt_file(print_content=output_text, file_name=chose_method)

            # 显示到GUI界面上
            if i < 9:
                self.text_frame.insert(END, "0" + output_text)
            else:
                self.text_frame.insert(END, output_text)

    def print_three_chinese(self):
        """
        功能:调用output_twenty_five_lines方法，向窗口输出25行汉字
        代码逻辑：每次调用显示25行的方法前，先清除上一次显示到窗口的文字
        button_print_three_chinese_sign = 1的含义：输出三个中文
        :return:不返回任何值
        """
        button_print_three_chinese_sign = 1
        self.text_frame.delete(0.0, END)
        self.output_twenty_five_lines(chose_method=button_print_three_chinese_sign,
                                      check_button_status=self.check_box1_status.get())

    def print_string(self):
        """
        功能:调用output_twenty_five_lines方法，向窗口输出25数字和字母的组合
        代码逻辑：每次调用显示25行的方法前，先清除上一次显示到窗口的字符串
        button_print_three_chinese_sign = 2的含义：输出数字和字母的组合
        :return:
        """
        button_print_string_sign_sign = 2
        self.text_frame.delete(0.0, END)
        self.output_twenty_five_lines(chose_method=button_print_string_sign_sign,
                                      check_button_status=self.check_box2_status.get())


Gui()
