#Asal sayı kontrol eden fonksiyon.
def primecontroller(number):

    if number < 2: #Girilen sayı 2 den küçükse.
        return False #Girilen sayı asal sayı değil ise.
    
    for i in range(2, int(number ** 0.5) + 1): #Girilen sayı 2 den büyükse.
        if number % i == 0: 
            return False #Girilen sayı asal sayı değil ise.
        
    return True #Girilen sayı asal sayı ise.

#Girilen sayıya kadar asal sayıları liste halinde yazan fonksiyon.
def primenumber(number):
    primelist = [] #Asal sayılar listesi.
    number = int(number) #Sayı integere çevrilir.

#Sayı 2 den büyük ya da eşitse.
    if number >= 2:

        for i in range (2, number + 1): #Asal olmasu beklenen sayı.
            prime = True

            for j in range (2, int(i ** 0.5) + 1): #Bölen sayısı.
                if i % j == 0:
                    prime = False
                    break

#Eğer i asal sayı ise listeye eklenir
            if prime == True:
                primelist.append(i)

#Return olarak asal sayı listesinde dönüş yapar
    return primelist

#Sayının asal bölenlerini liste halinde geri veren fonksiyon.
def primedivisors(number):
    divisors = []
    variable_number = number

    for i in primenumber(number):

        while True:
            if variable_number % i == 0:
                variable_number /= i
                divisors.append(i)

            else:
                break 

    return divisors

#Sayının tüm bölenlerini liste halinde tersten geri veren fonksiyon.
def numberdivisors(number):
    divisors = []

    for x in range(number + 1, 1, -1):
        if number % x == 0:
            divisors.append(x)

    return divisors

#İki sayının obeb'ini hesaplayan fonksiyon
def obeb(number1, number2):

    for x in numberdivisors(number1):

        for y in numberdivisors(number2):

            if x == y:

                return x
            
#İki sayının okek'ini hesaplayan fonksiyon.
def okek(number1, number2):

    return (number1 * number2) // obeb(number1, number2)

#Belirtilen sayıda fibonacci serisi elemanını liste halinde verir.
def fibonacci(number):
    fibonacci_list = [1,1]
    index = 0

    while number > len(fibonacci_list):
        new_number = fibonacci_list[index] + fibonacci_list[index + 1]
        fibonacci_list.append(new_number)
        index += 1
    
    return fibonacci_list

#Verilen sayının tam sayı olup olmadığını kotrol eden foksiyon.
def intcontroller(number):
    try:
        int(number)
        return True
    except (ValueError, TypeError):
        return False     

#Yardım Fonksiyonu 
def help():
    print("""
          KOMUT LİSTESİ
          
          SADECE ANA UYGULAMADA ÇALIŞIR
          
          'asal kontrolcü' : Asal sayı kontrol uygulamasına yönlendirir. 
          'asal sayıcı' : Asal sayıcı uygulamasına yönlendirir.
          'asal bölen' : Asal bölen uygulamasına yönlendirir.
          'bölen' : bölen uygulamasına yönlendirir.
          'obeb' : obeb uygulamasına yönlendirir.
          'okek' : okek uygulamasına yönlendirir.
          'fibonacci' : fibonacci uygulamasına yönlendirir.

          HER DURUMDA ÇALIŞIR

          'help' : komutları listeler açar.
          'yardım' : komutları listeler.
          'quit' : sayfadam çıkış yapar.
""")
    
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
                help()
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
                print(primecontroller(number))
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
                help()
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
                print(primenumber(number))
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
                help()
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
                print(primedivisors(number))
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
                help()
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
                print(numberdivisors(number))
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
                help()
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
                print(obeb(number1, number2))
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
                help()
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
                print(okek(number1, number2))
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
                help()
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
                print(fibonacci(number))
                continue