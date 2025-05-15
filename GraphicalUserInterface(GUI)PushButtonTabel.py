# PyQt5 Push Button in Tabel Introduction

print()
print("========== Push Button Example Versi 1 ===========")
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel

class MainWindow (QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.setGeometry(400, 150, 500, 500)
        self.initUI ()

    def initUI (self) :
        self.Button = QPushButton ("Click Me!", self)
        self.Button.setGeometry (150, 200, 200, 100)
        self.Button.setStyleSheet ("Font-Size : 30px;")
        self.Button.clicked.connect (self.On_Click)

    def On_Click (self) :
        print("Button Clicked!")
        self.Button.setText ("Clicked!")

if __name__ == "__main__" :
    App = QApplication (sys.argv)
    Window = MainWindow ()
    Window.show ()
    sys.exit(App.exec_())

print()
print("========== Push Button Example Versi 2 ===========")
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel

class MainWindow (QMainWindow) :
    def __init__(self) :
        super().__init__()
        # Pindah Di Sini
        # self.Button = QPushButton("Click Me!", self)
        # Pindahkan Ke Bawah Sini
        self.setGeometry(400, 150, 500, 500)
        # Pindah Ke Bawah Sini
        self.Button = QPushButton("Click Me!", self)
        # Setelah tambahkan Di Bawah Sini, tambahkan juga Berikut
        self.Label = QLabel ("Hello", self)
        self.initUI ()

    def initUI (self) :
        # Note : Klik pada Button lalu klik tanda Lampu klik panah bawah => pilih (Move attribute to __init__Method)
        # Maka akan pindah ke Class MainWindow (QMainWindow) pada keterang # Pindah Di Sini
        # self.Button = QPushButton ("Click Me!", self)
        self.Button.setGeometry (150, 200, 200, 100)
        self.Button.setStyleSheet ("Font-Size : 30px;")
        self.Button.clicked.connect (self.On_Click)

        # Setelah tambahkan juga Berikut, Tambahkan juga hal ini
        self.Label.setGeometry(150, 300, 200, 100)
        self.Button.setStyleSheet("Font-Size : 50px;")

    def On_Click (self) :
        print("Button Clicked!")
        self.Button.setText ("Clicked!")
        # Setelah Pindah Ke Bawah tambahkan Di Bawah Sini
        self.Button.setDisabled(True)

if __name__ == "__main__" :
    App = QApplication (sys.argv)
    Window = MainWindow ()
    Window.show ()
    sys.exit(App.exec_())

print()
print("========== Push Button Example Versi 3 ===========")
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel

class MainWindow (QMainWindow) :
    def __init__(self) :
        super().__init__()
        # Pindah Di Sini
        # self.Button = QPushButton("Click Me!", self)
        # Pindahkan Ke Bawah Sini
        self.setGeometry(400, 150, 500, 500)
        # Pindah Ke Bawah Sini
        self.Button = QPushButton("Click Me!", self)
        # Setelah tambahkan Di Bawah Sini, tambahkan juga Berikut
        self.Label = QLabel ("Hello", self)
        self.Label.setStyleSheet("Font-Size : 50px;")
        self.initUI ()

    def initUI (self) :
        # Note : Klik pada Button lalu klik tanda Lampu klik panah bawah => pilih (Move attribute to __init__Method)
        # Maka akan pindah ke Class MainWindow (QMainWindow) pada keterang # Pindah Di Sini
        # self.Button = QPushButton ("Click Me!", self)
        self.Button.setGeometry (150, 200, 200, 100)
        self.Button.setStyleSheet ("Font-Size : 30px;")
        self.Button.clicked.connect (self.On_Click)

        # Setelah tambahkan juga Berikut, Tambahkan juga hal ini
        self.Label.setGeometry(150, 300, 200, 100)
        self.Button.setStyleSheet("Font-Size : 50px;")

    def On_Click (self) :
        self.Label.setText("GoodBye!")

if __name__ == "__main__" :
    App = QApplication (sys.argv)
    Window = MainWindow ()
    Window.show ()
    sys.exit(App.exec_())