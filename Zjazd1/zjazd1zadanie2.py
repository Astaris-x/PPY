# --- !Nie mój pisany kod. Jedynie komentarze są mojego autorstwa. Nie mam treści poleceń zadań z 1 zjazdu. ---

# --- KALKULATOR BMI ---

# --- Część 1: Pobranie od użytkownika informacji o wzroście oraz wadze. ---
wzrost = float(input("Podaj wzrost w metrach: "))
waga = float(input("Podaj wagę: "))

# --- Część 2: Obliczanie BMI. ---
BMI = waga/(wzrost**2)

if BMI > 18 and BMI < 25:
    print("Twoje BMI jest w normie.")
elif BMI <= 18 or BMI >= 25:
    print("Twoje BMI nie jest w normie.")

# --- Część 3: Wydrukowanie wyników. ---
print("BMI = ", BMI)