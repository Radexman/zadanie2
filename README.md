# 📊 Raport Ocen Klasy – w kontenerze Dockera! 🐳

Hej! 👋 To mały projekt, w którym program w Pythonie 🐍 **czyta oceny uczniów z pliku**, **liczy średnie** i **robi z tego ładny raport** – a wszystko to działa w **kontenerze Dockera**.

---

## 🤔 Co ten program robi?

1. 📥 Wczytuje oceny z pliku `data/oceny.csv`
2. 🧮 Liczy średnią każdego ucznia
3. 🏆 Sortuje uczniów od najlepszej średniej
4. 🖨️ Wypisuje tabelkę na ekranie
5. 💾 Zapisuje raport do pliku `out/raport.txt`

Przykładowy wynik:

```
RAPORT OCEN KLASY

+--------+--------------+---------------+-------------+----------+-----------+
| imie   |   matematyka |   informatyka |   angielski |   fizyka |   średnia |
+========+==============+===============+=============+==========+===========+
| Ewa    |            5 |             5 |           6 |        5 |      5.25 |
+--------+--------------+---------------+-------------+----------+-----------+
| Ania   |            5 |             6 |           4 |        5 |      5    |
+--------+--------------+---------------+-------------+----------+-----------+
...

Najlepsza średnia: Ewa (5.25)
```

---

## 🐳 Czym jest Docker i po co nam on?

Wyobraź sobie **pudełko na drugie śniadanie** 🍱. Wkładasz do niego wszystko, czego potrzebujesz – i możesz je zabrać gdziekolwiek, a w środku zawsze jest to samo.

**Kontener** działa podobnie: pakujemy do niego Pythona, potrzebne biblioteki i nasz program. Dzięki temu program zadziała **tak samo na każdym komputerze** – nie trzeba nic instalować ręcznie! ✨

---

## 📁 Co jest w projekcie?

| Plik / folder | Do czego służy |
|---|---|
| 🐍 `app.py` | Nasz program w Pythonie |
| 📋 `requirements.txt` | Lista bibliotek, których potrzebuje program (tu: `tabulate` do rysowania tabelek) |
| 🐳 `Dockerfile` | „Przepis” na zbudowanie obrazu kontenera |
| 🎛️ `docker-compose.yaml` | Ustawienia uruchamiania – które foldery podłączyć do kontenera |
| 🙈 `.dockerignore` | Pliki, których Docker ma **nie** wrzucać do obrazu |
| 📂 `data/` | Tu leży plik z ocenami `oceny.csv` |
| 📂 `out/` | Tu pojawi się gotowy raport `raport.txt` |

---

## 🛠️ Czego potrzebujesz?

- ✅ Zainstalowany **Docker Desktop** 👉 https://www.docker.com/products/docker-desktop/
- ✅ Docker Desktop musi być **włączony** (wieloryb 🐳 na pasku zadań)

Sprawdź, czy działa – wpisz w terminalu:

```bash
docker --version
```

Jeśli zobaczysz numer wersji – jest super! 🎉

---

## 🚀 Jak uruchomić projekt?

### Krok 1️⃣ – Otwórz terminal w folderze projektu

W VS Code: menu **Terminal → New Terminal** (albo `Ctrl + ~`).

### Krok 2️⃣ – Zbuduj i uruchom kontener

```bash
docker compose up --build
```

Co tu się dzieje? 🧐
- `build` – Docker czyta `Dockerfile` i buduje obraz (za pierwszym razem może to chwilę potrwać ⏳)
- `up` – uruchamia kontener z naszym programem

### Krok 3️⃣ – Zobacz wynik 👀

- Raport wyświetli się w terminalu 🖥️
- Otwórz plik `out/raport.txt` – tam też jest zapisany! 📄

### Krok 4️⃣ – Posprzątaj po sobie 🧹

```bash
docker compose down
```

---

## 🔗 Jak to działa, że kontener widzi nasze pliki?

W `docker-compose.yaml` są tzw. **volumes** (woluminy) – to takie „tunele” 🚇 między Twoim komputerem a kontenerem:

```yaml
volumes:
    - ./data:/data   # folder data z komputera ➡️ /data w kontenerze
    - ./out:/out     # folder /out z kontenera ➡️ out na komputerze
```

Dzięki temu:
- 📥 kontener **czyta** oceny z Twojego folderu `data/`
- 📤 kontener **zapisuje** raport do Twojego folderu `out/`

A **zmienne środowiskowe** (`environment`) mówią programowi, gdzie ma szukać tych plików 🗺️

---

## 🎮 Wyzwania dla Ciebie!

Spróbuj sam(a):

1. ✏️ **Dopisz siebie** do pliku `data/oceny.csv` i uruchom program ponownie. Jesteś na podium? 🥇
2. ➕ **Dodaj nowy przedmiot** (np. `historia`) jako kolejną kolumnę w CSV. Czy program sam go policzy? 🤯
3. 🧪 Zmień oceny tak, żeby ktoś inny miał najlepszą średnią.
4. 🌟 **Dla ambitnych:** dopisz w `app.py` linijkę, która pokaże **najgorszą** średnią. Pamiętaj, żeby potem uruchomić `docker compose up --build` – bez `--build` kontener nie zobaczy zmian w kodzie! 😉

> 💡 **Ciekawostka:** zmiany w `oceny.csv` widać od razu (dzięki woluminom), ale zmiany w `app.py` wymagają przebudowania obrazu, bo kod jest **kopiowany** do środka obrazu w `Dockerfile`.

---

## 🆘 Coś nie działa?

| Problem 😵 | Rozwiązanie 💡 |
|---|---|
| `docker: command not found` | Zainstaluj Docker Desktop i uruchom terminal od nowa |
| `Cannot connect to the Docker daemon` | Włącz Docker Desktop i poczekaj, aż wystartuje 🐳 |
| `FileNotFoundError: /data/oceny.csv` | Upewnij się, że jesteś w folderze projektu i plik `data/oceny.csv` istnieje |
| `ValueError: invalid literal for int()` | W CSV jest coś, co nie jest liczbą (np. pusta komórka albo litera) – popraw to ✏️ |
| Zmieniłem kod, a nic się nie zmienia 🤔 | Uruchom z `--build`: `docker compose up --build` |

---

Powodzenia i miłego kodowania! 🚀💙
