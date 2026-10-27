# Zasady pracy: ARC-DERA-HRI

## Przed zmianą
- Przeczytaj `README.md`, odpowiednie strony `docs/`, `CHANGELOG.md`, otwarte Issues i PR-y.
- **KISS:** jeden cel zmiany, minimalna liczba plików, brak frameworków, modułów i zależności „na zapas”.
- Dokumentacja projektu jest w MkDocs (`mkdocs.yml`, `docs/`). **Nie wymagaj nieistniejących `docs/architecture.md` ani `docs/adr/`**.

## Rygor naukowy
- Rozdzielaj: treść źródła → hipotezę → zatwierdzoną decyzję → badanie → wynik.
- Nie nazywaj skali zwalidowaną, nie zakładaj liczby czynników ani skoringu przed empirycznym uzasadnieniem.
- Kanoniczne banki `instruments/*.csv` mają **niezmienne ID i brzmienia**. Każda korekta pytania to nowa wersja; nie przepisuj historii.
- Nie myl samoopisu z pomiarem fizjologicznym ani korelacji z przyczynowością. Rozdzielaj brak kanału od braku odpowiedzi.
- Nowy dokument źródłowy: zaktualizuj istniejącą właściwą stronę i `docs/sources.md`; nowy plik tylko dla odrębnego celu.

## Kod, testy i dokumentacja
- Python standard library, PEP 8, proste funkcje i tylko wymagane zależności. Bez zbędnej abstrakcji i pustych atrap.
- Utrzymuj podstawowe testy integralności instrumentu; nie maskuj usterek usuwaniem testów.
- Po zmianach dokumentacji zweryfikuj linki i uruchom `python -m mkdocs build --strict`, o ile MkDocs jest dostępny; w innym razie jasno odnotuj brak testu i sprawdź workflow.
- `README.md` = zwięzły punkt wejścia; `docs/` = opis aktualnego stanu; `CHANGELOG.md` = historia; `instruments/` = pełne brzmienia pozycji. Nie dubluj tych treści.
- Żadnych płatnych usług, własnego API, danych osobowych ani nagrań w publicznym repozytorium.

## Zamykanie pracy
- Dla zmian wymagających przeglądu preferuj PR; po scaleniu **usuń gałąź**, zamknij lub uaktualnij Issue, nie zostawiaj martwych PR-ów.
- Małe, atomowe aktualizacje samej dokumentacji mogą trafiać bezpośrednio na `main`, jeśli zapobiega to tworzeniu zbędnych gałęzi.
- Podaj pliki, zakres, wynik rzeczywistych testów, status publikacji Pages i nierozstrzygnięte blokery. Nie ogłaszaj sukcesu publikacji bez potwierdzenia działania strony.
