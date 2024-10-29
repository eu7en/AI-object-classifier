### gui interface 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# window geometry variables
xpos=100
ypos=100
width=1000
height=700

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setGeometry(xpos, ypos, width, height)
        self.setWindowTitle("Object Classifier")
        
        self.initUI()

    def initUI(self):
        # text
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Welcome")
        self.label.move(100, 20)

        # buttons
        self.b_cam = QtWidgets.QPushButton(self)
        self.b_cam.setText("camera")
        self.b_cam.clicked.connect(self.cam)

    def update(self):
        self.label.adjustSize()

    def cam(self):
        self.label.setText("you pushed the button")
        self.update()





def window():
    # using MyWindow class
    app = QApplication(sys.argv)
    win = MyWindow()

    # exit
    win.show()
    sys.exit(app.exec_())


# test
window()
