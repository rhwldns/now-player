import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
import os.path


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Now Music Player')
        self.move(300, 300)
        self.resize(400, 200)
        btn1 = QPushButton('플레이리스트 추가', self)
        btn1.move(20, 20)        
        btn1.clicked.connect(self.make_playlist)
        self.show()
    
    def make_playlist(self):
        self.lbl1 = QLabel('이름을 입력하세요')
        
        

        


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())