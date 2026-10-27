# Zasady pracy: ARC-DERA-HRI

## Start
- Przeczytaj `README.md`, `docs/architecture.md`, `docs/model.md`, `docs/instrument.md`, `docs/validation.md`, `docs/sources.md`.
- Sprawdź `docs/adr/` (obowiązujące decyzje), otwarte Issues i PR-y, zanim zaczniesz pracę.

## Samodzielność
- Działaj samodzielnie: podejmuj rozsądne decyzje, nie pytaj o zgodę na każdą zmianę.
- Przy niejasności wybierz najprostszą sensowną interpretację, zapisz założenie w opisie PR/Issue i kontynuuj.
- Pytaj tylko, gdy decyzja jest nieodwracalna (np. usunięcie danych, przepisanie historii Git) lub zmienia kierunek badawczy projektu.
- Nie zatrzymuj pracy na drobiazgach (nazewnictwo, formatowanie, kolejność sekcji).

## Architektura i ADR
- `docs/architecture.md` to jedyny opis struktury projektu: moduły, przepływ danych, zależności. Maksymalnie jedna strona, bez powielania README.
- Zmiana struktury (nowy moduł, zmiana przepływu, nowa zależność): zaktualizuj `docs/architecture.md` w tym samym PR.
- ADR (Architecture Decision Record) pisz tylko dla istotnych, trudno odwracalnych decyzji technicznych lub metodologicznych (wybór narzędzia, format danych, podejście analityczne). Nie dla drobiazgów.
- Format ADR: `docs/adr/NNNN-krotki-tytul.md`, do 15 linii: Status (zaproponowana / przyjęta / zastąpiona), Kontekst, Decyzja, Konsekwencje.
- Nie edytuj przyjętych ADR. Zmianę decyzji zapisz jako nowy ADR i oznacz stary jako „zastąpiona przez NNNN”.
- Przed większą zmianą sprawdź, czy nie narusza istniejącego ADR.
- Decyzje badawcze (instrument, analiza) zapisuj zgodnie z sekcją „Rygor naukowy”; ADR dotyczy implementacji i struktury.

## Źródła i dokumentacja
- Nowe źródło: porównaj z obecnym stanem i **zaktualizuj istniejącą treść**. Nowy plik tylko dla odrębnego celu.
- Uzupełnij `docs/sources.md` i `CHANGELOG.md`.
- Opisy zwięzłe: konkretnie, bez wstępów, powtórzeń i ozdobników. Jedno miejsce na jedną informację; w pozostałych odsyłaj linkiem.

## KISS
- Nie komplikuj projektu. Najprostsze rozwiązanie, które spełnia cel.
- Brak frameworków, warstw abstrakcji i architektury „na zapas”.
- Nie powielaj opisów, programów, konfiguracji ani dokumentacji.
- Nie dodawaj funkcji, których nikt nie zlecił.

## Struktura repozytorium
- **Zakaz mnożenia plików.** Przed utworzeniem pliku sprawdź, czy treść nie pasuje do istniejącego.
- Brak plików tymczasowych, roboczych, szkiców, kopii „v2/final/old”, notatek sesji i raportów agenta w repozytorium.
- Nowy plik wymaga uzasadnienia w opisie PR (wyjątek: kolejne ADR).
- Brak katalogów „na przyszłość”.

## Kod
- Python: standard library w pierwszej kolejności, PEP 8, czytelne nazwy, jawne typy tam, gdzie pomagają.
- Funkcje o jednej odpowiedzialności, kod reużywalny, minimalne zależności.
- Najpierw użyj istniejących modułów. Nie twórz alternatywnych implementacji tego samego zadania.
- Bez niepotrzebnych abstrakcji i „defensive overengineering”.

## Testy i walidacja (faza początkowa: luźno)
- Projekt jest we wczesnej fazie i będzie się zmieniał. Testy i walidacje są pomocnicze, nie blokujące.
- Pisz tylko kilka testów kluczowych reguł; nie dąż do pełnego pokrycia i nie dopisuj testów „na zapas”.
- Nie twórz rygorystycznych walidatorów, schematów ani sprawdzeń formatu, które będą się psuć przy każdej zmianie struktury.
- Padający test lub walidacja nie blokuje pracy ani scalenia: popraw szybko, jeśli to prosta poprawka; w przeciwnym razie zapisz w Issue i idź dalej.
- Gdy zmiana celowo unieważnia test, zaktualizuj test do nowego stanu. Nie usuwaj testów, by ukryć błąd w kodzie.
- Bez pustych atrap funkcjonalności.
- Zaostrzenie testów i walidacji nastąpi, gdy zostanie to jawnie zapisane w `docs/validation.md`.

## Instrument
- Zachowaj **dokładne brzmienie** pozycji i ich stabilne ID.
- Korekta pozycji tylko jako nowa wersja z uzasadnieniem.

## Rygor naukowy
- Oddzielaj: źródło → propozycję → decyzję badawczą → wykonany test → wynik empiryczny.
- Nie przedstawiaj planów, danych syntetycznych ani opinii jako potwierdzonej trafności.
- Nie wymuszaj czterech czynników, jednego wyniku globalnego, skoringu ani określonych efektów.
- Nie zmieniaj analizy po poznaniu wyników bez jawnego oznaczenia (data, powód).

## Dane i koszty
- Brak płatnych usług i runnerów oraz zbędnych workflow CI.

## Zakres zmian
- Zmiany małe: jedna zmiana = jeden cel.
- Praca w osobnej gałęzi, zmiana przez PR powiązany z Issue (`Closes #n`).

## Sprzątanie po zmianie (obowiązkowe)
Po każdej zakończonej zmianie agent samodzielnie, bez pytania o zgodę:
1. Szybko sprawdza, czy zmiana działa (zgodnie z sekcją „Testy i walidacja”).
2. Aktualizuje `docs/architecture.md` i ADR, jeśli zmiana ich dotyczy.
3. **Scala PR** (squash merge) do gałęzi głównej.
4. **Usuwa gałąź** zdalną i lokalną.
5. **Aktualizuje Issue**: status, krótkie podsumowanie, zamknięcie albo wskazanie, co zostało.
6. Usuwa pliki tymczasowe utworzone podczas pracy.
7. Nie zostawia otwartych PR-ów ani martwych gałęzi.

Jeśli scalenie jest niemożliwe (konflikt Git), agent zapisuje przyczynę w Issue i zgłasza ją zamiast pomijać krok.

## Raport końcowy
- Podaj: zmienione pliki, zakres, co faktycznie sprawdzono (i czego nie), stan PR/gałęzi/Issue.
- Bez ogólników; nie raportuj jako zrobionego tego, czego nie sprawdzono.
