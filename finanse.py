import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
data = yf.download("TSLA", period="6mo")
print(data.head())
data['average_30'] = data['Close'].rolling(30).mean()
print(data.tail())

# --- WIZUALIZACJA ---
plt.figure(figsize=(12, 6))


plt.plot(data.index, data['Close'], label='Cena zamknięcia (TSLA)', color='#ff7900', linewidth=2)


plt.plot(data.index, data['average_30'], label='Średnia 30-dniowa', color='blue', linestyle='--')


plt.title('Analiza akcji Tesli (TSLA) - Ostatnie 6 miesięcy', fontsize=14)
plt.xlabel('Data')
plt.ylabel('Cena w USD')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)


plt.savefig('analiza_TSLA.png')
print("Wykres został zapisany jako analiza_TSLA.png")


plt.show()

# --- EKSPORT DANYCH ---

data.to_csv('wyniki_tesla.csv')
print("Dane zostały zapisane do pliku wyniki_tesla.csv")