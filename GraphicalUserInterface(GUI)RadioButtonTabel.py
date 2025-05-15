# PyQt5 Radio Button in Tabel Introduction

print()
print("========== Radio Button Example ==========")
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

class MainWindow (QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.setGeometry (400, 150, 500, 500)
        self.Radio1 = QRadioButton ("Visa", self)
        self.Radio2 = QRadioButton("Mastercard", self)
        self.Radio3 = QRadioButton("Gift Card", self)
        self.Radio4 = QRadioButton("In-Store", self)
        self.Radio5 = QRadioButton("Online", self)
        self.Button_Group1 = QButtonGroup (self)
        self.Button_Group2 = QButtonGroup (self)
        self.initUI ()

    def initUI (self) :
        self.Radio1.setGeometry (0, 0, 300, 50)
        self.Radio2.setGeometry (0, 50, 300, 50)
        self.Radio3.setGeometry (0, 100, 300, 50)
        self.Radio4.setGeometry(0, 150, 300, 50)
        self.Radio5.setGeometry(0, 200, 300, 50)

        self.setStyleSheet ("QRadioButton {"
                            "Font-Size : 40px;"
                            "Font-Family : Arial;"
                            "Padding : 10px;""}")

        self.Button_Group1.addButton (self.Radio1)
        self.Button_Group1.addButton (self.Radio2)
        self.Button_Group1.addButton (self.Radio3)
        self.Button_Group2.addButton (self.Radio4)
        self.Button_Group2.addButton (self.Radio5)

        self.Radio1.toggled.connect (self.Radio_Button_Change)
        self.Radio2.toggled.connect(self.Radio_Button_Change)
        self.Radio3.toggled.connect(self.Radio_Button_Change)
        self.Radio4.toggled.connect(self.Radio_Button_Change)
        self.Radio5.toggled.connect(self.Radio_Button_Change)

    def Radio_Button_Change (self) :
        # print("Your Selected Something")                        # For Test

        Radio_Button = self.sender()

        if Radio_Button.isChecked () :
            print(f"{Radio_Button.text()} is Selected")

if __name__ == '__main__' :
    App = QApplication (sys.argv)
    Window = MainWindow ()
    Window.show ()
    sys.exit (App.exec_())