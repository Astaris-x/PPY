# --- !Nie mój pisany kod. Jedynie komentarze są mojego autorstwa. Nie mam treści polecenia zadań z 1 zjazdu. ---

# --- Część 1: Pobranie liczby a od użytkownika oraz sprawdzenie jej typu. ---
a = int(input("Podaj liczbę: "))
print(type(a))

# --- Część 2: Instrukcja warunkowa (if, elif, else). ---
if a < 10:
    print("Małe.")
elif a > 15:
    print("Duże.")
else:
    print("Ni to, ni to.")

# --- Część 3: Potęgowanie liczby a. ---
print(a**78)

# --- Część 4: Pętla while. ---
while a <= 5:
    print(a)
    a += 1

# --- Część 5: Nieskończona pętla (while True) przerywana przez break ---
while True:
    print(a)
    a += 1
    if a > 5:
        break

# --- Część 6: Pętla for iterująca po liście z różnymi typami danych ---
for x in [1, 3.6, "abc"]:
    print(x)

# --- Część 7: Pętla for iterująca po napisach (łańcuchu znaków) ---
for c in "abc":
    print(c)

# --- Część 8: Sprawdzanie typu zmiennej. [Poprawione przeze mnie.] ---
if isinstance(a, str):
    print("str")
else:
    print("coś innego")

# --- Część 9: Sprawdzanie, czy zmienna to liczba całkowita. [Dopisane przeze mnie.] ---
if isinstance(a, int):
    print("To jest liczba całkowita (int).")
else:
    print("To nie jest int.")