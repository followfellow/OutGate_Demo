import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import json
from Params import Params, ReadParameters
import os
from Dicts import Layouts
import threading

global button_image
global img
global label_image
global label_img


def code_check_command():
    change_to_frame4()


def idcard_check_command():
    change_to_frame4()


def face_check_command():
    change_to_frame6()


def change_to_frame1():
    fm1.frame_pack()
    # fm1.image(0, 0, 'images/1.1.jpg')
    fm1.radiobutton(background_color, read_parameters.background_color_var)
    fm1.radiobutton(testing_mode, read_parameters.testing_mode_var)
    fm1.radiobutton(interface, read_parameters.Interface_var)
    fm1.label(frame1_number)
    fm1.entry(250, 100, 40, read_parameters.name_var)
    fm1.entry(250, 200, 40, read_parameters.support_var)
    fm1.entry(250, 300, 40, read_parameters.URL_var)
    fm1.entry(250, 350, 40, read_parameters.GateNum_var)


def change_to_frame2():
    fm2.frame_pack()
    # fm2.image(0, 0, 'images/3.1.jpg')
    fm2.label(frame2_number)
    fm2.radiobutton(gate_form, read_parameters.gate_form_var)
    # fm2.radiobutton(three, read_parameters.three_var)
    # fm2.radiobutton(wing, read_parameters.wing_var)
    # fm2.radiobutton(swing, read_parameters.swing_var)
    fm2.combobox(350, 100, read_parameters.three_var, three)
    fm2.combobox(350, 150, read_parameters.wing_var, wing)
    fm2.combobox(350, 200, read_parameters.swing_var, swing)
    fm2.combobox(350, 250, read_parameters.swing_2_var, swing_2)


def change_to_frame3():
    fm3.frame_pack()
    fm3.label(frame3_number)
    fm3.radiobutton(gate_mode, read_parameters.gate_mode_var)
    fm3.radiobutton(ticket_mode, read_parameters.ticket_mode_var)


def change_to_frame4():
    fm4.frame_pack()
    fm4.label(frame4_number)
    fm4.checkbutton(idcard_check, read_parameters.idcard_check_var, command=idcard_check_command)
    fm4.checkbutton(code_check, read_parameters.code_check_var, command=code_check_command)

    temp1 = read_parameters.code_check_var.get()
    if temp1 == 1:
        # fm4.radiobutton(code_com, read_parameters.code_com_var)
        fm4.combobox(250, 150, read_parameters.code_com_var, code_com)
        fm4.combobox(250, 200, read_parameters.code_com_2_var, code_com_2)
        fm4.combobox(250, 250, read_parameters.code_com_3_var, code_com_3)
    temp2 = read_parameters.idcard_check_var.get()
    if temp2 == 1:
        fm4.radiobutton(idcard_set, read_parameters.idcard_set_var)
        # fm4.radiobutton(zkong_com, read_parameters.zkong_com_var)
        fm4.combobox(350, 410, read_parameters.zkong_com_var, zkong_com)


def change_to_frame5():
    fm5.frame_pack()
    fm5.label(frame5_number)
    fm5.radiobutton(screen, read_parameters.screen_var)


def change_to_frame6():
    fm6.frame_pack()
    fm6.label(frame6_number)
    fm6.checkbutton(face_check, read_parameters.face_check_var, command=face_check_command)
    temp1 = read_parameters.face_check_var.get()
    if temp1 == 1:
        fm6.entry(250, 150, 40, read_parameters.face_ip_var)
        fm6.entry(250, 200, 40, read_parameters.threshold_var)
        fm6.checkbutton(face_mode_1, read_parameters.face_mode_1_var, command=None)
        fm6.checkbutton(face_mode_n, read_parameters.face_mode_n_var, command=None)
        fm6.combobox(250, 300, read_parameters.rotate_var, rotate)
        fm6.combobox(250, 350, read_parameters.index_var, index)
        # fm6.radiobutton(face_mode,read_parameters.face_mode_var)
    # fm6.combobox(250,400,read_parameters.number_var,zhongkonglist)


def change_to_frame7():
    fm7.frame_pack()
    fm7.label(frame7_number)
    fm7.combobox(250, 100, read_parameters.ui_mode_var, ui_mode)
    fm7.combobox(250, 150, read_parameters.temperature_var, temperature)

class Frame:
    def __init__(self, master, canvas, tags='tags'):

        self.canvas = canvas
        self.master = master
        self.tags = tags

    def frame_pack(self):
        global button_image
        global img

        self.tag_list = ['frame1', 'frame2', 'frame3', 'frame4', 'frame5', 'frame6', 'frame7']
        self.tag_list.remove(self.tags)
        for i in range(0, 5):
            self.canvas.delete(self.tag_list[i])
        self.frame = tk.Frame(self.master, bg='white')

        self.canvas.create_window(90, 60, width=700, height=530, anchor='nw', window=self.frame, tags=self.tags)
        button_image = Image.open('images/save.png')
        img = ImageTk.PhotoImage(image=button_image)
        btn = tk.Button(self.frame, text='保存修改', command=self.save, bg='DodgerBlue', fg='white', image=img,
                        compound='left', padx=15)
        btn.place(x=557, y=5)

    def image(self, x, y, image):
        global label_image
        global label_img
        canv = tk.Canvas(self.frame, height=529, width=434)
        label_image = Image.open(image)
        label_img = ImageTk.PhotoImage(image=label_image)
        canv.create_image(x, y, anchor='nw', image=label_img)
        canv.pack(side='left')

    def checkbutton(self, mode, var, command):
        for text, x, y in mode:
            ck = tk.Checkbutton(self.frame, text=text, variable=var, bg='white', command=command)
            ck.place(x=x, y=y)

    def entry(self, x, y, width, nam):
        self.name = tk.Entry(self.frame, width=width, textvariable=nam)
        self.name.place(x=x, y=y)

    def label(self, label):
        # tk.Label(self.frame, text=self.tags).place(x=label_x, y=label_y)
        for text, color, width, x, y in label:
            tk.Label(self.frame, text=text, bg=color, width=width).place(x=x, y=y)

    def save(self):
        par.dict['BasePar']['name'] = read_parameters.name_var.get()
        par.dict['BasePar']['image'] = read_parameters.background_color_var.get()
        par.dict['BasePar']['support'] = read_parameters.support_var.get()
        par.dict['BasePar']['testing'] = read_parameters.testing_mode_var.get()
        par.dict['BasePar']['URL'] = read_parameters.URL_var.get()
        par.dict['BasePar']['GateNum'] = read_parameters.GateNum_var.get()
        par.dict['BasePar']['Interface'] = read_parameters.Interface_var.get()
        par.dict['GateForm']['gate_form'] = read_parameters.gate_form_var.get()
        par.dict['GateForm']['three'] = read_parameters.three_var.get()
        par.dict['GateForm']['wing'] = read_parameters.wing_var.get()
        par.dict['GateForm']['swing'] = read_parameters.swing_var.get()
        par.dict['GateForm']['swing_2'] = read_parameters.swing_2_var.get()
        par.dict['GateMode']['gate_mode'] = read_parameters.gate_mode_var.get()
        par.dict['GateMode']['ticket_mode'] = read_parameters.ticket_mode_var.get()
        par.dict['Reader']['code_check'] = read_parameters.code_check_var.get()
        par.dict['Reader']['code_com'] = read_parameters.code_com_var.get()
        par.dict['Reader']['code_com_2'] = read_parameters.code_com_2_var.get()
        par.dict['Reader']['code_com_3'] = read_parameters.code_com_3_var.get()
        par.dict['Reader']['idcard_check'] = read_parameters.idcard_check_var.get()
        par.dict['Reader']['idcard_set'] = read_parameters.idcard_set_var.get()
        par.dict['Reader']['zkong_com'] = read_parameters.zkong_com_var.get()
        par.dict['Screen']['screen'] = read_parameters.screen_var.get()
        par.dict['Face']['face_check'] = read_parameters.face_check_var.get()
        par.dict['Face']['face_ip'] = read_parameters.face_ip_var.get()
        par.dict['Face']['threshold'] = read_parameters.threshold_var.get()
        # par.dict['Face']['num'] = read_parameters.number_var.get()
        par.dict['Face']['face_mode_1'] = read_parameters.face_mode_1_var.get()
        par.dict['Face']['face_mode_n'] = read_parameters.face_mode_n_var.get()
        par.dict['Face']['rotate'] = read_parameters.rotate_var.get()
        par.dict['Face']['index'] = read_parameters.index_var.get()
        par.dict['UiMode']['ui_mode'] = read_parameters.ui_mode_var.get()
        par.dict['UiMode']['temperature'] = read_parameters.temperature_var.get()
        par.save('params.json')

    def radiobutton(self, mode, var, cmd=None):
        for text, mode, x, y in mode:
            rd = tk.Radiobutton(self.frame, text=text, variable=var,
                                value=mode, bg='white', command=cmd)
            rd.place(x=x, y=y)

    def combobox(self, x, y, number, value):
        cb = ttk.Combobox(self.frame, width=15, textvariable=number)
        cb['values'] = value
        # print(number.get())
        # print(value.index(number.get()))
        cb.current(value.index(number.get()))
        cb.place(x=x, y=y)


def thread_it(func, *args):
    '''将函数打包进线程'''
    # 创建
    t = threading.Thread(target=func, args=args)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()
    # 阻塞--卡死界面！
    # t.join()


def click_button1():
    change_to_frame1()
    button1.config(fg='yellow')
    button2.config(fg='white')
    button3.config(fg='white')
    button4.config(fg='white')
    button5.config(fg='white')
    button6.config(fg='white')
    button7.config(fg='white')


def click_button2():
    change_to_frame2()
    button2.config(fg='yellow')
    button1.config(fg='white')
    button3.config(fg='white')
    button4.config(fg='white')
    button5.config(fg='white')
    button6.config(fg='white')
    button7.config(fg='white')


def click_button3():
    change_to_frame3()
    button3.config(fg='yellow')
    button1.config(fg='white')
    button2.config(fg='white')
    button4.config(fg='white')
    button5.config(fg='white')
    button6.config(fg='white')
    button7.config(fg='white')


def click_button4():
    change_to_frame4()
    button4.config(fg='yellow')
    button1.config(fg='white')
    button2.config(fg='white')
    button3.config(fg='white')
    button5.config(fg='white')
    button6.config(fg='white')
    button7.config(fg='white')


def click_button5():
    change_to_frame5()
    button5.config(fg='yellow')
    button1.config(fg='white')
    button2.config(fg='white')
    button3.config(fg='white')
    button4.config(fg='white')
    button6.config(fg='white')
    button7.config(fg='white')


def click_button6():
    change_to_frame6()
    button6.config(fg='yellow')
    button1.config(fg='white')
    button2.config(fg='white')
    button3.config(fg='white')
    button4.config(fg='white')
    button5.config(fg='white')
    button7.config(fg='white')


def click_button7():
    change_to_frame7()
    button7.config(fg='yellow')
    button1.config(fg='white')
    button2.config(fg='white')
    button3.config(fg='white')
    button4.config(fg='white')
    button5.config(fg='white')
    button6.config(fg='white')


if __name__ == '__main__':
    window = tk.Tk()
    window.title('GateCheck')
    window.geometry('800x600')
    window.resizable(False, False)

    layout = Layouts()
    # <editor-fold desc="read_layouts">
    background_color = layout.bg_color()
    testing_mode = layout.tst_mode()
    frame1_number = layout.fm1_number()
    frame2_number = layout.fm2_number()
    frame3_number = layout.fm3_number()
    frame4_number = layout.fm4_number()
    frame5_number = layout.fm5_number()
    frame6_number = layout.fm6_number()
    frame7_number = layout.fm7_number()

    gate_form = layout.gt_form()
    three = layout.thr()
    wing = layout.wng()
    swing = layout.swg()
    swing_2 = layout.swg_2()
    gate_mode = layout.gt_mode()
    code_check = layout.cd_check()
    idcard_check = layout.id_check()
    code_com = layout.cd_com()
    code_com_2 = layout.cd_com_2()
    code_com_3 = layout.cd_com_3()
    idcard_set = layout.id_set()
    zkong_com = layout.zk_com()
    screen = layout.scr()
    face_check = layout.fc_check()
    # zhongkonglist = layout.zhkcom_list()
    interface = layout.interfc()
    face_mode_1 = layout.fc_mode_1()
    face_mode_n = layout.fc_mode_n()
    rotate = layout.rotat()
    index=layout.idx()
    ticket_mode = layout.tk_mode()
    ui_mode = layout.uii_mode()
    temperature = layout.temper()
    # </editor-fold>
    parameters = {
        "BasePar": {
            "name": "",
            "image": "亮色",
            "support": "上海大漠电子科技股份有限公司",
            "testing": "否",
            "URL": "",
            "GateNum": "",
            "Interface": "1"
        },
        "GateForm": {
            "gate_form": "三辊闸机",
            "three": "ttyS1",
            "wing": "ttyS1",
            "swing": "ttyS1",
            "swing_2": "ttyS1",
        },
        "GateMode": {
            "gate_mode": "单向入口",
            "ticket_mode": "一票多客",
        },
        "Reader": {
            "code_check": 1,
            "idcard_check": 1,
            "code_com": "ttyS0",
            "code_com_2": "None",
            "code_com_3": "None",
            "idcard_set": "synjo+RFID",
            "zkong_com": "ttyS2",
        },
        "Screen": {
            "screen": "6.5_800*600",
        },
        "Face": {
            "face_check": 1,
            "face_ip": "192.168.0.0",
            "threshold": "50",
            "face_mode_1": 1,
            "face_mode_n": 1,
            "rotate": "clockwise0",
            "index": "0",
        },
        "UiMode": {
            "ui_mode": "样式一",
            "temperature": "None",
        },
    }
    json_str = json.dumps(parameters, indent=4)
    # json_str = json.dumps(parameters, ensure_ascii=False,indent=4)
    if os.path.isfile('params.json'):
        try:
            with open('params.json', 'r') as f:
                a = json.load(f)
            par = Params('params.json')
            read_parameters = ReadParameters()
            read_parameters.read_params(par)
        except:
            with open('params.json', 'w') as f:  # 创建一个params.json文件
                f.write(json_str)  # 将json_str写到文件中
            par = Params('params.json')
            read_parameters = ReadParameters()
            read_parameters.read_params(par)
    else:
        with open('params.json', 'w') as f:  # 创建一个params.json文件
            f.write(json_str)  # 将json_str写到文件中
        par = Params('params.json')
        read_parameters = ReadParameters()
        read_parameters.read_params(par)

    # 画布放置图片
    canvas = tk.Canvas(window, height=800, width=800)
    pil_image = Image.open('images/6.jpg')
    image_file = ImageTk.PhotoImage(image=pil_image)
    image = canvas.create_image(0, 0, anchor='nw', image=image_file)
    canvas.pack()
    # <editor-fold desc="button">
    region = (1, 75, 90, 115)
    region_lb = (100, 20, 250, 42)

    im = Image.open('images/6.jpg')
    cropped = im.crop(region)
    tk_im = ImageTk.PhotoImage(cropped)
    cropped_lb = im.crop(region_lb)
    tk_im_lb = ImageTk.PhotoImage(cropped_lb)
    lb = tk.Label(window, image=tk_im_lb, text='闸机管理系统', compound='center', borderwidth=0, padx=0, pady=0,
                  fg='white', font=('黑体', 13)).place(x=100, y=20)
    button1 = tk.Button(image=tk_im, command=lambda: thread_it(click_button1), text='基本参数', compound='center',
                        borderwidth=0, padx=0,
                        pady=0,
                        fg='yellow')
    button1.place(x=1, y=80)
    button2 = tk.Button(image=tk_im, command=lambda: thread_it(click_button2), text='闸机类型', compound='center',
                        borderwidth=0, padx=0,
                        pady=0,
                        fg='white')
    button2.place(x=1, y=120)
    button3 = tk.Button(image=tk_im, command=lambda: thread_it(click_button3), text='工作模式', compound='center',
                        borderwidth=0, padx=0,
                        pady=0,
                        fg='white')
    button3.place(x=1, y=160)
    button4 = tk.Button(image=tk_im, command=lambda: thread_it(click_button4), text='读卡器', compound='center',
                        borderwidth=0, padx=0,
                        pady=0,
                        fg='white')
    button4.place(x=1, y=200)
    button5 = tk.Button(image=tk_im, command=lambda: thread_it(click_button5), text='显示器', compound='center',
                        borderwidth=0, padx=0,
                        pady=0,
                        fg='white')
    button5.place(x=1, y=240)
    button6 = tk.Button(image=tk_im, command=lambda: thread_it(click_button6), text='人脸识别', compound='center',
                        borderwidth=0, padx=0,
                        pady=0,
                        fg='white')
    button6.place(x=1, y=280)
    button7 = tk.Button(image=tk_im, command=lambda: thread_it(click_button7), text='样式选择', compound='center',
                        borderwidth=0, padx=0,
                        pady=0,
                        fg='white')
    button7.place(x=1, y=320)
    # </editor-fold>
    fm1 = Frame(window, canvas, tags='frame1')
    fm2 = Frame(window, canvas, tags='frame2')
    fm3 = Frame(window, canvas, tags='frame3')
    fm4 = Frame(window, canvas, tags='frame4')
    fm5 = Frame(window, canvas, tags='frame5')
    fm6 = Frame(window, canvas, tags='frame6')
    fm7 = Frame(window, canvas, tags='frame7')
    change_to_frame1()

    window.mainloop()
