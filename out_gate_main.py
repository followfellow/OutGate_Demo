from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.Qt import Qt
import sys
import count
from post_update import Update
import serial_port

# import RPi.GPIO as GPIO

num = 0
BtnPin = 11


class MyThread(QtCore.QThread):
    my_signal = pyqtSignal(str)  # 自定义信号对象。参数str就代表这个信号可以传一个字符串

    def __init__(self):
        super().__init__()
        self.pdd = Update()

    def run(self):
        i = self.pdd.post_send()
        self.my_signal.emit(str(i))


class MainWindow(QtWidgets.QMainWindow, count.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = count.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label_2.setText('0')
        self.ui.label_3.setText('')
        self.pass_count = 0
        self.update_count = 0
        self.up = Update()
        self.t1 = MyThread()
        self.t1.my_signal.connect(self.data_receive)
        # self.IO_setup()

    def data_receive(self, msg):
        self.a = msg
        self.update_count+=1
        if self.a == '1':
            # self.ui.label_3.setText('')
            self.ui.label_3.setStyleSheet('color:green')
            self.ui.label_3.setText('网络正常')
        elif self.a == '0':
            self.ui.label_3.setStyleSheet('color:red')
            self.ui.label_3.setText('网络异常')
        # print('thread id', int(QtCore.QThread.currentThreadId()))

    # def IO_setup(self):
    #     GPIO.setmode(GPIO.BOARD)
    #     GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    #     GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=self.detect, bouncetime=100)

    def detect(self):
    # def detect(self,chn):
        self.pass_count += 1
        self.ui.label_2.setText(str(self.pass_count))
        if self.pass_count-self.update_count>2:
            self.ui.label_3.setStyleSheet('color:red')
            self.ui.label_3.setText('网络异常')
        # self.up.post_send()
        self.t1.start()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.pass_count += 1
            self.ui.label_2.setText(str(self.pass_count))
            if self.pass_count - self.update_count > 2:
                # self.ui.label_3.setStyleSheet('color:red')
                # self.ui.label_3.setText('网络异常')
                pass
            self.t1.start()
            # self.up.post_send()
            # print("鼠标左键点击")
        elif event.button() == Qt.RightButton:
            win.setStyleSheet("#MainWindow{border-image:url(检票1.jpg);}")
            print("鼠标右键点击")
        elif event.button() == Qt.MidButton:
            win.setStyleSheet("#MainWindow{border-image:url(通行5.jpg);}")
            print("鼠标中键点击")
            # QtCore.QCoreApplication.quit()


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.setStyleSheet("#MainWindow{border-image:url(images/检票1.jpg);}")
    win.setWindowOpacity(1)  # 透明度0~1
    # win.setStyleSheet("#MainWindow{background-color:yellow}")
    win.show()
    # win.showFullScreen()
    sys.exit(app.exec_())
