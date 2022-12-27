import sys
from xml.etree.ElementInclude import include
from PyQt5.QtWidgets import *
app = QApplication(sys.argv) # sys 모듈의 argv는 명령 창에서 입력한 인수를 의미함 # 여기서는 절대 경로가 됨
# sys 참고 -> https://wikidocs.net/26
# print(sys.argv)
label = QLabel("PyQt First Test!") # text나 이미지를 만들때 사용함
label.show()

print("Before Loop")
app.exec_() # 이벤트 루프의 실행
print("After Loop")

# 참고
# https://martinii.fun/150