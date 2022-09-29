# DemoForm.py
# DemoForm.ui(화면단) + DemoForm.py(로직단)
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 
#화면로딩
form_class = uic.loadUiType("Demoform.ui")[0]
#클래스 정의
class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 화면")

app = QApplication(sys.argv)
demoWindow = DemoForm()
demoWindow.show() 
app.exec_()