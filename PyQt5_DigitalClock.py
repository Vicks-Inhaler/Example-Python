# PyQt5 Digital Clock in Tabel Introduction

print()
print("========== PyQt5 Digital Clock Example ==========")
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
# Note :
# Untuk Menginputkan Custom Style Font Clock dengan DS Digital => Download Font Clock di https://www.dafont.com/ds-digital.font
# Kemudian Copy File DS-DIGIT.TTF ke Folder Program Python/Pycharm-mu, Kemudian tambahkan script dibawah ini
from PyQt5.QtGui import QFont, QFontDatabase            # Kemudian delete Font keterangan dibawah

class DigitalClock (QWidget) :
    def __init__(self) :
        super().__init__ ()
        self.Time_Label = QLabel ("12:00:00", self)
        self.Timer = QTimer (self)
        self.initUI ()

    def initUI (self) :
        self.setWindowTitle ("Digital Clock")
        self.setGeometry (600, 400, 300, 100)

        VBox = QVBoxLayout ()
        VBox.addWidget (self.Time_Label)
        self.setLayout (VBox)

        self.Time_Label.setAlignment (Qt.AlignCenter)
        self.Time_Label.setStyleSheet ("Font-Size : 150px;"
                                       # "Font-Family : Arial;"              # Delete Font ini kemudian tambahkan Script dibawah
                                       # "Color : Green;")                   # OR Color With Lighnest Dibawah
                                       "Color : hsl(111, 100%, 50%);")
        self.setStyleSheet ("Background-Color : Black;")

        # Tambahkan Script berikut
        Font_ID = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        Font_Family = QFontDatabase.applicationFontFamilies(Font_ID)[0]
        My_Font = QFont (Font_Family, 150)
        self.Time_Label.setFont(My_Font)

        self.Timer.timeout.connect(self.Update_Time)
        self.Timer.start(1000)

        self.Update_Time()

    def Update_Time (self) :
        Current_Time = QTime.currentTime().toString("hh:mm:ss AP")
        self.Time_Label.setText(Current_Time)

if __name__ == "__main__" :
    App = QApplication (sys.argv)
    Clock = DigitalClock ()
    Clock.show ()
    sys.exit(App.exec_())