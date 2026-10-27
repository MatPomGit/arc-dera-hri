# Plan badań walidacyjnych DERA-HRI

**Status:** plan kandydujący, bez wyników empirycznych; punktem wyjścia jest bank [v3.0](../instruments/dera_hri_v3.csv). Dokument źródłowy proponuje siedem etapów i orientacyjnie 42 miesiące, lecz to **niezatwierdzony harmonogram**, podobnie jak szacunkowe N.

**Operacyjny projekt pierwszego badania:** [walidacja treściowa v3, protokół roboczy](content-validity.md). Dokument określa panel ekspertów, oceny CVR/CVI, dwie rundy wywiadów poznawczych oraz rejestr decyzji. Badanie nie zostało rozpoczęte ani zatwierdzone etycznie na podstawie dostępnych materiałów.

## Bramka P0: ustalenie treści i modelu

1. Panel specjalistów psychometrii/HRI/psychologii emocji: pokrycie domen, jednoznaczność, rozumienie sformułowań, ocena przydziału pozycji. CVI/CVR wyłącznie z kryteriami właściwymi dla liczby ekspertów; dla wielu oceniających nie stosować automatycznie *Cohen's κ*.
2. Wywiady poznawcze w **języku administracji**: SEI zależne od kanałów, MP i antropomorfizacja, pary o przeciwnej walencji, kontrola i koszt wypełnienia. Po zmianie pozycji zachować nową wersję.
3. Ustalić populację, HRI scenariusz, warunki fizycznego bezpieczeństwa/etyki, procedurę zgód, kompletny bank oraz metadane sesji.
4. Rozstrzygnąć pozycje o sprzecznych kierunkach, reguły strukturalnego `nie dotyczy`, nadmiarowość i zasady wyliczeń. Śledzenie: [Issue #1](https://github.com/MatPomGit/arc-dera-hri/issues/1).

## Kolejne etapy (warunkowe)

| Etap | Pytanie | Podstawowy dowód |
| --- | --- | --- |
| Pilotaż | Czy pozycje i procedura działają? | rozkłady, braki, zrozumiałość, czas, artefakty kanałów |
| Struktura | Ile czynników rzeczywiście występuje? | EFA/ESEM; później niezależna CFA, porównanie alternatyw |
| Rzetelność | Z jaką precyzją wyniki mierzą postulowane domeny? | ω/α z niepewnością, właściwy model pomiaru |
| Trafność zewnętrzna | Czy wyniki wiążą się z odpowiednimi konstruktami? | SAM/PAD, antropomorfizacja, zaufanie, akceptacja, zachowanie |
| Kontekst i czas | Czy wyniki są porównywalne między zadaniami i robotami? | ocena inwariancji, powtórzenia, opcjonalnie ESM/EDA/HRV |
| Adaptacje i rozszerzenia | Czy narzędzie działa w innych językach/populacjach? | procedura adaptacji, inwariancja i niezależna ocena |

Siedmioetapowy plan źródłowy przewiduje także wielokulturową walidację, analizy sieciowe, LPA, testy podłużne i ewentualną wersję skróconą. **Nie są konieczne do uruchomienia minimalnego pilotażu i nie stanowią obietnicy realizacji.** Wielkość próby wyznaczyć z rozważanych modeli, precyzji oszacowania, dostępności warunków i braków danych, a nie mechanicznie ze źródłowego `n=300–500` czy `2000–3000`.

## Wnioski z historycznej recenzji v1

Z krytycznej analizy `Recenzja-DERA-HRI.md` (również w PDF) pozostają aktualne wymagania: mierzyć trafność względem PAD/SAM, kontrolować efekt halo, społeczną pożądaność, doświadczenie z robotami, cechy empatii, różnice środowiska/trybu autonomii oraz oddzielać subiektywne doznania od fizjologii. Ewentualna weryfikacja porządku EAR/SAP/SEI/RAR i opóźnień <200 / 100–500 / 500–2000 ms wymaga danych czasowych i protokołu, nie ankiety po jednej interakcji. Raport nie zawiera danych walidacyjnych. Przewidywany harmonogram 3–4 lata i wielkości prób są orientacyjne, **nie stanowią obowiązkowych bramek**; do pilotażu należy dopuścić wersję rozwojową z właściwym oznaczeniem i zgodami. [Status źródeł](sources.md#audyt-źródłowy-recenzji-v1).

## Specyfikacja postulowana w manuskrypcie v3

Szkic artykułu `kwestionariusz-dera-hri_v3.docx` podaje jako cele: α/ω ≥0,80; test–retest po dwóch tygodniach ≥0,70; CVR ≥0,75 (panel co najmniej 5 osób); CFA: CFI/TLI ≥0,95, RMSEA ≤0,06, SRMR ≤0,08; dodatkowo `ΔR² ≥10%` ponad modele wymiarowe. **Są to oczekiwania źródła, nie uzyskane parametry, normy ani automatyczne kryteria przyjęcia.** Zwłaszcza CVR zależy od liczby ekspertów i definicji oceny „niezbędności”; test–retest wymaga stabilnego kontekstu przy narzędziu mierzącym doświadczenie *stanu*.

Artykuł koncepcyjny może prezentować model, bank i plan walidacji, ale nie wolno opisywać ich w abstrakcie jako uzyskanej trafności. Wyniki własnej walidacji wymagają odrębnych danych, analiz, protokołu i sekcji Results. Zewnętrzna podstawa dla luk w psychometrii HRI: Vagnetti i in., *J Med Internet Res* **2024;26:e55597**, [DOI](https://doi.org/10.2196/55597).

## Reguły interpretacji

- **Hipotezy**: EAR↔pobudzenie, SEI↔czytelność sygnałów, SAP↔przewidywalność/kontrola, MP↔antropomorfizacja, RAR↔regulacja emocji; związek SEI–SAP–RAR oraz rola MP jako moderatora wymagają osobnych projektów do wnioskowania przyczynowego.
- Nie przyjmować „pięciu czynników” jako oczekiwanego wyniku; porównywać struktury prostsze i potencjalne ładunki krzyżowe. Nie usuwać pozycji wyłącznie po to, aby poprawić α czy dopasowanie modelu.
- Nie używać arbitralnych progów CVR, CFI/RMSEA, α, 20% braków, czasu 3 minut ani skutków o `d≥0,5` jako automatycznych bramek bez uzasadnienia metodycznego.
- W pozycjach porządkowych 1–7 dobierać estymację do rozkładów i modelu. Wyraźnie oddzielać brak kanału od braku odpowiedzi; nie stosować prostego FIML do wszystkich schematów.
- Raportować wyniki ujemne i zerowe, ograniczenia, z góry zaplanowane analizy i eksplorację; test–retest interpretować względem cechy/stanu po konkretnym doświadczeniu.
- Korzystać z odpowiednich standardów AERA/APA/NCME i COSMIN po weryfikacji zakresu; źródłowe pozycje bibliograficzne wymagają niezależnej kontroli przed publikacją.
