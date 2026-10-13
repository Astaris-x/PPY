# --- !Nie mój pisany kod. Jedynie komentarze są mojego autorstwa. Nie mam treści poleceń zadań z 1 zjazdu. ---

# ==========================================
# Palindrom sprawdzany z listy elementów (wpisywanych po kolei)
# ==========================================

# --- Część 1: Inicjalizacja pustej listy na dane od użytkownika. ---
a = []

# --- Część 2: Pętla zbierająca elementy, dopóki użytkownik nie wpisze "stop". ---
while True:
    x = input("Podaj znak lub liczbe: ")
    if x == 'stop': 
        break
    a.append(x)

    print("Aktualna lista: ", a)

# --- Zmienna pomocnicza do oznaczania, czy lista jest symetryczna. ---
czyPalindrom = True

# --- Część 3: Sprawdzanie symetrii listy (czy od tyłu jest taka sama jak od przodu). [Poprawione przeze mnie.]---
for i in range(len(a)):
    if a[i] != a[-(i + 1)]:
        czyPalindrom = False
        break

# --- Część 4: Drukowanie wyniku. ---
if czyPalindrom:
    print("To jest palindrom.")
else:
    print("To nie jest palindrom.")


# ==========================================
# BONUS - Palindrom sprawdzany jako słowo.
# ==========================================

# --- Część 1: Pobranie od użytkownika jednego słowa do sprawdzenia. ---
slowo = input("Podaj słowo do sprawdzenia: ")

# --- Część 2: Sprawdzanie symetrii słowa. ---
if slowo == slowo[::-1]:
    print(f"Słowo '{slowo}' jest palindromem.")
else:
    print(f"Słowo '{slowo}' nie jest palindromem.")