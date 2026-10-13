# --- Część 1: Utworzenie listy imion. ---
imiona = ["John", "Mary", "Kitty", "Alice", "John", "Mary", "Al", "Bill", "John", "Alice", "Al"]
print(imiona)



# --- Część 2: Pierwsza część zadania - utworzenie listy długości imion. ---
dlugosc = []
for i in imiona:
    dlugosc.append(len(i))

print(dlugosc)



# --- Część 3: Druga część zadania - utworzenie słownika, gdzie kluczami są długości imion, a wartościami listy imion o tej długości. ---
slownikImiona = {}

for i in imiona:
    dlugosc = len(i)

    if dlugosc not in slownikImiona:
        slownikImiona[dlugosc] = []

    slownikImiona[dlugosc].append(i)

print(slownikImiona)



# --- Część 4: Trzecia część zadania - utworzenie słownika, gdzie kluczami są długości imion, a wartościami zbiory imion o tej długości. ---
slownikZbiory = {}

for i in imiona:
    dlugosc = len(i)

    if dlugosc not in slownikZbiory:
        slownikZbiory[dlugosc] = set()

    slownikZbiory[dlugosc].add(i)

print(slownikZbiory)



# --- Część 5: Czwarta część zadania - utworzenie słownika, gdzie kluczami są imiona, a wartościami liczby wystąpień danego imienia. ---
slownikWystapienia = {}

for i in imiona:
    if i not in slownikWystapienia:
        slownikWystapienia[i] = 0

    slownikWystapienia[i] += 1

print(slownikWystapienia)