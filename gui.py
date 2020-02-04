from PyQt5 import QtCore, QtWidgets, uic
import serial
import sys

# serial port globals
SERIAL_PORT = 'COM1'
SERIAL_BAUD = 19200

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('gui.ui', self)

        # configure and initialize serial port
        # self.ser = serial.Serial()
        # self.ser.baudrate = SERIAL_BAUD
        # self.ser.port = SERIAL_PORT
        # self.ser.open()

        # lookup text widgets on gui
        self.ir_widget = self.findChild(QtWidgets.QLabel, 'ir_value')
        self.us_widget = self.findChild(QtWidgets.QLabel, 'us_value')
        self.pot_widget = self.findChild(QtWidgets.QLabel, 'pot_value')

        # initialize timer with update function
        self.my_timer = QtCore.QTimer()
        self.my_timer.timeout.connect(self.update_vals)
        self.my_timer.start(100) # 100 ms interval (10 hz)

        # show gui
        self.show()

    def parse_message(self, msg):
        msg = msg.strip()
        vals = msg.split(',')
        return vals
    
    def update_vals(self):
        # msg = self.ser.readline()
        msg = "42.251,52.32,5261\n" # temporary test message
        vals = self.parse_message(msg)

        self.ir_widget.setText(str(vals[0]))
        self.us_widget.setText(str(vals[1]))
        self.pot_widget.setText(str(vals[2]))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()