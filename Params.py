import json
import tkinter as tk


class Params:
    """Class that loads hyperparameters from a json file.
        Example:
        ```
        params = Params(json_path)
        print(params.learning_rate)
        params.learning_rate = 0.5  # change the value of learning_rate in params
        ```
        """

    def __init__(self, json_path):
        with open(json_path) as f:
            params = json.load(f)  # 将json格式数据转换为字典
            self.__dict__.update(params)

    def save(self, json_path):
        with open(json_path, 'w') as f:
            json.dump(self.__dict__, f, indent=4)  # indent缩进级别进行漂亮打印
            # json.dump(self.__dict__, f, ensure_ascii=False, indent=4)  # indent缩进级别进行漂亮打印

    def update(self, json_path):
        """Loads parameters from json file"""
        with open(json_path) as f:
            params = json.load(f)
            self.__dict__.update(params)

    @property  # Python内置的@property装饰器就是负责把一个方法变成属性调用的
    def dict(self):
        """Gives dict-like access to Params instance by `params.dict['learning_rate']"""
        return self.__dict__


class ReadParameters():
    def __init__(self):
        self.background_color_var = tk.StringVar()
        self.testing_mode_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.support_var = tk.StringVar()
        self.URL_var = tk.StringVar()
        self.GateNum_var = tk.StringVar()
        self.Interface_var = tk.StringVar()
        self.gate_form_var = tk.StringVar()
        self.three_var = tk.StringVar()
        self.wing_var = tk.StringVar()
        self.swing_var = tk.StringVar()
        self.swing_2_var = tk.StringVar()
        self.gate_mode_var = tk.StringVar()
        self.ticket_mode_var = tk.StringVar()
        self.code_check_var = tk.IntVar()
        self.idcard_check_var = tk.IntVar()
        self.code_com_var = tk.StringVar()
        self.code_com_2_var = tk.StringVar()
        self.code_com_3_var = tk.StringVar()
        self.idcard_set_var = tk.StringVar()
        self.zkong_com_var = tk.StringVar()
        self.screen_var = tk.StringVar()
        self.face_check_var = tk.IntVar()
        self.face_ip_var = tk.StringVar()
        self.threshold_var = tk.StringVar()
        self.number_var = tk.StringVar()
        # self.face_mode_var=tk.StringVar()
        self.face_mode_1_var = tk.IntVar()
        self.face_mode_n_var = tk.IntVar()
        self.rotate_var = tk.StringVar()
        self.index_var=tk.StringVar()
        self.ui_mode_var = tk.StringVar()
        self.temperature_var = tk.StringVar()

    def read_params(self, par):
        self.background_color_var.set(par.dict['BasePar']['image'])
        self.testing_mode_var.set(par.dict['BasePar']['testing'])
        self.name_var.set(par.dict['BasePar']['name'])
        self.support_var.set(par.dict['BasePar']['support'])
        self.URL_var.set(par.dict['BasePar']['URL'])
        self.GateNum_var.set(par.dict['BasePar']['GateNum'])
        self.Interface_var.set(par.dict['BasePar']['Interface'])
        self.gate_form_var.set(par.dict['GateForm']['gate_form'])
        self.three_var.set(par.dict['GateForm']['three'])
        self.wing_var.set(par.dict['GateForm']['wing'])
        self.swing_var.set(par.dict['GateForm']['swing'])
        self.swing_2_var.set(par.dict['GateForm']['swing_2'])
        self.gate_mode_var.set(par.dict['GateMode']['gate_mode'])
        self.ticket_mode_var.set(par.dict['GateMode']['ticket_mode'])
        self.code_check_var.set(par.dict['Reader']['code_check'])
        self.idcard_check_var.set(par.dict['Reader']['idcard_check'])
        self.code_com_var.set(par.dict['Reader']['code_com'])
        self.code_com_2_var.set(par.dict['Reader']['code_com_2'])
        self.code_com_3_var.set(par.dict['Reader']['code_com_3'])
        self.idcard_set_var.set(par.dict['Reader']['idcard_set'])
        self.zkong_com_var.set(par.dict['Reader']['zkong_com'])
        self.screen_var.set(par.dict['Screen']['screen'])
        self.face_check_var.set(par.dict['Face']['face_check'])
        self.face_ip_var.set(par.dict['Face']['face_ip'])
        self.threshold_var.set(par.dict['Face']['threshold'])
        # self.number_var.set(par.dict['Face']['num'])
        # self.face_mode_var.set(par.dict['Face']['face_mode'])
        self.face_mode_1_var.set(par.dict['Face']['face_mode_1'])
        self.face_mode_n_var.set(par.dict['Face']['face_mode_n'])
        self.rotate_var.set(par.dict['Face']['rotate'])
        self.index_var.set(par.dict['Face']['index'])
        self.ui_mode_var.set(par.dict['UiMode']['ui_mode'])
        self.temperature_var.set(par.dict['UiMode']['temperature'])
