#Asal sayı kontrol eden fonksiyon.
def primecontroller(number):

    if number < 2: #Girilen sayı 2 den küçükse.
        return False #Girilen sayı asal sayı değil ise.
    
    for i in range(2, int(number ** 0.5) + 1): #Girilen sayı 2 den büyükse.
        if number % i == 0: 
            return False #Girilen sayı asal sayı değil ise.
        
    return True #Girilen sayı asal sayı ise.