# PyQt 실행 -> 대기상태
# 시그널 : 이벤트 발생
# SLOT(슬롯) : 이벤트를 처리

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class TestForm(QMainWindow):
    def __init__(self):
        super().__init__() # super는 부모를 호출하기 웨 사용/여기선 QMainWidow 실행
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("PyQt Test")
        self.setGeometry(800,400,500,300)

        btn_1 = QPushButton("Click1", self)
        btn_2 = QPushButton("Click2", self)
        btn_3 = QPushButton("click3", self)

        btn_1.move(20,20)
        btn_2.move(20,60)
        btn_3.move(20,100)

        btn_1.clicked.connect(self.btn_1_clicked) # click이 시그널 btn_1 clicked는 슬롯 connect는 이를 연결
        btn_2.clicked.connect(self.btn_2_clicked)
        btn_3.clicked.connect(QCoreApplication.instance().quit) # 나가짐 / 외우기

    def btn_1_clicked(self):
        QMessageBox.about(self,"message","clicked")

    def btn_2_clicked(self):
        print("Button Clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()