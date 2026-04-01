# Python Finance Tracker & SQL Database

Prosty system do automatycznego pobierania cen akcji i zapisywania ich w lokalnej bazie danych SQLite. 

## Funkcje
- Pobieranie realnych danych giełdowych za pomocą biblioteki `yfinance`.
- Automatyczne tworzenie bazy danych SQL (`sqlite3`).
- Logika zapobiegająca duplikowaniu danych (sprawdzanie ostatniej ceny).
- Rejestracja czasu zapisu (Timestamp) w czasie lokalnym.
- Obliczanie statystyk (średnia cena akcji w portfelu).

## Technologie
- **Python 3.x**
- **SQLite** (Baza danych)
- **yfinance** (API giełdowe)
- **Git** (Kontrola wersji)

## Jak uruchomić projekt?
1. Zainstaluj wymagane biblioteki:
   `pip install yfinance`
2. Uruchom skrypt:
   `python Database_Architect.py`
