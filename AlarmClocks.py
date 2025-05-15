# Python Alarm Clocks

print()
import time
import datetime
import pygame

# Note :
# Jika File pygame tidak terdapat di library Python maka :
# Klik Menu Terminal Python, kemudian ketikkan => pip install pygame
# Jika ingin melihat versi pygame jika sudah terinstall => pip show pygame

def Set_Alarm (Alarm_Time) :
    print()
    print(f"Alarm Set for {Alarm_Time}")
    Sound_File = "jingle-bells-alarm-clock-version-129333.mp3"
    Is_Running = True

    # Note :
    # Copy Paste File .mp3 yang akan dijadikan File alarm ke Folder program berjalan, misalnya disini :
    # Di Folder => Example-Python

    print()
    while Is_Running :
        Current_Time = datetime.datetime.now().strftime("%H:%M:%S")
        print(Current_Time)

        if Current_Time == Alarm_Time :
            print()
            print("WAKE UP!")

            pygame.mixer.init()
            pygame.mixer.music.load(Sound_File)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy() :
                time.sleep(1)

            Is_Running = False

        # Is_Running = False
        time.sleep(1)

if __name__ == "__main__" :
    Alarm_Time = input("Enter the Alarm Time (HH:MM:SS) : ")
    Set_Alarm(Alarm_Time)

    # Note :
    # Jika Output Running Python Keluar tulisan
    #         pygame 2.6.1(SDL 2.28.4, Python 3.8.10)
    #         Hello from the pygame community.https: // www.pygame.org / contribute.html
    # Maka Hapus Tulisan tersebut di :
    # External Libraries => <Python 3.8 (Versi Pythonmu)> => Lib => site-packages => pygame => __init__.py
    # Cari Tulisan berikut :
    #         if "PYGAME_HIDE_SUPPORT_PROMPT" not in os.environ:
    #             print(
    #                 "pygame {} (SDL {}.{}.{}, Python {}.{}.{})".format(  # pylint: disable=consider-using-f-string
    #                     ver, *get_sdl_version() + sys.version_info[0:3]
    #                 )
    #             )
    #             print("Hello from the pygame community. https://www.pygame.org/contribute.html")
    # Hapus Tulisan tersebut dan close file __init__.py