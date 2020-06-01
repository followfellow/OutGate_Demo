import serial
import serial.tools.list_ports

class Serial_port:
    def __init__(self):
        self.serial_port_init(9600)

    def serial_port_init(self, bps):
        self.com_list = []
        self.bps = bps
        self.timeout = 5
        self.port_lst = list(serial.tools.list_ports.comports())
        try:
            for ii in range(0, len(self.port_lst)):
                self.com_list.append(list(self.port_lst[ii]))
                print(self.com_list[ii])
                # if 'COM4' in self.com_list[ii]:
                if any('USB' in s for s in self.com_list[ii]):
                    self.port = self.com_list[ii][0]

            self.ser = serial.Serial(self.port, self.bps, timeout=self.timeout)
            # 接收数据和发送数据数目置零
            self.data_num_received = 0
            # self.ui.lineEdit.setText(str(self.data_num_received))

            print("open:" + self.ser.name)
        except Exception as e:
            print("no port:", e)


if __name__ == '__main__':
    ser=Serial_port()
    ser.ser.write('abc'.encode())