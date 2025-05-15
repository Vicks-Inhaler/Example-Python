# PyQt5 LineEdit in Tabel Introduction

print()
print("========== Line Edit Example ==========")
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

class MainWindow(QMainWindow) :
    def __init__ (self) :
        super().__init__ ()
        self.setGeometry(400, 150, 500, 500)
        self.Line_Edit = QLineEdit (self)
        self.Button = QPushButton ("Submit", self)
        self.initUI ()

    def initUI (self) :
        self.Line_Edit.setGeometry (10, 10, 200, 40)
        self.Button.setGeometry (210, 10, 100, 40)
        self.Line_Edit.setStyleSheet ("Font-Size : 25px;"
                                      " Font-Family : Arial")
        self.Button.setStyleSheet("Font-Size : 25px;"
                                     " Font-Family : Arial")
        self.Line_Edit.setPlaceholderText ("Enter Your Name")

        self.Button.clicked.connect(self.Submit)

    def Submit (self) :
        # print("You Clicked the Button")                       # For Test
        Text = self.Line_Edit.text ()
        print(f"Hello {Text}")

if __name__ == '__main__' :
    App = QApplication (sys.argv)
    Window = MainWindow ()
    Window.show ()
    sys.exit (App.exec_())