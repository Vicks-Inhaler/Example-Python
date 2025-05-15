# PyQt5 Image Introduction

# Jika tidak ada di <python 3.8 (Your Version Python)> => Lib => site-packages library install from Terminal :
# #        pip install PyQt5

print()
print()
print("========== Basic Image PyQt5 ==========")
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow (QMainWindow) :
    def __init__(self) :
        super().__init__ ()
        self.setGeometry(400, 150, 500, 500)

        Label = QLabel (self)
        # Label.setGeometry(0, 0, 250, 250)                     # For Test
        Label.setGeometry(0, 0, 250, 250)

        Pixmap = QPixmap ("Razka.jpg")
        Label.setPixmap(Pixmap)

        Label.setScaledContents(True)

        # Label.setGeometry(130, 130, 250, 250)                 # For Test => Label.setGeometry(0, 0, Label.Width(), Label.Height())
        Label.setGeometry ((self.width() // 2 - Label.width() // 2),
                           (self.height() // 2 - Label.height() // 2),
                           Label.width(),
                           Label.height())

def Main () :
    App = QApplication (sys.argv)
    Window = MainWindow ()
    Window.show()
    sys.exit(App.exec_())

if __name__ == "__main__" :
    Main ()