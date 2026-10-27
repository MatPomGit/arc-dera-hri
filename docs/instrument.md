# Kwestionariusz DERA-HRI (wersje rozwojowe)

**Aktualna propozycja:** [DERA-HRI v2.1](../instruments/dera_hri_v2_1.csv), 48 pozycji i cztery postulowane domeny po 12 pozycji. [DERA-HRI v2](../instruments/dera_hri_v2.csv) pozostaje nienaruszony jako materiał porównawczy. Treść w CSV jest wierną transkrypcją propozycji z recenzji; żadna wersja nie została zwalidowana.

## Administracja

Bezpośrednio po **jednej konkretnej interakcji z robotem**, zgodnie z wersją protokołu. Proponowana instrukcja v2.1: „Proszę odpowiedzieć, w jakim stopniu poniższe stwierdzenia opisują Pana/Pani doświadczenie w trakcie tej konkretnej interakcji z robotem.”

Odpowiedzi **1–7** (v2.1: 1 „Zdecydowanie nie”, 7 „Zdecydowanie tak”). Pełne etykiety kategorii w wersji v2 i krótsze kotwice v2.1 wymagają ujednolicenia i sprawdzenia w wywiadach poznawczych. Nie wprowadzać zmienionego formularza pod tym samym ID wersji.

## Klucz z dokumentu źródłowego, niezatwierdzony

Recenzja proponuje odwrócenie (`8 – odpowiedź`) następujących pozycji:

- EAR-D: **6, 12**;
- SAP-D: **17, 23**;
- SEI-D: **31, 32, 34, 36**;
- RAR-D: **41, 42, 43**.

Kolumna `reverse` w CSV zapisuje **propozycję recenzji**, nie poprawny i zatwierdzony skoring. **Nie implementować automatycznego obliczania wyników.**

Szczególna niespójność: pozycja **6** („komfort cielesny”) jest oznaczona do odwrócenia, choć reaktywność nie oznacza automatycznie dyskomfortu. Ponadto pozycje EAR 6–9 reprezentują różne bieguny doświadczenia, a 11 mówi o przewidywalności, nie wielkości pobudzenia. Wymaga to rozdzielenia koncepcji konstruktów przed zatwierdzeniem średniej.

## Proponowane moduły analityczne

- SAP-D: pozycje 13–18 i 23–24 jako rdzeń predykcji; 19–22 potencjalnie osobny moduł atrybucji/mentalizacji, ale **nie usuwać ich z banku v2.1 bez nowej wersji**.
- SEI-D: 26 tylko przy obecnym głosie, 27 przy gestach/zmianach postawy, 28 przy co najmniej dwóch kanałach. **Brak zastosowania ≠ zwykły brak odpowiedzi ani wartość 4.** Proponowana średnia z dostępnych pozycji wymaga walidacji porównywalności między konfiguracjami kanałów; należy raportować zestaw i liczbę odpowiedzi.
- RAR-D: recenzja proponuje jako rdzeń efektu **38–43, 47** (41–43 odwrócone); 37 = ogólny wpływ, 44–46 = strategie, 48 = intencja ponownej interakcji. To hipoteza strukturalna, nie końcowy wynik podskali.
- Nie ma zatwierdzonego **wyniku globalnego**, średniej dla żadnej podskali ani zasad traktowania braków danych.

## Metadane poza skalą

Wersja instrumentu, anonimowy identyfikator sesji, konfiguracja robota i tryb sterowania, użyte kanały (ruch, głos, gesty itd.), zadanie, czas interakcji i odległość czasowa do ankiety. Kontrole badawcze (do decyzji przed pilotażem): wcześniejsza ekspozycja na roboty, postawy (np. NARS), antropomorfizacja, ogólny komfort z technologią; dobór miar zewnętrznych wraz z licencją.

**Do sprawdzenia:** nakładanie się 19–22 z mind perception, 31/33/35/36 z SAP, negatywnych pozycji 41–43 oraz podobieństwo semantyczne 19–20 i 31/36. Zmiany itemów wyłącznie w nowej wersji i z zapisanym uzasadnieniem.
