print()
import random
import string

Chars = string.punctuation + string.digits + string.ascii_letters
Chars1 = string.whitespace + string.punctuation + string.digits + string.ascii_letters
Chars2 = " " + string.punctuation + string.digits + string.ascii_letters
Chars3 = " " + string.punctuation + string.digits + string.ascii_letters
Chars4 = " " + string.punctuation + string.digits + string.ascii_letters
Chars5 = " " + string.punctuation + string.digits + string.ascii_letters

Chars3 = list(Chars3)
Chars4 = list(Chars4)
Chars5 = list(Chars5)

Key3 = Chars3.copy()
Key4 = Chars4.copy()
Key5 = Chars5.copy()

random.shuffle(Key4)
random.shuffle(Key5)

print(Chars)
print(Chars1)
print(Chars2)

print()
print(f"Chars : {Chars3}")
print(f"Key : {Key3}")

print()
print(f"Chars : {Chars4}")
print(f"Key : {Key4}")

# ENCRYPT
print()
print("========== ONLY ENCRYPT ==========")
Plain_Text4 = input("Enter a Message to Encrypt : ")
Cipher_Text4 = ""

for Letter4 in Plain_Text4 :
    Index4 = Chars4.index(Letter4)
    Cipher_Text4 += Key4[Index4]

print()
print(f"Original Message : {Plain_Text4}")
print(f"Encrypted Message : {Cipher_Text4}")

#=======================================================
# ENCRYPT
print()
print("========== To ENCRYPT ==========")
Plain_Text5 = input("Enter a Message to Encrypt : ")
Cipher_Text5 = ""

for Letter5 in Plain_Text5 :
    Index5 = Chars5.index(Letter5)
    Cipher_Text5 += Key5[Index5]

print()
print(f"Original Message : {Plain_Text5}")
print(f"Encrypted Message : {Cipher_Text5}")

# DECRYPT
print()
print("========== To DECRYPT ==========")
Cipher_Text5 = input("Enter a Message to Encrypt : ")
Plain_Text5 = ""

for Letter5 in Cipher_Text5 :
    Index5 = Key5.index(Letter5)
    Plain_Text5 += Chars5[Index5]

print()
print(f"Encrypted Message : {Cipher_Text5}")
print(f"Original Message : {Plain_Text5}")
