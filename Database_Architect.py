import sqlite3
import yfinance as yf

# 1. Połączenie
polaczenie = sqlite3.connect('moje_finanse.db')
kursor = polaczenie.cursor()

# 2. Tabela - Dodajemy kolumnę data_zapisu (Zwróć uwagę na TIMESTAMP)
# Jeśli chcesz zobaczyć tę kolumnę, usuń najpierw stary plik moje_finanse.db!
kursor.execute('''
CREATE TABLE IF NOT EXISTS portfel (
    symbol TEXT, 
    cena REAL, 
    data_zapisu TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# --- KROK A: PORZĄDKI ---
akcja_do_skasowania = 'TSLA'
kursor.execute("DELETE FROM portfel WHERE symbol = ?", (akcja_do_skasowania,))
polaczenie.commit()

# --- KROK B: NOWY ZAPIS ---
akcja_do_sprawdzenia = 'MSFT'
ticker = yf.Ticker(akcja_do_sprawdzenia)
aktualna_cena = ticker.history(period='1d')['Close'].iloc[-1]

kursor.execute("SELECT cena FROM portfel WHERE symbol = ? ORDER BY rowid DESC LIMIT 1", (akcja_do_sprawdzenia,))
ostatni_wynik = kursor.fetchone()

if ostatni_wynik is not None and ostatni_wynik[0] == aktualna_cena:
    print(f"Pominięto: Cena {akcja_do_sprawdzenia} się nie zmieniła ({aktualna_cena:.2f})")
else:
    # Wkładamy tylko symbol i cenę, data_zapisu doda się SAMA dzięki DEFAULT
    kursor.execute("INSERT INTO portfel (symbol, cena) VALUES (?, ?)", (akcja_do_sprawdzenia, aktualna_cena))
    polaczenie.commit()
    print(f"Nowy wpis: {akcja_do_sprawdzenia} zapisano w cenie {aktualna_cena:.2f}")

# --- KROK C: STATYSTYKI ---
kursor.execute("SELECT AVG(cena) FROM portfel")
wynik_srednia = kursor.fetchone()[0]

if wynik_srednia:
    print(f"Średnia wartość wszystkich akcji w bazie: {wynik_srednia:.2f} PLN")

# --- KROK D: WYŚWIETLANIE (Z DATĄ!) ---
kursor.execute("SELECT symbol, cena, data_zapisu FROM portfel")
print("\n--- Pełna historia Twoich zapisów ---")
for wiersz in kursor.fetchall():
    # wiersz[0] = symbol, wiersz[1] = cena, wiersz[2] = data
    print(f"[{wiersz[2]}] Spółka: {wiersz[0]} | Cena: {wiersz[1]:.2f}")

polaczenie.close()