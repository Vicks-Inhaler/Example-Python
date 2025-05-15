# PyQt5 SetStyleSheet() in Tabel Introduction

print()
print("========== Set StyleSheet() Example ==========")
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout

class MainWindow(QMainWindow) :
    def __init__ (self) :
        super().__init__ ()
        self.Button1 = QPushButton ("#1")
        self.Button2 = QPushButton ("#2")
        self.Button3 = QPushButton ("#3")
        self.initUI ()

    def initUI (self) :
        Central_Widget = QWidget ()
        self.setCentralWidget (Central_Widget)

        HBox = QHBoxLayout ()

        HBox.addWidget (self.Button1)
        HBox.addWidget (self.Button2)
        HBox.addWidget (self.Button3)

        Central_Widget.setLayout (HBox)

        self.Button1.setObjectName ("Button1")
        self.Button2.setObjectName ("Button2")
        self.Button3.setObjectName ("Button3")

        self.setStyleSheet ("""
            QPushButton{
                Font-Size : 40px;
                Font-Family : Arial;
                Padding : 15px 75px;
                Margin : 25px;
                Border : 3px Solid;
                Border-Radius : 15px;
            }
            QPushButton#Button1 {
                Background-Color : hsl(0, 100%, 64%);
            }
            QPushButton#Button2 {
                Background-Color : hsl(122, 100%, 64%);
            }
            QPushButton#Button3 {
                Background-Color : hsl(204, 100%, 64%);
            }
            QPushButton#Button1:hover {
                Background-Color : hsl(0, 100%, 84%);
            }
            QPushButton#Button2:hover {
                Background-Color : hsl(122, 100%, 84%);
            }
            QPushButton#Button3:hover {
                Background-Color : hsl(204, 100%, 84%);
            }
        """)

if __name__ == '__main__' :
    App = QApplication (sys.argv)
    Window = MainWindow ()
    Window.show ()
    sys.exit (App.exec_())

#======================================================================================
# Note :
# QPushButton{
#                 Font-Size : 40px;
#                 Font-Family : Arial;
#                 Padding : 15px 75px;
#                 Margin : 25px;
#                 Border : 3px Solid;
#                 Border-Radius : 15px;
#                 # Background-Color : Red;           # Jika ingin semua Backgroud sama warnanya
#             }
#             QPushButton#Button1 {
#                 # Background-Color : Red;
#                 # OR
#                 # Background-Color : #ff4747;
#                 # OR
#                 # Background-Color : rgb(255, 71, 71);
#                 # OR
#                 Background-Color : hsl(0, 100%, 64%);                 # Warna dengan Saturasi
#             }
#             QPushButton#Button2 {
#                 # Background-Color : Green;
#                 Background-Color : hsl(122, 100%, 64%);               # Warna dengan Saturasi
#             }
#             QPushButton#Button3 {
#                 # Background-Color : Blue;
#                 Background-Color : hsl(204, 100%, 64%);               # Warna dengan Saturasi
#             }
#             QPushButton#Button1:hover {                               # Warna dengan Lightnest Perubahan Saat Disorot Cursor
#                 Background-Color : hsl(0, 100%, 84%);
#             }
#             QPushButton#Button2:hover {                               # Warna dengan Lightnest Perubahan Saat Disorot Cursor
#                 Background-Color : hsl(122, 100%, 84%);
#             }
#             QPushButton#Button3:hover {                               # Warna dengan Lightnest Perubahan Saat Disorot Cursor
#                 Background-Color : hsl(204, 100%, 84%);
#             }