import csv
import os
from tabulate import tabulate

# Ścieżki: lokalnie domyślne, w kontenerze podmienione przez docker-compose
CSV_PATH = os.environ.get("CSV_PATH", "data/oceny.csv")
OUT_DIR = os.environ.get("OUT_DIR", "out")

# 1. Wczytanie danych
with open(CSV_PATH, encoding="utf-8") as f:
    uczniowie = list(csv.DictReader(f))

# 2. Liczenie średnich
tabela = []
for uczen in uczniowie:
    oceny = [int(v) for k, v in uczen.items() if k != "imie"]
    srednia = round(sum(oceny) / len(oceny), 2)
    tabela.append([uczen["imie"], *oceny, srednia])

# 3. Sortowanie od najlepszej średniej
tabela.sort(key=lambda w: w[-1], reverse=True)

# 4. Budowa raportu
naglowki = list(uczniowie[0].keys()) + ["średnia"]
raport = "RAPORT OCEN KLASY\n\n"
raport += tabulate(tabela, headers=naglowki, tablefmt="grid")
raport += f"\n\nNajlepsza średnia: {tabela[0][0]} ({tabela[0][-1]})\n"

print(raport)

# 5. Zapis do pliku
os.makedirs(OUT_DIR, exist_ok=True)
with open(os.path.join(OUT_DIR, "raport.txt"), "w", encoding="utf-8") as f:
    f.write(raport)

print("Zapisano raport do:", OUT_DIR)
