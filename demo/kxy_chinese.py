# -*- coding:utf-8 -*-
# @Time    : 2017/12/30 18:37
# @Author  : Harry
import random


class KxyChinese(object):
    """
    kxy0-kxy9，共计10组，0-1,2-3,4-5,6-7,8-9为5组，该方法的功能是从5组中的一组中随机获取3个字，组成一个字符串
    规则，每组(两个元组合)至少要选择一个汉字，即一个元组选择1个汉字，另外一个远足选择2个汉字
    """

    def __init__(self):

        # 定义十组KXY数据
        self.kxy0 = (u'阿', u'暗', u'昂', u'熬', u'比', u'变', u'标', u'宾', u'擦', u'尺',
                     u'冲', u'德', u'地', u'电', u'董', u'多', u'儿', u'发', u'佛', u'改',
                     u'干', u'根', u'古', u'河', u'黑', u'会', u'火', u'吉', u'叫', u'竟',
                     u'九', u'决', u'库', u'浪', u'良', u'律', u'门', u'某', u'木', u'你',
                     u'农', u'排', u'气', u'欠', u'全', u'绕', u'人', u'善', u'蛇', u'师',
                     u'刷', u'谁', u'顺', u'四', u'太', u'滕', u'图', u'卧', u'西', u'写',
                     u'信', u'醒', u'哑', u'也', u'一', u'硬', u'又', u'找', u'这', u'正',
                     u'志', u'专', u'自', u'组', u'作')
        self.kxy1 = (u'肮', u'拔', u'帮', u'必', u'赤', u'窗', u'词', u'代', u'德', u'敌',
                     u'东', u'堵', u'恩', u'发', u'奋', u'盖', u'敢', u'格', u'更', u'过',
                     u'贺', u'红', u'换', u'记', u'奖', u'叫', u'斤', u'京', u'举', u'口',
                     u'列', u'刘', u'罗', u'妹', u'棉', u'母', u'恼', u'娘', u'跑', u'起',
                     u'前', u'热', u'容', u'善', u'生', u'是', u'帅', u'水', u'说', u'四',
                     u'提', u'跳', u'推', u'吴', u'西', u'下', u'谢', u'信', u'眼', u'移',
                     u'硬', u'用', u'由', u'玉', u'元', u'运', u'诈', u'债', u'真', u'纸',
                     u'主', u'捉', u'资', u'走', u'组')
        self.kxy2 = (u'熬', u'八', u'必', u'伯', u'布', u'成', u'尺', u'错', u'但', u'德',
                     u'底', u'对', u'夺', u'二', u'房', u'奋', u'该', u'共', u'沟', u'管',
                     u'哈', u'贺', u'黑', u'昏', u'记', u'酱', u'交', u'近', u'旧', u'肯',
                     u'老', u'乐', u'脸', u'茂', u'灭', u'明', u'牛', u'怒', u'皮', u'齐',
                     u'欠', u'窃', u'然', u'入', u'傻', u'射', u'神', u'十', u'暑', u'说',
                     u'四', u'腾', u'天', u'筒', u'威', u'我', u'五', u'习', u'小', u'心',
                     u'性', u'牙', u'移', u'营', u'玉', u'远', u'月', u'在', u'摘', u'站',
                     u'丈', u'纸', u'抓', u'子', u'宗')
        self.kxy3 = (u'埃', u'变', u'宾', u'冰', u'茶', u'赤', u'次', u'代', u'德', u'地',
                     u'吊', u'叠', u'恩', u'纺', u'费', u'盖', u'葛', u'工', u'狗', u'贵',
                     u'痕', u'红', u'活', u'吉', u'甲', u'减', u'江', u'紧', u'旧', u'科',
                     u'炉', u'律', u'罗', u'马', u'米', u'木', u'鸟', u'农', u'碰', u'起',
                     u'庆', u'然', u'绕', u'邵', u'身', u'十', u'手', u'树', u'说', u'死',
                     u'他', u'腾', u'替', u'外', u'我', u'误', u'细', u'详', u'谢', u'宣',
                     u'烟', u'移', u'用', u'又', u'玉', u'允', u'脏', u'展', u'折', u'至',
                     u'竹', u'壮', u'追', u'白', u'钻')
        self.kxy4 = (u'奥', u'北', u'比', u'宾', u'布', u'柴', u'尺', u'次', u'当', u'吊',
                     u'动', u'对', u'夺', u'鹅', u'恩', u'耳', u'粉', u'父', u'改', u'个',
                     u'共', u'过', u'海', u'航', u'横', u'换', u'记', u'如', u'旧', u'举',
                     u'决', u'可', u'拉', u'兰', u'六', u'迷', u'命', u'抹', u'男', u'你',
                     u'欧', u'扑', u'气', u'浅', u'切', u'然', u'瑞', u'神', u'胜', u'使',
                     u'树', u'刷', u'说', u'孙', u'他', u'套', u'亭', u'习', u'闲', u'谢',
                     u'信', u'亚', u'眼', u'羊', u'腰', u'义', u'院', u'则', u'闸', u'照',
                     u'志', u'主', u'捉', u'自', u'宗')
        self.kxy5 = (u'安', u'宝', u'必', u'别', u'扯', u'池', u'此', u'打', u'代', u'地',
                     u'动', u'多', u'发', u'反', u'根', u'共', u'拐', u'贵', u'郭', u'和',
                     u'很', u'户', u'记', u'见', u'江', u'节', u'井', u'旧', u'肯', u'乐',
                     u'亮', u'龙', u'卖', u'米', u'木', u'内', u'能', u'飘', u'勤', u'穷',
                     u'热', u'软', u'沙', u'是', u'受', u'赎', u'双', u'说', u'四', u'唐',
                     u'桃', u'替', u'窝', u'习', u'现', u'修', u'许', u'亚', u'言', u'摇',
                     u'意', u'印', u'影', u'于', u'元', u'运', u'债', u'掌', u'争', u'志',
                     u'周', u'竹', u'子', u'租', u'最')
        self.kxy6 = (u'爱', u'暗', u'绑', u'北', u'笨', u'边', u'尺', u'穿', u'词', u'搭',
                     u'等', u'敌', u'丢', u'盾', u'鹅', u'二', u'乏', u'父', u'更', u'狗',
                     u'姑', u'国', u'汉', u'烘', u'胡', u'化', u'甲', u'见', u'脚', u'九',
                     u'决', u'苦', u'懒', u'离', u'律', u'门', u'密', u'抹', u'尼', u'懦',
                     u'泡', u'七', u'前', u'庆', u'饶', u'入', u'色', u'晒', u'上', u'绍',
                     u'射', u'十', u'说', u'贴', u'亭', u'痛', u'委', u'卧', u'习', u'乡',
                     u'信', u'选', u'摇', u'也', u'亿', u'因', u'英', u'在', u'诈', u'折',
                     u'枕', u'知', u'追', u'自', u'宗')
        self.kxy7 = (u'背', u'必', u'补', u'车', u'赤', u'次', u'代', u'德', u'地', u'董',
                     u'豆', u'恩', u'发', u'纺', u'搞', u'跟', u'更', u'工', u'过', u'哈',
                     u'红', u'黄', u'吉', u'见', u'奖', u'叫', u'借', u'旧', u'考', u'辽',
                     u'吕', u'乱', u'麻', u'门', u'米', u'宁', u'奴', u'批', u'恰', u'茄',
                     u'日', u'瑞', u'晒', u'善', u'蛇', u'十', u'收', u'树', u'死', u'汤',
                     u'退', u'拖', u'外', u'习', u'显', u'心', u'凶', u'眼', u'养', u'一',
                     u'印', u'英', u'由', u'鱼', u'元', u'运', u'在', u'展', u'者', u'正',
                     u'志', u'住', u'捉', u'足', u'左')
        self.kxy8 = (u'爱', u'安', u'奧', u'把', u'必', u'别', u'伯', u'柴', u'处', u'词',
                     u'敌', u'定', u'动', u'对', u'多', u'饿', u'二', u'粉', u'风', u'个',
                     u'给', u'共', u'关', u'号', u'喝', u'红', u'货', u'吉', u'尖', u'奖',
                     u'金', u'九', u'口', u'狼', u'鲁', u'落', u'满', u'秒', u'木', u'拿',
                     u'尼', u'片', u'气', u'求', u'缺', u'热', u'如', u'少', u'神', u'生',
                     u'是', u'书', u'睡', u'四', u'烫', u'条', u'亭', u'蛙', u'细', u'现',
                     u'些', u'许', u'哑', u'意', u'因', u'影', u'元', u'杂', u'在', u'站',
                     u'枕', u'知', u'准', u'捉', u'自')
        self.kxy9 = (u'闭', u'边', u'表', u'陈', u'池', u'此', u'带', u'德', u'底', u'董',
                     u'杜', u'饭', u'分', u'格', u'给', u'姑', u'关', u'过', u'哈', u'恨',
                     u'坏', u'记', u'酱', u'姐', u'井', u'九', u'捐', u'克', u'来', u'力',
                     u'律', u'满', u'盟', u'面', u'你', u'农', u'欧', u'普', u'墙', u'穷',
                     u'日', u'弱', u'晒', u'商', u'十', u'树', u'谁', u'说', u'送', u'腾',
                     u'透', u'土', u'王', u'窝', u'细', u'笑', u'写', u'心', u'牙', u'烟',
                     u'意', u'银', u'英', u'又', u'玉', u'运', u'杂', u'早', u'诈', u'张',
                     u'赵', u'折', u'止', u'追', u'自')

        self.list_kxy = [self.kxy0, self.kxy1, self.kxy2, self.kxy3, self.kxy4,
                         self.kxy5, self.kxy6, self.kxy7, self.kxy8, self.kxy9]
        self.list_font = ["", "", ""]

    @staticmethod
    def random_number():
        """
        随机生成0-74中的一个数
        :return: 返回一个随机数
        """
        return random.randint(0, 74)

    @staticmethod
    def sign_number():
        """
        随机生成一个标志位
        :return: 返回1或者0
        """
        return random.randint(0, 1)

    def three_font(self):
        """
        功能：生成三个汉字
        :return:
        """
        sign_num = self.sign_number()
        if sign_num == 1:
            for i in range(3):
                self.add_font_to_list(sign_number=sign_num, index_number=i)
        elif sign_num == 0:
            for i in range(3):
                self.add_font_to_list(sign_number=sign_num, index_number=i)
        # 打乱3个字的顺序
        random.shuffle(self.list_font)
        # 将列表中的数据转化为字符串
        return "".join(self.list_font)

    def add_font_to_list(self, sign_number, index_number):
        """
        向list_font中添加3个汉字
        :param sign_number: 标志位，用来选择元组
        :param index_number: list的索引号码
        :return: 无返回值
        """
        five_num = self.chose_five_num()
        random_num = self.random_number()
        self.list_font[index_number] = self.list_kxy[five_num + sign_number][random_num]

    @staticmethod
    def chose_five_num():
        """
        0-1,2-3,4-5,6-7,8-9为5组，该方法的功能是从5组中的随机选择一组返回
        :return: 0，2,4,6,8中的任意一个数
        """
        five_num = random.randint(0, 4)
        return five_num * 2
