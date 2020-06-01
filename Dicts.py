class Layouts:
    def __init__(self):
        self.background_color = [
            ('亮色', '亮色', 250, 150),
            ('暗色', '暗色', 350, 150),
            ('其他', '其他', 450, 150)
        ]
        self.testing_mode = [
            ('是', '是', 250, 250),
            ('否', '否', 350, 250)
        ]
        self.interface = [
            ('信息公司', '1', 250, 400),
            ('本部', '2', 350, 400)
        ]
        self.frame1_number = [
            ('1', 'white', '8', 50, 100),
            ('2', 'white', '8', 50, 150),
            ('3', 'white', '8', 50, 200),
            ('4', 'white', '8', 50, 250),
            ('5', 'white', '8', 50, 300),
            ('6', 'white', '8', 50, 350),
            ('7', 'white', '8', 50, 400),
            ('景区名称', 'white', '10', 150, 100),
            ('背景图片', 'white', '10', 150, 150),
            ('技术支持', 'white', '10', 150, 200),
            ('测试模式', 'white', '10', 150, 250),
            ('后台地址', 'white', '10', 150, 300),
            ('闸机编号', 'white', '10', 150, 350),
            ('接口选择', 'white', '10', 150, 400),
            ('序号', 'SkyBlue', '8', 50, 50),
            ('项目名称', 'SkyBlue', '10', 150, 50),
            ('参数设置', 'SkyBlue', '44', 250, 50)
        ]
        self.frame2_number = [
            ('1', 'white', '8', 50, 100),
            ('2', 'white', '8', 50, 150),
            ('3', 'white', '8', 50, 200),
            ('4', 'white', '8', 50, 250),
            ('三辊闸机V1.0', 'white', '10', 150, 100),
            ('翼门闸机V1.0', 'white', '10', 150, 150),
            ('摆门闸机V1.0', 'white', '10', 150, 200),
            ('摆门闸机V2.0', 'white', '10', 150, 250),
            ('序号', 'SkyBlue', '8', 50, 50),
            ('闸机型式', 'SkyBlue', '20', 150, 50),
            ('闸机控制器串口号', 'SkyBlue', '30', 350, 50),
            ('选择', 'SkyBlue', '8', 580, 50)
        ]
        self.frame3_number = [
            ('1', 'white', '8', 50, 100),
            ('2', 'white', '8', 50, 150),
            ('3', 'white', '8', 50, 200),
            ('4', 'white', '8', 50, 250),
            ('5', 'white', '8', 50, 300),
            ('6', 'white', '8', 50, 350),
            ('单向入口', 'white', '8', 150, 100),
            ('单向出口', 'white', '8', 150, 150),
            ('单向出口', 'white', '8', 150, 200),
            ('双向进出', 'white', '8', 150, 250),
            ('双向进出', 'white', '8', 150, 300),
            ('单向进入', 'white', '8', 250, 100),
            ('出口计数', 'white', '8', 250, 150),
            ('出口不计数', 'white', '10', 250, 200),
            ('正向刷卡，出口计数', 'white', '17', 250, 250),
            ('正向刷卡，出口不计数', 'white', '19', 250, 300),
            ('序号', 'SkyBlue', '8', 50, 50),
            ('工作模式', 'SkyBlue', '10', 150, 50),
            ('内容', 'SkyBlue', '44', 250, 50),
            ('选择', 'SkyBlue', '8', 580, 50)
        ]
        self.frame4_number = [
            ('1', 'white', '8', 50, 150),
            ('2', 'white', '8', 50, 200),
            ('3', 'white', '8', 50, 250),
            ('1', 'white', '8', 50, 360),
            # ('2', 'white', '8', 50, 350),
            ('2', 'white', '8', 50, 410),
            # ('4', 'white', '8', 50, 450),
            ('主二维码', 'white', '10', 150, 150),
            ('二维码2', 'white', '10', 150, 200),
            ('二维码3', 'white', '10', 150, 250),
            ('新中新DJ1', 'white', '10', 150, 360),
            # ('新中新DJ2', 'white', '10', 150, 350),
            ('中控1', 'white', '7', 150, 410),
            # ('中控2', 'white', '7', 150, 450),
            ('身份证+RFID卡二合一', 'white', '18', 250, 360),
            # ('身份证', 'white', '6', 250, 350),
            ('身份证+RFID', 'white', '11', 250, 410),
            # ('身份证', 'white', '6', 250, 450),
            ('二维码门票阅读器配置', 'white', '20', 50, 70),
            ('序号', 'SkyBlue', '8', 50, 100),
            ('读卡器', 'SkyBlue', '10', 150, 100),
            ('读卡器串口号', 'SkyBlue', '44', 250, 100),
            ('身份证阅读器配置', 'white', '16', 50, 280),
            ('序号', 'SkyBlue', '8', 50, 310),
            ('阅读器型号', 'SkyBlue', '10', 150, 310),
            ('说明', 'SkyBlue', '44', 250, 310),
            ('选择', 'SkyBlue', '8', 580, 310)
        ]
        self.frame5_number = [
            ('1', 'white', '8', 50, 100),
            ('2', 'white', '8', 50, 150),
            ('3', 'white', '8', 50, 200),
            ('4', 'white', '8', 50, 250),
            ('5', 'white', '8', 50, 300),
            ('6', 'white', '8', 50, 350),
            ('7', 'white', '8', 50, 400),
            ('6.5寸', 'white', '10', 150, 100),
            ('6.5寸', 'white', '10', 150, 150),
            ('8.4寸', 'white', '10', 150, 200),
            ('8.4寸', 'white', '10', 150, 250),
            ('10.2寸', 'white', '10', 150, 300),
            ('10.2寸', 'white', '10', 150, 350),
            ('12.5寸', 'white', '10', 150, 400),
            ('800*600', 'white', '7', 300, 100),
            ('600*800', 'white', '7', 300, 150),
            ('1024*768', 'white', '8', 300, 200),
            ('768*1024', 'white', '8', 300, 250),
            ('1024*768', 'white', '8', 300, 300),
            ('768*1024', 'white', '8', 300, 350),
            ('900*1600', 'white', '8', 300, 400),
            ('横放', 'white', '4', 480, 100),
            ('竖放', 'white', '4', 480, 150),
            ('横放', 'white', '4', 480, 200),
            ('竖放', 'white', '4', 480, 250),
            ('横放', 'white', '4', 480, 300),
            ('竖放', 'white', '4', 480, 350),
            ('竖放', 'white', '4', 480, 400),
            ('序号', 'SkyBlue', '8', 50, 50),
            ('屏幕大小', 'SkyBlue', '10', 150, 50),
            ('分辨率', 'SkyBlue', '25', 250, 50),
            ('放置形式', 'SkyBlue', '18', 440, 50),
            ('选择', 'SkyBlue', '8', 580, 50)
        ]
        self.frame6_number = [
            ('1', 'white', '8', 50, 150),
            ('2', 'white', '8', 50, 200),
            ('3', 'white', '8', 50, 250),
            ('4', 'white', '8', 50, 300),
            ('5', 'white', '8', 50, 350),
            ('人脸IP', 'white', '10', 150, 150),
            ('阈值', 'white', '10', 150, 200),
            ('类型', 'white', '10', 150, 250),
            ('旋转', 'white', '10', 150, 300),
            ('index', 'white', '10', 150, 350),
            ('序号', 'SkyBlue', '8', 50, 100),
            ('项目名称', 'SkyBlue', '10', 150, 100),
            ('参数设置', 'SkyBlue', '44', 250, 100)
        ]
        self.frame7_number = [
            ('1', 'white', '8', 50, 100),
            ('2', 'white', '8', 50, 150),
            ('样式选择', 'white', '10', 150, 100),
            ('测温模块', 'white', '10', 150, 150),
            ('序号', 'SkyBlue', '8', 50, 50),
            ('式样', 'SkyBlue', '10', 150, 50),
            ('参数设置', 'SkyBlue', '44', 250, 50)
        ]
        self.gate_form = [
            ('', '三辊闸机', 600, 100),
            ('', '翼闸', 600, 150),
            ('', '摆闸', 600, 200),
            ('', '摆闸二', 600, 250)
        ]
        self.ticket_mode = [
            ('一票一客', '一票一客', 150, 350),
            ('一票多客', '一票多客', 300, 350),
        ]
        self.three = ("ttyS0", "ttyS1", "ttyS2", "ttyS3", "ttyS4", "ttyS5", "ttyS6", "ttyS7")

        self.wing = ("ttyS0", "ttyS1", "ttyS2", "ttyS3", "ttyS4", "ttyS5", "ttyS6", "ttyS7")

        self.swing = ("ttyS0", "ttyS1", "ttyS2", "ttyS3", "ttyS4", "ttyS5", "ttyS6", "ttyS7")
        self.swing_2 = ("ttyS0", "ttyS1", "ttyS2", "ttyS3", "ttyS4", "ttyS5", "ttyS6", "ttyS7")
        self.gate_mode = [
            ('', '单向入口', 600, 100),
            ('', '单出计数', 600, 150),
            ('', '单出不计', 600, 200),
            ('', '双向出计', 600, 250),
            ('', '双向不计', 600, 300)
        ]
        self.code_check = [
            ('二维码', 100, 15)
        ]
        self.idcard_check = [
            ('身份证', 200, 15)
        ]
        # self.code_com = [
        #     ('COM1', 'COM1', 250, 150),
        #     ('COM2', 'COM2', 330, 150),
        #     ('COM3', 'COM3', 410, 150),
        #     ('COM4', 'COM4', 490, 150)
        # ]
        self.code_com = ("ttyS0", "ttyS1", "ttyS2", "ttyS3", "ttyS4", "ttyS5", "ttyS6", "ttyS7")
        self.code_com_2 = ("None","ttyS0", "ttyS1", "ttyS2", "ttyS3", "ttyS4", "ttyS5", "ttyS6", "ttyS7")
        self.code_com_3 = ("None","ttyS0", "ttyS1", "ttyS2", "ttyS3", "ttyS4", "ttyS5", "ttyS6", "ttyS7")
        self.idcard_set = [
            ('', 'synjo+RFID', 600, 360),
            # ('', 'synjo', 600, 350),
            ('', 'zk1+RFID', 600, 410),
            # ('', 'zk2', 600, 450)
        ]
        # self.zkong_com = [
        #     ('COM1', 'COM1', 250, 400),
        #     ('COM2', 'COM2', 330, 400),
        #     ('COM3', 'COM3', 410, 400),
        #     ('COM4', 'COM4', 490, 400)
        # ]
        self.zkong_com = ("ttyS0", "ttyS1", "ttyS2", "ttyS3", "ttyS4", "ttyS5", "ttyS6", "ttyS7")
        self.screen = [
            ('', '6.5_800*600', 600, 100),
            ('', '6.5_600*800', 600, 150),
            ('', '8.4_1024*768', 600, 200),
            ('', '8.4_768*1024', 600, 250),
            ('', '10.2_1024*768', 600, 300),
            ('', '10.2_768*1024', 600, 350),
            ('', '12.5_900*1600', 600, 400)
        ]
        self.face_check = [
            ('人脸识别', 100, 15),
        ]
        self.zhkocom_list = ("ttyS0", "ttyS1", "ttyS2", "ttyS3", "ttyS4", "ttyS5", "ttyS6", "ttyS7")
        self.face_mode = [
            ('1:1', '1:1', 250, 250),
            ('1:N', '1:N', 350, 250)
        ]
        self.face_mode_1 = [
            ('1:1', 250, 250)
        ]
        self.face_mode_n = [
            ('1:N', 350, 250)
        ]
        self.rotate = ("clockwise0", "clockwise90", "clockwise180", "clockwise270", "anticlockwise0", "anticlockwise90", "anticlockwise180", "anticlockwise270")
        self.index = ("0", "1","2","3")
        self.ui_mode = ("样式一", "样式二")
        self.temperature = ("None", "lm")

    def bg_color(self):
        return self.background_color

    def tst_mode(self):
        return self.testing_mode

    def fm1_number(self):
        return self.frame1_number

    def fm2_number(self):
        return self.frame2_number

    def fm3_number(self):
        return self.frame3_number

    def fm4_number(self):
        return self.frame4_number

    def fm5_number(self):
        return self.frame5_number

    def fm6_number(self):
        return self.frame6_number

    def fm7_number(self):
        return self.frame7_number

    def gt_form(self):
        return self.gate_form

    def thr(self):
        return self.three

    def wng(self):
        return self.wing

    def swg(self):
        return self.swing

    def swg_2(self):
        return self.swing_2

    def gt_mode(self):
        return self.gate_mode

    def cd_check(self):
        return self.code_check

    def id_check(self):
        return self.idcard_check

    def cd_com(self):
        return self.code_com

    def cd_com_2(self):
        return self.code_com_2

    def cd_com_3(self):
        return self.code_com_3

    def id_set(self):
        return self.idcard_set

    def zk_com(self):
        return self.zkong_com

    def scr(self):
        return self.screen

    def fc_check(self):
        return self.face_check

    def zhkcom_list(self):
        return self.zhkocom_list

    def interfc(self):
        return self.interface

    def fc_mode(self):
        return self.face_mode

    def fc_mode_1(self):
        return self.face_mode_1

    def fc_mode_n(self):
        return self.face_mode_n

    def rotat(self):
        return self.rotate

    def tk_mode(self):
        return self.ticket_mode

    def idx(self):
        return self.index

    def uii_mode(self):
        return self.ui_mode

    def temper(self):
        return self.temperature