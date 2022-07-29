#!/bin/avr/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet ANEMON")

print("""
            
PORT TARAYICI
      
1) Normal Port Tarama
2) Servis ve Versiyon
3) Isletim Sistemi Tarama
00) Cikis

""")

islemno = input("İslem Numarasi Giriniz: ")
if islemno=="1":
    hedefip=input("Hedef Ip Giriniz: ")
    os.system("nmap" + hedefip)
elif islemno=="2":
    hedefip = input("Hedef Ip Giriniz: ")
    os.system("nmap -sS -sV" + hedefip)
elif islemno=="3":
    hedefip = input("Hedef Ip Giriniz: ")
    os.system("nmap -O " + hedefip)
elif islemno=="00":
    quit()
else :
       print("Hatali İslem Girdiniz.") 