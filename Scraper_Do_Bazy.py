import requests
from bs4 import BeautifulSoup
import sqlite3
import urllib3

# 1. WYŁĄCZANIE OSTRZEŻEŃ SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 2. PRZYGOTOWANIE BAZY DANYCH

polaczenie = sqlite3.connect('moja_biblioteka.db')
kursor = polaczenie.cursor()

# Tworzymy tabelę
kursor.execute('''
    CREATE TABLE IF NOT EXISTS cytaty (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tresc TEXT NOT NULL,
        autor TEXT
    )
''')

# 3. POBIERANIE DANYCH
url = "http://quotes.toscrape.com"
naglowki = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

try:
    odpowiedz = requests.get(url, headers=naglowki, timeout=10, verify=False)

    if odpowiedz.status_code == 200:
        soup = BeautifulSoup(odpowiedz.text, 'html.parser')
        bloki_cytatow = soup.find_all('div', class_='quote')

        # --- ETAP A: ZAPISYWANIE (PĘTLA) ---
        print("--- KROK 1: Zapisywanie nowych danych do bazy ---")
        for blok in bloki_cytatow:
            tekst = blok.find('span', class_='text').text
            autor = blok.find('small', class_='author').text

            # Tu wrzucamy dane do bazy
            kursor.execute("INSERT INTO cytaty (tresc, autor) VALUES (?, ?)", (tekst, autor))
            print(f"Pobrano i zapisano cytat autora: {autor}")

        # Bardzo ważne: Zatwierdzamy wszystkie wrzutki naraz!
        polaczenie.commit()
        print("\nZapisywanie zakończone sukcesem.")

        # --- ETAP B: WYŚWIETLANIE (RAPORT) ---
        # Teraz, gdy baza jest już pełna, robimy JEDNO zapytanie o konkretnego autora
        print("\n--- KROK 2: Szukanie w bazie: Winston Churchill ---")
        kursor.execute("SELECT * FROM cytaty WHERE autor = 'Winston Churchill'")
        wyniki = kursor.fetchall()

        if wyniki:
            for wiersz in wyniki:
                print(f"ID: {wiersz[0]} | Treść: {wiersz[1]}")
        else:
            print("W bazie nie ma jeszcze cytatów tego autora.")

    else:
        print(f"Błąd połączenia ze stroną: {odpowiedz.status_code}")

except Exception as e:
    print(f"Wystąpił błąd techniczny: {e}")

finally:
    # Zawsze zamykamy warsztat na koniec
    polaczenie.close()
    print("\nPołączenie z bazą zamknięte.")