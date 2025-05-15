# PyQt5 CheckBoxes in Tabel Introduction

print()
print("========== CheckBoxes Example ==========")
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow (QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.setGeometry (400, 150, 500, 500)
        self.CheckBoxes = QCheckBox ("Do You Like Food?", self)
        self.initUI ()

    def initUI (self) :
        self.CheckBoxes.setGeometry (10, 0, 500, 100)
        self.CheckBoxes.setStyleSheet ("Font-Size : 30px;"
                                       "Font-Family : Arial;")
        self.CheckBoxes.setChecked (False)                              # True = Centang, False = Not Centang
        self.CheckBoxes.stateChanged.connect (self.CheckBoxes_Change)

    def CheckBoxes_Change (self, State) :
        # print(State)                        # For Test : Nilai 0 output artinya Not Checked, Nilai 2 artinya Checked
        if State == Qt.Checked :
            print("You Like Food")
        else :
            print("You Do Not Like Food")

if __name__ == '__main__' :
    App = QApplication (sys.argv)
    Window = MainWindow ()
    Window.show()
    sys.exit(App.exec_())