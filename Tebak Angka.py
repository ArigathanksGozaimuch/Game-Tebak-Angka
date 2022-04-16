# Library
import random

#Intro
print("\nSaya ingin main permainan tebak angka nih!")
print("Kenalan dulu yuk! Siapa nama kamu?")
nama=input("Namaku adalah: ")
print("\nOk, " + nama + ". Aku akan memberimu 3x kesempatan")
print("Clue untuk kamu, angka yang sudah aku pikirkan ada di antara 0-10")
print("Berapa angkanya?\n")

#menentukan angka acak sesuai ketentuan soal
angka=random.randint(0,10)

#Cheat untuk memperlihatkan jawaban sebagai tes hasil output
print(angka)

#algoritma loop
for jmlTebak in range(1,4):
    print("Tebakanku adalah: ", end="")
    tebakan=int(input())
    print("")
    if tebakan>angka:
        print("Salah, tebakanmu terlalu tinggi!")
        if jmlTebak<3:
            print("Kamu masih punya " + str((jmlTebak-3)*-1) + " Kali kesempatan lagi")
    elif tebakan<angka:
        print("Salah, tebakanmu terlalu rendah!")
        if jmlTebak<3:
            print("Kamu masih punya " + str((jmlTebak-3)*-1) + " Kali kesempatan lagi")
    else:
        break

#output jawaban benar/salah
if jmlTebak==1:
    print("Wow, Langsung Tau! Anda psychic!")
    print("Bravo "+ nama +"! Anda menang dengan sempurna!")
elif tebakan==angka:
    print("Selamat " + nama + "! Kamu berhasil menebak angka dengan " + str(jmlTebak) + " kali tebak!")
    print("Luar biasa! Anda menang!")
else:
    print("Sayang sekali " + nama + ", kesempatanmu sudah habis...")
    print("Anda kalah! Jawaban yang benar adalah " + str(angka))

