# --- Część 1: Podanie liczby N przez użytkownika. ---
N = int(input("Podaj liczbę N: "))



# --- Część 2: Stworzenie zbioru i listy. ---
unikalneLiczby = set()
wszystkieLiczby = []



# --- Część 3: Podawanie różnych liczb przez użytkownika. ---
while len(unikalneLiczby) < N:
    liczba = int(input("Podaj liczbę: "))

    wszystkieLiczby.append(liczba)

    unikalneLiczby.add(liczba)



# --- Część 4: Drukowanie wyników. ---
print("Unikalne liczby: ", unikalneLiczby)
print("Wszystkie liczby: ", wszystkieLiczby)



# --- Część 5: Szukanie liczb podanych więcej niż raz. ---
powtorzoneLiczby = []
for liczba in unikalneLiczby:
    if wszystkieLiczby.count(liczba) > 1:
        powtorzoneLiczby.append(liczba)

print("Liczby podane więcej niż raz: ", powtorzoneLiczby)



