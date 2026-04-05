import sqlite3

polaczenie = sqlite3.connect('moja_biblioteka.db')
kursor = polaczenie.cursor()

# Pobieramy wszystko z tabeli 'cytaty'
kursor.execute('SELECT * FROM cytaty')

# 'fetchall' to polecenie: "przynieś mi wszystkie wyniki, które znalazłeś"
wszystkie_cytaty = kursor.fetchall()

print("--- ZAWARTOŚĆ TWOJEJ BAZY ---")
for wiersz in wszystkie_cytaty:
    print(f"ID: {wiersz[0]} | Autor: {wiersz[2]} | Treść: {wiersz[1]}")

polaczenie.close()