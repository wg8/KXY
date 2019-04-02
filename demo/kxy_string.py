# -*- coding:utf-8 -*-
# @Time    : 2017/12/30 18:37
# @Author  : Harry

import random


class KxyString(object):
    """
    随机生成字母和数字的组合
    规则：其中要有个、十、百、千、万位数及10个字母
    """

    def __init__(self):
        self.ABC = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.string_list = []

    def append_to_list_letter(self):
        """
        给list中先加入10个字母
        :return: 无返回值
        """
        for i in range(10):
            # 随机产生0-25中的一个数字
            random_num = random.randint(0, 25)
            letter = self.ABC[random_num]
            self.string_list.append(letter)

    def append_to_list_num(self):
        """
        给string_list分别添加个、十、百、前、万，5组数字
        方法说明：循环5次，第一次的random取值范围为1-9，后面是10-99，100-999，1000-9999，10000-99999
        :return: 无返回值
        """
        for i in range(5):

            start_num = 10 ** i  # 输出1,10,100,1000,10000
            end_num = start_num * 10 - 1  # 输出9,99,999,9999,99999
            if i == 0:
                start_num = 10 ** i - 1  # 如果start_name = 1，就要赋值为0，start_num=0
            random_num = random.randint(start_num, end_num)
            self.string_list.append(str(random_num))

    def output_string_list(self):
        """
        输出这个由数字和字母组成的list
        :return: 返回一个打乱的字符串
        """
        self.append_to_list_letter()
        self.append_to_list_num()
        # 打乱list中的数据
        random.shuffle(self.string_list)
        # 将list中的数据全部转化为字符串
        return "".join(self.string_list)
