# --- Część 1: Wczytanie N i wygenerowanie listy. ---
N = input('Podaj liczbę: ')

wzorRange = (1 + int(N) * 3)
print(wzorRange)
myRange = range(1, int(wzorRange), 3)

lst = list(myRange)
print(lst)



# --- Część 2: Definicja predykatów. ---
def pierwszyPredykat(liczba):
    return liczba < 5

def drugiPredykat(liczba):
    return liczba % 2 == 0

def trzeciPredykat(liczba):
    return liczba >= 10

def czwartyPredykat(liczba):
    return int(liczba ** 0.5) ** 2 == liczba
      
# --- testowanie predykatu na przykładowej liczbie ---
print(pierwszyPredykat(3))



# --- Część 3: Pierwsza część zadania - utworzenie i wydrukowanie listy liczb z lst, dla których dany predykat zwraca True. ---
pasujaceLiczby = []
for i in lst:
      if pierwszyPredykat(i):
            pasujaceLiczby.append(i)
    
print(pasujaceLiczby)



# --- Część 4: Druga część zadania - utworzenie funkcji przyjmującej listę i predykat, a zwracająca listę elementów wejściowej listy spełniających dany predykat. ---
def funkcjaFiltrowanieListy(lista, predykat):
      wynik = []
      for i in lista:
           if predykat(i):
                wynik.append(i)

      return wynik



# --- Część 5: Testowanie uniwersalnej funkcji na różnych predykatach ---
print(funkcjaFiltrowanieListy(lst, pierwszyPredykat))
print(funkcjaFiltrowanieListy(lst, drugiPredykat))
print(funkcjaFiltrowanieListy(lst, trzeciPredykat))
print(funkcjaFiltrowanieListy(lst, czwartyPredykat))