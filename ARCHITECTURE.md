# Architektura projektu DERA-HRI

Projekt obejmuje opracowanie i ocenę trafności treściowej kwestionariusza doświadczeń afektywnych po interakcji człowiek–robot. Jedynymi kanonicznymi źródłami pozycji są wersjonowane `instruments/dera_hri_*.csv`. Opisy konstruktu, skoringu i walidacji znajdują się w zatwierdzonych materiałach projektu.

**Granice katalogów:** `instruments/` zawiera bank pozycji oraz puste formularze, `tools/` analizę CVR/CVI, `tests/` kontrolę tożsamości pozycji i obliczeń, `docs/` procedury wewnętrzne i decyzje architektoniczne. Publiczna witryna ma osobne `pages/`, z jawnym dopuszczeniem każdego pliku. Dane uczestników i wypełnione arkusze ekspertów nie są przechowywane w Git.

**Stan:** przygotowanie instrumentu i planów badawczych, bez potwierdzonej struktury czynnikowej, trafności i rzetelności. Istnienie kodu analizy nie oznacza, że wykonano ocenę z udziałem ekspertów ani badań z udziałem osób.

Wszelkie zmiany tekstu pytania wymagają nowej wersji banku, decyzji naukowej i kontroli powiązań CSV/DOCX/MkDocs. [ADR](docs/adr/README.md) dotyczą granic narzędzi i publikacji, nie zastępują metodologii badania. Polityka bezpieczeństwa: [SECURITY.md](SECURITY.md).
