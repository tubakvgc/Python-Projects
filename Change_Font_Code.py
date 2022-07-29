from pyfiglet import Figlet
print("Bir font seçiniz...")
print('''
    1-roman
    2-slant
    3-5lineoblique
    4-acrobatic
    5-alligator
    6-alligator2
    7-banner \n''')
while True :
    devam=input("Devam etmek ister misin ? (y/n) : ")
    if devam=="y":
        secim=int(input("Font Seçiniz :  "))
        if secim==1:
            girdi = input("Bir yazı giriniz : ")
            font = Figlet(font="roman")
            print("")
            print(font.renderText(girdi))
        elif secim==2:
            girdi = input("Bir yazı giriniz : ")
            font = Figlet(font="slant")
            print("")
            print(font.renderText(girdi))
        elif secim==3:
            girdi = input("Bir yazı giriniz : ")
            font = Figlet(font="5lineoblique")
            print("")
            print(font.renderText(girdi))
        elif secim==4:
            girdi = input("Bir yazı giriniz : ")
            font = Figlet(font="acrobatic")
            print("")
            print(font.renderText(girdi))
        elif secim==5:
            girdi = input("Bir yazı giriniz : ")
            font = Figlet(font="alligator")
            print("")
            print(font.renderText(girdi))
        elif secim==6:
            girdi = input("Bir yazı giriniz : ")
            font = Figlet(font="alligator2")
            print("")
            print(font.renderText(girdi))
        elif secim==7:
            girdi = input("Bir yazı giriniz : ")
            font = Figlet(font="banner")
            print("")
            print(font.renderText(girdi))
        else :
            print("Ya o 7 sayıdan birini seç ya da defol!(Şaka şaka gül diye :)")
    elif devam=="n":
        font = Figlet(font="roman")
        print("")
        print(font.renderText("BYE"))
        break
    else :
        print("Lütfen y veya n harflerini giriniz!")