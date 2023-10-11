from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, QComboBox
import serial.tools.list_ports
import time


app = QApplication([])


class MainWindow(QMainWindow):
    combo_box_1 = QComboBox()
    label_1 = QLabel()
    label_2 = QLabel()
    line_edit_1 = QLineEdit("<SMB>")
    button_1 = QPushButton("connect")
    button_2 = QPushButton("send command")
    ports = serial.tools.list_ports.comports()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("COM PHP")
        self.setFixedSize(QSize(400, 300))

        layout = QVBoxLayout()

        for port in self.ports:
            self.combo_box_1.addItem(port.device)
        layout.addWidget(self.combo_box_1)

        self.button_1.setCheckable(True)
        self.button_1.clicked.connect(self.clicked_button_connect_com)
        self.setCentralWidget(self.button_1)
        layout.addWidget(self.button_1)

        layout.addWidget(self.label_1)
        layout.addWidget(self.label_2)
        layout.addWidget(self.line_edit_1)

        self.button_2.setCheckable(True)
        self.button_2.clicked.connect(self.the_button_was_clicked)
        self.setCentralWidget(self.button_2)
        layout.addWidget(self.button_2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def clicked_button_connect_com(self):
        ser = serial.Serial(self.combo_box_1.currentText(), baudrate=9600)
        self.label_1.setText("")

        while True:
            line = ser.read().decode()

            if line:
                self.label_1.setText(self.label_1.text() + line)
                print(self.label_1.text() + line)

                if line == '>':
                    break
        ser.close()

    def the_button_was_clicked(self):
        ser = serial.Serial(self.combo_box_1.currentText(), baudrate=9600)
        self.label_2.setText(self.line_edit_1.text())
        ser.write(self.line_edit_1.text().encode())
        self.label_1.setText("")

        while True:
            line = ser.read().decode()

            if line:
                self.label_1.setText(self.label_1.text() + line)
                print(self.label_1.text() + line)

                if line == '>':
                    break

        ser.close()


window = MainWindow()
window.show()

app.exec()
"""


port = "COM6"  # Replace with the appropriate COM port name
baudrate = 9600

try:
    # Open the COM port
    ser = serial.Serial(port, baudrate=baudrate)
    print("Serial connection established.")

    # Read data from the Arduino
    while True:
        #line = ser.readline().decode().strip()
        line = ser.readline(1).decode()

        if line:
            print(line)


except serial.SerialException as se:
    print("Serial port error:", str(se))

except KeyboardInterrupt:
    pass

finally:
    # Close the serial connection
    if ser.is_open:
        ser.close()
        print("Serial connection closed.")
"""