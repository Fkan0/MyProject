import controller 
import my_math 


#Uygulama hazırlık mesajları
print("MyProject uygulamasına giriş yaptınız.")
print("Yardım almak için 'help' veya 'yardım' yazın")


#ANA SAYFA
while True:
    print("ANASAYFA")
    maincode = input("")


#ASAL SAYI KONTROLCÜ SAYFASI
    if maincode == "asal kontrolcü":
        controller.page1(my_math.primecontroller, "ASAL SAYI KONTROLCÜSÜ")


#ASAL SAYI SIRALAMA SAYFASI
    elif maincode == "asal sayıcı":
        controller.page1(my_math.primenumber, "ASAL SAYI SIRALAMA SAYFASI")


#ASAL BÖLENLERİ BULMA SAYFASI
    elif maincode == "asal bölen":
        controller.page1(my_math.primedivisors, "ASAL BÖLENLERİ BULMA SAYFASI")


#BÖLEN BULMA SAYFASI
    elif maincode == "bölen":
        controller.page1(my_math.numberdivisors, "BÖLEN BULMA SAYFASI")


#OBEB BULMA SAYFASI
    elif maincode == "obeb":
        controller.page2(my_math.obeb, "OBEB BULMA SAYFASI")


#OKEK BULMA SAYFASI
    elif maincode == "okek":
        controller.page2(my_math.okek, "OKEK BULMA SAYFASI")


#FİBONACCİSAYFASI
    elif maincode == "fibonacci":
        controller.page1(my_math.fibonacci, "FİBONACCİ SAYFASI")


#Help komutu çalıştırılırsa
    elif maincode == "help" or maincode == "yardım":
        controller.help()


#Çıkış yapılmak istenirse
    elif maincode == "quit":
        print("BAŞARIYLA ÇIKIŞ YAPILDI")
        break

#Bilinmeyen komut girilirse