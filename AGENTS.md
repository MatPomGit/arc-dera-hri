# Zasady pracy: ARC-DERA-HRI

## Submission-first editorial directive (2026-11-07)

Follow [RESEARCH.md](RESEARCH.md#submission-first-publication-policy-author-directive-2026-11-07): prioritize author-approved submission of a scientifically defensible, completed manuscript over indefinite polishing driven by fear of rejection. An achievable publication even at 20 verified Polish evaluation points is preferable to an unpublished manuscript, but points and acceptance are not guaranteed. Prepare a journal shortlist, requirements, submission package and author decision; after rejection, propose revision and resubmission. Never bypass evidence, ethics, consent, novelty, safety or author-approval gates; do not submit, contact publishers or incur APC without explicit author approval.


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

## Cykl autonomiczny i kryteria ukończenia
- Przy wyborze JUMP, rezerwacji pracy, użyciu skilli, testach exact-SHA, przeglądzie i sprzątaniu czytaj [procedurę agentów](docs/development/agent-workflow.md).
- Obowiązujące zasady metodologiczne, brak zwalidowanego instrumentu, niezmienne identyfikatory pozycji i zakaz nieuprawnionych badań pozostają nadrzędne wobec ogólnych wzorców.
- Przed integracją sprawdź aktualne Issues, wymagane CI/review i osobno publikację MkDocs. Nie traktuj `COMMENT` jako formalnego zatwierdzenia GitHub.
