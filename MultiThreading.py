# MultiThreading = Used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from APIs threading.
#                  Thread (target=my_function)

print()
print("========== Basic Threading ==========")
import threading
import time

def Walk_Dog () :
    time.sleep(8)
    print("You Finish Walking The Dog")

def Take_Out_Trash () :
    time.sleep(2)
    print("You Take Out The Trash")

def Get_Mail () :
    time.sleep(4)
    print("You Get The Mail")

Walk_Dog()
Take_Out_Trash()
Get_Mail()

print("--------------- OR -----------------")

Chore1 = threading.Thread(target=Walk_Dog)
Chore1.start()

Chore2 = threading.Thread(target=Take_Out_Trash)
Chore2.start()

Chore3 = threading.Thread(target=Get_Mail)
Chore3.start()

# Tambahkan ini agar pembacaan dibawah Chore tidak mendahului selama Chore belum selesai semua
Chore1.join()
Chore2.join()
Chore3.join()

print()
print("All Chore are Complete!")

# ==================================================================

print()
print("========== Example 1 Threading ==========")
import threading
import time

# def Walk_Dog (First) :        # OR
def Walk_Dog (First, Last) :
    time.sleep(8)
    # print(f"You Finish Walking {First}")      # OR
    print(f"You Finish Walking {First} {Last}")

def Take_Out_Trash () :
    time.sleep(2)
    print("You Take Out The Trash")

def Get_Mail () :
    time.sleep(4)
    print("You Get The Mail")

# Chore1 = threading.Thread(target=Walk_Dog, args=("Kadal",))       # OR
Chore1 = threading.Thread(target=Walk_Dog, args=("Kadal","Mesir"))
Chore1.start()

Chore2 = threading.Thread(target=Take_Out_Trash)
Chore2.start()

Chore3 = threading.Thread(target=Get_Mail)
Chore3.start()

Chore1.join()
Chore2.join()
Chore3.join()
print()
print("All Chore are Complete!")