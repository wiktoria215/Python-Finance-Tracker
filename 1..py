import pandas as pd

dane = {"Produkt": ["Zegarek", "Naszyjnik", "Pierścionek", "Kolczyki"],
    "Sprzedano_sztuk": [5, 12, 8, 15],
    "Cena_za_sztuke": [500, 200, 300, 150]

}

tabela = pd.DataFrame(dane)

print(tabela)

tabela["Przychód"] = tabela["Sprzedano_sztuk"] * tabela["Cena_za_sztuke"]

print("\n--Zaktualizowana tabela--")
print(tabela)

utarg = tabela["Przychód"].sum()
print("\nCałkowity utarg ze sprzedaży wynosi:", utarg, "zł")

import matplotlib.pyplot as plt

# Prosimy o narysowanie wykresu słupkowego
tabela.plot.bar(x="Produkt", y="Przychód", color="skyblue", title="Przychód ze sprzedaży biżuterii")

# Pokazujemy gotowy obrazek na ekranie
plt.show()

