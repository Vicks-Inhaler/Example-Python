# PyQt5 Stop Watch in Tabel Introduction

print()
print("========== PyQt5 Stop Watch Example ==========")
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import QTimer, QTime, Qt

class Stop_Watch (QWidget) :
    def __init__(self) :
        super().__init__ ()
        self.Time = QTime (0, 0, 0, 0)
        self.Time_Label = QLabel ("00:00:00.00", self)
        self.Start_Button = QPushButton ("Start", self)
        self.Stop_Button = QPushButton ("Stop", self)
        self.Reset_Button = QPushButton ("Reset", self)
        self.Timer = QTimer (self)
        self.initUI ()

    def initUI (self) :
        self.setWindowTitle ("STOPWATCH")

        VBox = QVBoxLayout ()
        VBox.addWidget (self.Time_Label)

        self.setLayout (VBox)

        self.Time_Label.setAlignment (Qt.AlignCenter)

        HBox = QHBoxLayout ()
        HBox.addWidget (self.Start_Button)
        HBox.addWidget (self.Stop_Button)
        HBox.addWidget (self.Reset_Button)

        VBox.addLayout (HBox)

        self.setStyleSheet ("""
            QPushButton, QLabel{
                Padding : 20px;
                Font-Weight : Bold;
                Font-Family : Calibri;
            }
            QPushButton {
                Font-Size : 50px;
            }
            QLabel {
                Font-Size : 120px;
                Background-Color : hsl(200, 100%, 85%);
                Border-Radius : 20px;
            }
        """)

        self.Start_Button.clicked.connect (self.Start)
        self.Stop_Button.clicked.connect (self.Stop)
        self.Reset_Button.clicked.connect (self.Reset)
        self.Timer.timeout.connect (self.Update_Display)

    def Start (self) :
        self.Timer.start (10)

    def Stop (self) :
        self.Timer.stop ()

    def Reset (self) :
        self.Timer.stop()
        self.Time = QTime (0, 0, 0, 0)
        self.Time_Label.setText (self.Format_Time(self.Time))

    def Format_Time (self, Time) :
        Hours = Time.hour ()
        Minutes = Time.minute ()
        Seconds = Time.second ()
        MilliSeconds = Time.msec () // 10                   # // 10 => Integer division 2 Digit
        return f"{Hours:02}:{Minutes:02}:{Seconds:02}.{MilliSeconds:02}"

    def Update_Display (self) :
        self.Time = self.Time.addMSecs (10)
        self.Time_Label.setText (self.Format_Time(self.Time))

if __name__ == "__main__" :
    App = QApplication (sys.argv)
    StopWatch = Stop_Watch ()
    StopWatch.show ()
    sys.exit(App.exec_())