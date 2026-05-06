#Asal sayı kontrol eden fonksiyon.
def primecontroller(number):

    if number < 2: #Girilen sayı 2 den küçükse.
        return False #Girilen sayı asal sayı değil ise.
    
    for i in range(2, int(number ** 0.5) + 1): #Girilen sayı 2 den büyükse.
        if number % i == 0: 
            return False #Girilen sayı asal sayı değil ise.
        
    return True #Girilen sayı asal sayı ise.

#Girilen sayıya kadar asal sayıları yazan fonksiyon.
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