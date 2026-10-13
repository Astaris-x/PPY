# --- !Nie mój pisany kod. Jedynie komentarze są mojego autorstwa. Nie mam treści poleceń zadań z 1 zjazdu. ---

# --- Część 1: Inicjalizacja pustej listy na liczby podane przez użytkownika. ---
a = []

# --- Część 2: Pętla zbierająca liczby, aż użytkownik wpisze "stop". [Poprawione przeze mnie] ---
while True:
    x = input("Podaj liczbe: ")
    if x == "stop":
        break
    a.append(int(x))

# --- Część 3: Sprawdzanie, czy użytkownik cokolwiek wpisał (czy lista nie jest pusta). [Poprawione przeze mnie] ---
if len(a) > 0:
    najwieksza = a[0]
    najmniejsza = a[0]

# --- Część 4: Szukanie minimum i maximum w liście. ---
    for z in a:
        if z < najmniejsza:
            najmniejsza = z
        elif z > najwieksza:
            najwieksza = z

# --- Część 5: Wydrukowanie wyników. ---
    print("Twoja lista liczb: ", a)
    print("Najmniejsza liczba to: ", najmniejsza)
    print("Największa liczba to: ", najwieksza)
else:
    print("Nie podano żadnych liczb.")