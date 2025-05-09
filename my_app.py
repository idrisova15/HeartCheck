from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # проверка типов вводимых значений
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout, QGridLayout,
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)
 
from instr import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        ''' окно, в котором располагается приветствие '''
        super().__init__()
    
        #устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()
    
        # создаём и настраиваем графические элементы:
        self.initUI()
    
        #устанавливает связи между элементами
        self.connects()
    
        # старт:
        self.show()
    
    def initUI(self):
        ''' создаёт графические элементы '''
        self.btn_next = QPushButton(txt_next)
        self.hello_text = QLabel(txt_hello) 
        self.hello_text.setStyleSheet('''color: rgb(255, 255, 255);
                                      background-color: rgb(0,0,0);
                                      font-size: 25px;
                                      border: 15px double rgb(255, 0, 0);''')
        self.instruction = QLabel(txt_instruction)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.btn_next, alignment = Qt.AlignCenter)  
        self.setLayout(self.layout)
    
    def next_click(self):
        self.tw = TestWin()
        self.hide()
    
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    
    def set_appear(self):
        ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
 
app = QApplication([])
mw = MainWin()
app.exec_()
 
