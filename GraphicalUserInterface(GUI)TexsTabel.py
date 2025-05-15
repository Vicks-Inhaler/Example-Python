# PyQt5 Introduction

# Jika tidak ada di <python 3.8 (Your Version Python)> => Lib => site-packages library install from Terminal :
# #        pip install PyQt5

print()
print("========== Basic PyQt5 ==========")
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow (QMainWindow) :
    def __init__(self) :
        super().__init__ ()

def Main () :
    App = QApplication (sys.argv)
    Window = MainWindow ()
    Window.show()
    sys.exit(App.exec_())

if __name__ == "__main__" :
    Main ()

# ====================================================================
print()
print("========== Basic Lanjutan 1 PyQt5 ==========")
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
# Jika ingin memasukkan Icon Picture :
from PyQt5.QtGui import QIcon

class MainWindow (QMainWindow) :
    def __init__(self) :
        super().__init__ ()
        self.setWindowTitle("Kadal GUI")
        self.setGeometry(400, 150, 500, 500)               # Basic => self.setGeometry(X, Y, Width, Height)
        # Jika akan menginsert Icon Picture :
        self.setWindowIcon(QIcon("Razka.jpg"))

def Main () :
    App = QApplication (sys.argv)
    Window = MainWindow ()
    Window.show()
    sys.exit(App.exec_())

if __name__ == "__main__" :
    Main ()

# ====================================================================
print()
print("========== Basic Lanjutan 2 PyQt5 ==========")
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# Jika ingin memasukkan Icon Picture :
from PyQt5.QtGui import QIcon
# Jika ingin merubah Jenis dan Ukuran Font Tulisan dalam Label :
from PyQt5.QtGui import QFont
# Jika ingin mengatur Center Texs
from PyQt5.QtCore import Qt

class MainWindow (QMainWindow) :
    def __init__(self) :
        super().__init__ ()
        self.setWindowTitle("Kadal GUI")
        self.setGeometry(400, 150, 500, 500)               # Basic => self.setGeometry(X, Y, Width, Height)
        # Jika akan menginsert Icon Picture :
        self.setWindowIcon(QIcon("Razka.jpg"))
        # Menambahkan Tulisan dalam Tabel
        Label = QLabel ("Hello", self)
        # Merubah Jenis dan Ukuran Font di dalam Tabel :
        Label.setFont(QFont("Arial", 30))
        Label.setGeometry(0, 0, 500, 100)
        Label.setStyleSheet("Color : Blue;"                         # Jika menggunakan Color Picker Label.setStyleSheet("Color : #1fff5a;")
                            "Background-Color : #6fdcf7;"
                            "Font-Weight : Bold;"
                            "Font-Style : Italic;"
                            "Text-Decoration : Underline;")
        # # Mengatur Center Teks
        # Label.setAlignment(Qt.AlignTop)                             # VERTICALLY TOP
        # Label.setAlignment(Qt.AlignBottom)                          # VERTICALLY BOTTOM
        # Label.setAlignment(Qt.AlignVCenter)                         # VERTICALLY CENTER
        # Label.setAlignment(Qt.AlignRight)                           # HORIZONTALLY RIGHT
        # Label.setAlignment(Qt.AlignHCenter)                         # HORIZONTALLY CENTER
        # Label.setAlignment(Qt.AlignLeft)                            # HORIZONTALLY LEFT
        #
        # Label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)             # CENTER TOP
        # Label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)          # CENTER BOTTOM
        # Label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)         # CENTER CENTER
        Label.setAlignment(Qt.AlignCenter)                            # CENTER CENTER

def Main () :
    App = QApplication (sys.argv)
    Window = MainWindow ()
    Window.show()
    sys.exit(App.exec_())

if __name__ == "__main__" :
    Main ()