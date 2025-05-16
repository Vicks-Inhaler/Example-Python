# PyQt5 Weather Application in Tabel Introduction
# Untuk Access Weather Application WebSite nya => https://openweathermap.org/

print()
print("========== PyQt5 Weather Application Example ==========")
import requests
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class WheatherApp (QWidget) :
    def __init__(self) :
        super().__init__ ()
        self.City_Label = QLabel ("Enter City Name : ", self)
        self.City_Input = QLineEdit (self)
        self.Get_Weather_Button = QPushButton ("Get Weather", self)
        # self.Temperature_Label = QLabel ("70°F", self)                    # For Test Program
        self.Temperature_Label = QLabel(self)
        # self.Emoji_Label = QLabel ("☉", self)                             # For Test Program
        self.Emoji_Label = QLabel(self)
        # self.Description_Label = QLabel ("Sunny", self)                   # For Test Program
        self.Description_Label = QLabel(self)
        self.initUI ()

    def initUI (self) :
        self.setWindowTitle ("Weather App")

        VBox = QVBoxLayout ()
        VBox.addWidget (self.City_Label)
        VBox.addWidget (self.City_Input)
        VBox.addWidget (self.Get_Weather_Button)
        VBox.addWidget (self.Temperature_Label)
        VBox.addWidget (self.Emoji_Label)
        VBox.addWidget (self.Description_Label)

        self.setLayout (VBox)

        self.City_Label.setAlignment (Qt.AlignCenter)
        self.City_Input.setAlignment(Qt.AlignCenter)
        self.Temperature_Label.setAlignment(Qt.AlignCenter)
        self.Emoji_Label.setAlignment(Qt.AlignCenter)
        self.Description_Label.setAlignment(Qt.AlignCenter)

        self.City_Label.setObjectName ("City_Label")
        self.City_Input.setObjectName("City_Input")
        self.Get_Weather_Button.setObjectName("Get_Weather_Button")
        self.Temperature_Label.setObjectName("Temperature_Label")
        self.Emoji_Label.setObjectName("Emoji_Label")
        self.Description_Label.setObjectName("Description_Label")

        self.setStyleSheet ("""
            QLabel, QPushButton {
                Font-Family : Calibri;
            }
            QLabel#City_Label {
                Font-Size : 40px;
                Font-Style : Italic;
            }
            QLineEdit#City_Input {
                Font-Size : 40px;
            }
            QPushButton#Get_Weather_Button {
                Font-Size : 30px;
                Font-Weight : Bold;
            }
            QLabel#Temperature_Label {
                Font-Size : 75px;
            }
            QLabel#Emoji_Label {
                Font-Size : 100px;
                Font-Family : Segoe UI emoji;
            }
            QLabel#Description_Label {
                Font-Size : 50px;
            }
        """)

        self.Get_Weather_Button.clicked.connect (self.Get_Weather_App)

    def Get_Weather_App (self) :
        # print("You Get the Weather")                              # For Test Program
        Api_Key = "0940ec3b7dcf019a4a94e338cec04335"                # From WebSite Wheater App => https://openweathermap.org/
                                                                    # => Klik Your Account => My API Keys => Copy, and Paste Here
        City = self.City_Input.text ()
        # From WebSite Wheater App => https://openweathermap.org/
        # => Klik Menu API, Scroll Down => Current Weather Data Klik API doc => Klik Built-in API request by city name
        # => Copy API q={city name}&appid={API key}, Paste Here :
        URL = f"https://api.openweathermap.org/data/2.5/weather?q={City}&appid={Api_Key}"
        # Change {City Name} => Your Initial City, {API Key} => Your Initial Api_Key

        # Response = requests.get(URL)          # For Test Program
        # Data = Response.json()                # For Test Program
        #
        # # print(Data)                         # For Test Program
        # if Data["cod"] == 200:                # For Test Program
        #     self.Display_Weather(Data)        # For Test Program
        # else :                                # For Test Program
        #     print(Data)                       # For Test Program

        try :
            Response = requests.get(URL)
            Response.raise_for_status()
            Data = Response.json ()

            # print(Data)                           # For Test Program
            if Data ["cod"] == 200 :
                self.Display_Weather(Data)
            # else :                                # For Test Program
            #     print(Data)                       # For Test Program

        except requests.exceptions.HTTPError as HTTP_Error:
            # print(Response.status_code)           # For Test Program

            # # Untuk Versi Python 3.10 Lebih Dapat Menggunakan match :
            # # =======================================================
            # match Response.status_code :
            #     case 400 :
            #         print("Bad Request\nPlease Check Your Input!")
            #     case 401 :
            #         print("UnAuthorized\nInvalid Key!")
            #     case 403 :
            #         print("Forbidden\nAccess is Denied!")
            #     case 404 :
            #         print("Not Found\nCity Not Found!")
            #     case 500 :
            #         print("Internal Server Error\nPlease Try Again Later!")
            #     case 502 :
            #         print("Bad Gateway\nInvalid Respon From the Server!")
            #     case 503 :
            #         print("Service UnAvailable\nServer is Down!")
            #     case 504 :
            #         print("Gateway Time Out\nNo Response From the Server!")
            #     case _ :
            #         print(f"HTTP Error Occured\n{HTTP_Error}")

            # Untuk Versi Python 3.9 dan Sebelumnya Dapat Menggunakan if else :
            # =================================================================
    #         # For Test :
    #         # -----------------------------------------------------------------
    #         status_code = Response.status_code
    #
    #         if status_code == 400:
    #             print("Bad Request\nPlease Check Your Input!")
    #         elif status_code == 401:
    #             print("UnAuthorized\nInvalid Key!")
    #         elif status_code == 403:
    #             print("Forbidden\nAccess is Denied!")
    #         elif status_code == 404:
    #             print("Not Found\nCity Not Found!")
    #         elif status_code == 500:
    #             print("Internal Server Error\nPlease Try Again Later!")
    #         elif status_code == 502:
    #             print("Bad Gateway\nInvalid Response From the Server!")
    #         elif status_code == 503:
    #             print("Service UnAvailable\nServer is Down!")
    #         elif status_code == 504:
    #             print("Gateway Time Out\nNo Response From the Server!")
    #         else:
    #             print(f"HTTP Error Occurred\n{HTTP_Error}")
    #
    #     except requests.exceptions.ConnectionError:
    #         print("Connection Error :\nCheck Your Internet Connection!")
    #
    #     except requests.exceptions.Timeout:
    #         print("Timeout Error :\nThe Request Timed Out!")
    #
    #     except requests.exceptions.TooManyRedirects:
    #         print("Too Many Redirects :\nCheck the URL!")
    #
    #     except requests.exceptions.RequestException as Req_Error:
    #         print(f"Request Error :\n{Req_Error}")
    #
    # def Display_Error(self, Message):
    #     pass
    #
    # def Display_Weather(self, Data):
    #     print(Data)

            # For App :
            # -----------------------------------------------------------------
            status_code = Response.status_code

            if status_code == 400:
                self.Display_Error("Bad Request :\nPlease Check Your Input!")
            elif status_code == 401:
                self.Display_Error("UnAuthorized :\nInvalid Key!")
            elif status_code == 403:
                self.Display_Error("Forbidden :\nAccess is Denied!")
            elif status_code == 404:
                self.Display_Error("Not Found :\nCity Not Found!")
            elif status_code == 500:
                self.Display_Error("Internal Server Error :\nPlease Try Again Later!")
            elif status_code == 502:
                self.Display_Error("Bad Gateway :\nInvalid Response From the Server!")
            elif status_code == 503:
                self.Display_Error("Service UnAvailable :\nServer is Down!")
            elif status_code == 504:
                self.Display_Error("Gateway Time Out :\nNo Response From the Server!")
            else:
                self.Display_Error(f"HTTP Error Occurred :\n{HTTP_Error}")

        except requests.exceptions.ConnectionError :
            self.Display_Error("Connection Error :\nCheck Your Internet Connection!")

        except requests.exceptions.Timeout :
            self.Display_Error("Timeout Error :\nThe Request Timed Out!")

        except requests.exceptions.TooManyRedirects :
            self.Display_Error("Too Many Redirects :\nCheck the URL!")

        except requests.exceptions.RequestException as Req_Error :
            self.Display_Error(f"Request Error :\n{Req_Error}")

    def Display_Error (self, Message) :
        self.Temperature_Label.setStyleSheet ("Font-Size : 30px;")
        self.Temperature_Label.setText (Message)
        self.Emoji_Label.clear ()
        self.Description_Label.clear ()

    def Display_Weather (self, Data) :
        # print(Data)                                                   # For Test Program
        self.Temperature_Label.setStyleSheet("Font-Size : 75px;")
        Temperature_K = Data ["main"] ["temp"]
        Temperature_C = Temperature_K - 273.15
        Temperature_F = (Temperature_K * 9 / 5) - 459.67
        Weather_ID = Data ["weather"] [0] ["id"]
        Weather_Description = Data ["weather"] [0] ["description"]

        # print(Temperature_C)                                          # For Test Program
        # self.Temperature_Label.setText (f"{Temperature_F : .0f} °F")
        self.Temperature_Label.setText(f"{Temperature_C : .0f} °C")
        self.Emoji_Label.setText (self.Get_Emoji_Weather(Weather_ID))
        self.Description_Label.setText (Weather_Description)

    @staticmethod
    def Get_Emoji_Weather (Weather_ID) :

        # Website Copy Paste Emoji for Win 7 => https://emojipedia.org/ OR https://getemoji.com/
        if 200 <= Weather_ID <= 232 :
            return "🌉"
        elif 300 <= Weather_ID <= 321 :
            return "⛅"
        elif 500 <= Weather_ID <= 531 :
            return "💫"
        elif 600 <= Weather_ID <= 622 :
            return "❄"
        elif 700 <= Weather_ID <= 741 :
            return "🌁"
        elif Weather_ID == 762 :
            return "🔯"
        elif Weather_ID == 771 :
            return "💨"
        elif Weather_ID == 781 :
            return "❣"
        elif Weather_ID == 800 :
            return "☀"
        elif 801 <= Weather_ID <= 804 :
            return "🌟"
        else :
            return ""

if __name__ == "__main__" :
    App = QApplication (sys.argv)
    Weather_App = WheatherApp ()
    Weather_App.show ()
    sys.exit(App.exec_())