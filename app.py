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
        self.initUI()

    def initUI(self):
        # text
        label = QtWidgets.QLabel(win)
        label.setText("Welcome")
        label.move(100, 20)

        # buttons
        b_cam = QtWidgets.QPushButton()
        b_cam.setText("camera")
        b_cam.clicked.connect(Buttons.cam)




class Buttons:
    def cam():
        pass


def window():
    # base setup
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setGeometry(xpos, ypos, width, height)
    win.setWindowTitle("Object Classifier")


    # exit
    win.show()
    sys.exit(app.exec_())


# test
window()
