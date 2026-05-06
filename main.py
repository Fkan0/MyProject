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
        print("ASAL SAYI KONTROLCÜSÜ")

        while True:
            code1 = input("")

            #kullanıc anasayfaya dönmek istiyorsa
            if code1 == "quit": 
                break

            #Kullanıcı yardım istiyorsa        
            elif code1 == "help" or code1 == "yardım":
                controller.help()
                continue
            
            #Kullanıcı Sayının asal olup olmadığını kontrol etmek istiyorsa
            else:

                #Kullanıcının tam sayı girip girmediği kontrol edilir
                try:
                    number = int(code1)
            
                except:
                    print("Lütfen sadece TAM SAYI girin.")
                    continue

                #Herşey yolunda giderse        
                print(my_math.primecontroller(number))
                continue


#ASAL SAYI SIRALAMA SAYFASI
    if maincode == "asal sayıcı":
        print("ASAL SAYI SIRALAMA SAYFASI")

        while True:
            code1 = input("")

            #kullanıc anasayfaya dönmek istiyorsa
            if code1 == "quit": 
                break

            #Kullanıcı yardım istiyorsa        
            elif code1 == "help" or code1 == "yardım":
                controller.help()
                continue
            
            #Kullanıcı Sayının asal olup olmadığını kontrol etmek istiyorsa
            else:

                #Kullanıcının tam sayı girip girmediği kontrol edilir
                try:
                    number = int(code1)
            
                except:
                    print("Lütfen sadece TAM SAYI girin.")
                    continue

                #Herşey yolunda giderse        
                print(my_math.primenumber(number))
                continue 


#ASAL BÖLENLERİ BULMA SAYFASI
    if maincode == "asal bölen":
        print("ASAL BÖLENLERİ BULMA SAYFASI")

        while True:
            code1 = input("")

            #kullanıc anasayfaya dönmek istiyorsa
            if code1 == "quit": 
                break

            #Kullanıcı yardım istiyorsa        
            elif code1 == "help" or code1 == "yardım":
                controller.help()
                continue
            
            #Kullanıcı Sayının asal olup olmadığını kontrol etmek istiyorsa
            else:

                #Kullanıcının tam sayı girip girmediği kontrol edilir
                try:
                    number = int(code1)
            
                except:
                    print("Lütfen sadece TAM SAYI girin.")
                    continue

                #Herşey yolunda giderse        
                print(my_math.primedivisors(number))
                continue


#BÖLEN BULMA SAYFASI
    if maincode == "bölen":
        print("BÖLEN BULMA SAYFASI")

        while True:
            code1 = input("")

            #kullanıc anasayfaya dönmek istiyorsa
            if code1 == "quit": 
                break

            #Kullanıcı yardım istiyorsa        
            elif code1 == "help" or code1 == "yardım":
                controller.help()
                continue
            
            #Kullanıcı Sayının asal olup olmadığını kontrol etmek istiyorsa
            else:

                #Kullanıcının tam sayı girip girmediği kontrol edilir
                try:
                    number = int(code1)
            
                except:
                    print("Lütfen sadece TAM SAYI girin.")
                    continue

                #Herşey yolunda giderse        
                print(my_math
                      .numberdivisors(number))
                continue


#OBEB BULMA SAYFASI
    if maincode == "obeb":
        print("OBEB BULMA SAYFASI")

        while True:
            code1 = input("")

            #kullanıc anasayfaya dönmek istiyorsa
            if code1 == "quit": 
                break

            #Kullanıcı yardım istiyorsa        
            elif code1 == "help" or code1 == "yardım":
                controller.help()
                continue
            
            #Kullanıcı Sayının asal olup olmadığını kontrol etmek istiyorsa
            else:
                code2 = input("")

                #Kullanıcının tam sayı girip girmediği kontrol edilir
                try:
                    number1 = int(code1)
                    number2 = int(code2)
            
                except:
                    print("Lütfen sadece TAM SAYI girin.")
                    continue

                #Herşey yolunda giderse        
                print(my_math
                      .obeb(number1, number2))
                continue


#OKEK BULMA SAYFASI
    if maincode == "okek":
        print("OKEK BULMA SAYFASI")

        while True:
            code1 = input("")

            #kullanıc anasayfaya dönmek istiyorsa
            if code1 == "quit": 
                break

            #Kullanıcı yardım istiyorsa        
            elif code1 == "help" or code1 == "yardım":
                controller.help()
                continue
            
            #Kullanıcı Sayının asal olup olmadığını kontrol etmek istiyorsa
            else:
                code2 = input("")

                #Kullanıcının tam sayı girip girmediği kontrol edilir
                try:
                    number1 = int(code1)
                    number2 = int(code2)
            
                except:
                    print("Lütfen sadece TAM SAYI girin.")
                    continue

                #Herşey yolunda giderse        
                print(my_math.okek(number1, number2))
                continue  


#FİBONACCİSAYFASI
    if maincode == "fibonacci":
        print("BÖLEN BULMA SAYFASI")

        while True:
            code1 = input("")

            #kullanıc anasayfaya dönmek istiyorsa
            if code1 == "quit": 
                break

            #Kullanıcı yardım istiyorsa        
            elif code1 == "help" or code1 == "yardım":
                controller.help()
                continue
            
            #Kullanıcı Sayının asal olup olmadığını kontrol etmek istiyorsa
            else:

                #Kullanıcının tam sayı girip girmediği kontrol edilir
                try:
                    number = int(code1)
            
                except:
                    print("Lütfen sadece TAM SAYI girin.")
                    continue

                #Herşey yolunda giderse        
                print(my_math.fibonacci(number))
                continue


#Help komutu çalıştırılırsa
    if maincode == "help" or maincode == "yardım":
        controller.help()

#Çıkış yapılmak istenirse
    if maincode == "quit":
        print("BAŞARIYLA ÇIKIŞ YAPILDI")
        break

