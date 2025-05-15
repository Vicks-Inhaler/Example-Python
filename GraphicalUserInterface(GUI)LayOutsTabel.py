# PyQt5 LayOuts Introduction

# Jika tidak ada di <python 3.8 (Your Version Python)> => Lib => site-packages library install from Terminal :
# #        pip install PyQt5

print()
print()
print("========== Basic Image PyQt5 ==========")
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)
from PyQt5.QtGui import QPixmap

class MainWindow (QMainWindow) :
    def __init__(self) :
        super().__init__ ()
        self.setGeometry(400, 150, 500, 500)
        self.initUI()

    def initUI (self) :
        Central_Widget = QWidget ()
        self.setCentralWidget(Central_Widget)

        Label1 = QLabel ("#1", self)
        Label2 = QLabel ("#2", self)
        Label3 = QLabel ("#3", self)
        Label4 = QLabel ("#4", self)
        Label5 = QLabel ("#5", self)

        Label1.setStyleSheet ("Background-Color : Red;")
        Label2.setStyleSheet ("Background-Color : Yellow;")
        Label3.setStyleSheet ("Background-Color : Green;")
        Label4.setStyleSheet ("Background-Color : Blue;")
        Label5.setStyleSheet ("Background-Color : Purple;")

        # ===========================================================
        # VERTICALLY
        # ===========================================================
        VBox = QVBoxLayout ()

        VBox.addWidget (Label1)
        VBox.addWidget (Label2)
        VBox.addWidget (Label3)
        VBox.addWidget (Label4)
        VBox.addWidget (Label5)

        Central_Widget.setLayout(VBox)

        # ===========================================================
        # Horizontal
        # ===========================================================
        HBox = QHBoxLayout()

        HBox.addWidget(Label1)
        HBox.addWidget(Label2)
        HBox.addWidget(Label3)
        HBox.addWidget(Label4)
        HBox.addWidget(Label5)

        Central_Widget.setLayout(HBox)

        # ===========================================================
        # Grid Layouts
        # ===========================================================
        Grid = QGridLayout()

        Grid.addWidget(Label1)
        Grid.addWidget(Label2)
        Grid.addWidget(Label3)
        Grid.addWidget(Label4)
        Grid.addWidget(Label5)

        # -------------------------------------------------------------
        # OR
        # -------------------------------------------------------------
        Grid.addWidget(Label1, 0, 0)
        Grid.addWidget(Label2, 0, 1)
        Grid.addWidget(Label3, 1, 0)
        Grid.addWidget(Label4, 1, 1)
        # Grid.addWidget(Label5, 1, 2)
        # OR
        Grid.addWidget(Label5, 2, 2)
        Central_Widget.setLayout(Grid)

def Main () :
    App = QApplication (sys.argv)
    Window = MainWindow ()
    Window.show()
    sys.exit(App.exec_())

if __name__ == "__main__" :
    Main ()