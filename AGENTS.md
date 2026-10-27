# Zasady pracy: ARC-DERA-HRI

- W pierwszej kolejności przeczytaj `README.md`, `docs/model.md`, `docs/instrument.md`, `docs/validation.md` i `docs/sources.md`.
- Każdy nowy dokument źródłowy: porównaj z obecnym stanem; **zaktualizuj istniejącą treść**. Nowy plik twórz tylko dla odrębnego celu. Uzupełnij `docs/sources.md` i `CHANGELOG.md`.
- Zwięzłość i KISS. Nie powielaj opisów, programów, konfiguracji ani dokumentacji. Brak frameworków i architektury „na zapas”.
- Kod: Python standard library w pierwszej kolejności, PEP 8, czytelne nazwy, jawne typy tam, gdzie pomagają, funkcje o jednej odpowiedzialności, kod reużywalny, minimalne zależności.
- Najpierw użyj istniejących modułów. Nie twórz alternatywnych implementacji tego samego zadania; bez niepotrzebnych abstrakcji i „defensive overengineering”.
- Testuj istotne reguły, błędne i graniczne dane. Nie usuwaj testów, by ukryć błędy. Bez pustych atrap funkcjonalności.
- Zachowaj **dokładne brzmienie** pozycji i ich stabilne ID. Korekty pozycji tylko z nową wersją i uzasadnieniem.
- Oddziel: źródło → propozycję → decyzję badawczą → wykonany test → wynik empiryczny. Nie przedstawiaj planów, danych syntetycznych ani opinii jako potwierdzonej trafności.
- Nie wymuszaj czterech czynników, jednego wyniku globalnego, skoringu ani określonych efektów. Nie zmieniaj analizy po poznaniu wyników bez jawnego oznaczenia.
- Żadnych danych osobowych lub surowych odpowiedzi uczestników w publicznym Git. Brak płatnych usług, płatnych runnerów i zbędnych workflow.
- Zmiany mają być małe i sprawdzalne. Raportuj pliki, zakres oraz to, co faktycznie zweryfikowano.
