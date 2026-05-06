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
    

#Tek parametreli sayfa düzeni
def page1(function, page_name):

    print(page_name)
    while True:
        code = input("")

        if code in ["quit", "çıkış"]:
            break

        elif code in ["help", "yardım"]:
            help()
            continue
        
        else:
            try:
                number = int(code)

            except:
                print("Sadece TAM SAYI giriniz")
                continue
            
            print(function(number))


#Çift parametreli sayfa düzeni
def page2(function, page_name):

    print(page_name)
    while True:
        code1 = input("")

        if code1 in ["quit", "çıkış"]:
            break

        elif code1 in ["help", "yardım"]:
            help()
            continue
        
        else:
            
            code2 = input("")
            try:
                number1 = int(code1)
                number2 = int(code2)

            except:
                print("Sadece TAM SAYI giriniz")
                continue
            
            print(function(number1, number2))
