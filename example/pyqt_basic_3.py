import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore

class TestForm(QMainWindow):
    def __init__(self):
        super().__init__() # super는 부모를 호출하기 웨 사용/여기선 QMainWideo 실행
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("PyQt Test")
        self.setGeometry(800,400,500,500)

        label_1 = QLabel("입력 테스트",self)
        label_2 = QLabel("출력 테스트",self)

        label_1.move(20,20)
        label_2.move(20,60)

        self.lineEdit = QLineEdit("",self) # Default 값 # "" -> 기본값 # QlineEdit -> 한줄짜리 글을 입력받는 상자
        self.plainEdit = QtWidgets.QPlainTextEdit(self) # QpainTextEdit -> 사진 및 글 등을 가져 올수 있는 상자 가져옴
        # self.plainEdit.setReadOnly(True)
        
        self.lineEdit.move(90,20)
        self.plainEdit.setGeometry(QtCore.QRect(20,90,361,231)) # Qtcore.Qrect는 방향
        
        self.lineEdit.textChanged.connect(self.lineEditChanged)
        self.lineEdit.returnPressed.connect(self.lineEditEnter)

        # 상태바(창 밑에 부분)
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def lineEditChanged(self):
        self.statusBar.showMessage(self.lineEdit.text())
    
    # 줄 바꿈 # 입력테스트 -> 출력 테스트로
    def lineEditEnter(self):
        self.plainEdit.appendPlainText(self.lineEdit.text()) # insertPlaintext -> 뒤에 갖다 붙혀줌
        self.lineEdit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()