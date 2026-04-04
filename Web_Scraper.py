import requests
from bs4 import BeautifulSoup
import urllib3

# 1. PRZYGOTOWANIA
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "http://quotes.toscrape.com"
naglowki = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

try:
    # 2. WYSYŁKA (Tutaj powstaje zmienna 'odpowiedz')
    odpowiedz = requests.get(url, headers=naglowki, timeout=10, verify=False)

    # 3. SPRAWDZENIE I WYCIĄGANIE DANYCH
    if odpowiedz.status_code == 200:
        soup = BeautifulSoup(odpowiedz.text, 'html.parser')

        # Pobieramy główny tytuł strony (h1)
        tytul = soup.find('h1').text.strip()
        print(f"Hura! Weszłam na stronę: {tytul}\n")

        # SZUKAMY CYTATÓW (span z klasą 'text')
        cytaty = soup.find_all('span', class_='text')

        print("--- LISTA POBRANYCH CYTATÓW ---")
        for i, cytat in enumerate(cytaty, 1):
            print(f"{i}. {cytat.text}")

    else:
        print(f"Błąd {odpowiedz.status_code}. Serwer nas nie polubił.")

except Exception as e:
    print(f"Błąd techniczny (brak internetu lub SSL): {e}")