import random
from bigprimesgenerator import *


def wyznacz_e(Ø):
    e = 2
    warunek = Ø % e
    while warunek != 1:
        warunek = Ø % e
        e = e + 1
    return e - 1

def wyz_d(a, m):
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def text_na_liczby(tekst_jawny):
    txt2num = []
    for i in tekst_jawny:
        txt2num.append(str(slownik.index(i)))
    return int("".join(txt2num))

def liczby_na_tekst(szyfr, litery):
    text = ""
    for x,y in (str(szyfr)[i:i+2] for i in range(0,len(str(szyfr)),2)):
        numer = int(x+y)
        text = text + litery[numer]
    return text

slownik = [None,None,None,None,None,None,None,None,None,None,
           '0','1','2','3','4','5','6','7','8','9',
           'a','b','c','d','e','f','g','h','i','j',
           'k','l','m','n','o','p','q','r','s','t',
           'u','v','w','x','y','z','A','B','C','D',
           'E','F','G','H','I','J','K','L','M','N',
           'O','P','Q','R','S','T','U','V','W','X','Y','Z',
           '!','"','%','&',"'",'(',')','*','+',',','-','.',
           '/',':',';','<','=','>','?','@','[',']','_','{',
           '|','}',' ']


########MENU########

while True:
    print("")
    print("Witaj w maszynie szyfrowej z algorytmem RSA")
    print("Co chcesz zrobic?")
    print("1 - Generuj nowe klucze")
    print("2 - Zakoduj wiadomosc")
    print("3 - Odkoduj wiadomosc")
    print("4 - Zakoncz")
    print("")
    wybor = input("Wybieram: ")
    if wybor not in ("1", "2", "3", "4"):
        continue

    elif wybor == "1":
        p,q = 2,2
        bitKeylen = int(input("Podaj dlugosc klucza w bitach: ")) // 2
        print("Trwa generowanie liczb pierwszych...")
        while p == q:
            p = generuj_prime(bitKeylen)
            q = generuj_prime(bitKeylen)
        Ø = (p - 1) * (q - 1)
        n = p * q
        e = wyznacz_e(Ø)
        d = wyz_d(e, Ø)
        print("")
        print("########### Zakonczono analize liczb pierwszych ############")
        print("")
        print("################  Trwa generowanie kluczy  #################")
        print("")
        print("Twoj klucz publiczny e:")
        print(str(e))
        print("")
        print("Twoj klucz publiczny n:")
        print(str(n))
        print("")
        print("Twoj klucz prywatny  d:")
        print(str(d))
        print("")
        print("############################################################")
        print("")
        
    elif wybor == "2":
        publiczne_e = int(input("Podaj klucz publiczny e: "))
        publiczne_n = int(input("Podaj klucz publiczny n: "))
        limit = len(str(publiczne_n))//2
        kodowanie = True
        print("Limit dla tajnej wiadomosci wynosi " + str(limit) + " znakow")
        print("Dozwolone znaki to: " + "".join(slownik[10::]))
        
        wiadomosc = input("Podaj wiadomosc do zakodowania:  ")
        
        if len(wiadomosc) > limit:
            print("Przekroczono limit wiadomosci")
            continue
        
        elif wiadomosc == '':
            print("Nic nie wpisano")
            continue
        
        for i in wiadomosc:
            if i not in "".join(slownik[10::]):
                print("Err: Wprowadzono nieobslugiwany znak: " + "'" + str(i) + "'")
                kodowanie = False
                continue
        
        while kodowanie == True:
            print("")
            text_to_number = text_na_liczby(wiadomosc)
            zakoduj = pow(text_to_number, publiczne_e, publiczne_n)
            print("Twoja zakodowana wiadomosc:  " + str(zakoduj))
            break

    elif wybor == "3":
        publiczne_n = int(input("Podaj klucz publiczny n: "))
        prywatne_d = int(input("Podaj twoj klucz PRYWATNY d: "))
        zakoduj = int(input("Podaj zaszyfrowana wiadomosc: "))
        odkoduj = pow(zakoduj, prywatne_d, publiczne_n)
        number_to_text = liczby_na_tekst(odkoduj, slownik)
        print("")
        print("Wiadomosc po odkodowaniu:")
        print("")
        print(number_to_text)
        print("")
    
    elif wybor == "4":
        print("Trwa wylogowywanie")
        print("Czyszczenie pamieci")
        p,q,Ø,n,e,d,zakoduj,odkoduj,publiczne_e,publiczne_n,prywatne_d,number_to_text,text_to_number,wiadomosc,limit = None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
        print("Dane zniszczone...bye")
        break

######END_MENU######
