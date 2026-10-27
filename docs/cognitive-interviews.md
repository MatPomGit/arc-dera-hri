# Wywiady poznawcze DERA-HRI v3

**Status: protokół roboczy. Nie potwierdzono zgody/opinii etycznej ani przeprowadzonych wywiadów.** Procedura należy do [badania trafności treściowej](content-validity.md). Nie potwierdza struktury czynnikowej, trafności skali ani kierunku pozycji.

## Cel i narzędzia

Ustalić, jak respondenci **rozumieją pytania, przypominają doświadczenie, wydają ocenę i przypisują ją do skali odpowiedzi**. Oceniać także kompletność treści, instrukcję i okres odniesienia. Zgodnie z metodologią [COSMIN (Terwee i in., 2018)](https://doi.org/10.1007/s11136-018-1829-0) nie można ograniczać oceny zrozumiałości wyłącznie do pojedynczych stwierdzeń.

- [Oryginalny kwestionariusz v3 EN (45 + 4)](https://github.com/MatPomGit/arc-dera-hri/blob/main/instruments/dera_hri_v3.csv): jedyne źródło dosłownych pytań.
- [Pusty arkusz obserwacyjny z 49 identyfikatorami](https://github.com/MatPomGit/arc-dera-hri/blob/main/instruments/dera_hri_v3_cognitive_log.csv): skopiować go **osobno dla każdego uczestnika**, nie wpisywać odpowiedzi do pliku w repozytorium.
- Wypełnione arkusze, dane kontaktowe, nagrania i transkrypcje są **danymi prywatnymi**; przechowywać lokalnie lub instytucjonalnie według zatwierdzonego planu ochrony danych.

## Warunki rozpoczęcia

1. Przyjąć i udokumentować populację. Źródłowy protokół proponuje dorosłych **18+**, rozumiejących język podawanej wersji **angielskiej**; badanie polskiej wersji wymaga niezależnej adaptacji i oceny.
2. Opisać konkretny scenariusz i faktycznie obserwowane kanały ekspresji. Przy użyciu **Unitree G1 EDU** zapewnić operatora, ocenę zagrożeń, procedurę awaryjnego przerwania i bezpieczny dystans. Nie zakładać, że głos, mimika czy gesty były dostępne.
3. Przed rekrutacją uzyskać odpowiednią zgodę/opinię etyczną lub formalnie udokumentowane zwolnienie; przygotować zgodę na ewentualne nagrywanie, reguły rezygnacji i okres retencji danych.
4. Dobierać respondentów celowo pod względem doświadczenia z robotami i kompetencji językowej. **Mała próba jakościowa nie oznacza reprezentatywności statystycznej.**

## Organizacja i przebieg

Propozycja ze źródłowego protokołu: **dwie iteracyjne rundy**, około **10 osób** w pierwszej i **5–10** w drugiej, łącznie około **15–20**. Jedna sesja wywiadu może trwać **60–90 minut**. Liczby i czas są orientacyjne, nie gwarantują nasycenia problemów.

1. **Zgoda i metadane:** zapisać pseudonim, wersję, język, konfigurację robota, scenariusz, tryb sterowania, datę i odstęp między interakcją a kwestionariuszem. Informacje identyfikacyjne trzymać oddzielnie.
2. **Interakcja HRI:** przeprowadzić ustandaryzowaną, bezpieczną sesję. Zatrzymać ją na życzenie lub w razie dyskomfortu. Rejestrować realnie występujące sygnały, nie tylko sprzętowe możliwości robota.
3. **Początek ankiety:** źródło zaleca rozpoczęcie **5–10 minut po HRI**, przed debriefingiem. Myślenie na głos wydłuża wypełnianie; czasu sesji poznawczej **nie porównywać z proponowanym progiem 3 minut** dla standardowej ankiety.
4. **Think-aloud:** przejść przez wszystkie **45 pozycji głównych**, jeśli uczestnik może to zrobić; dodatkowe M1–M3/F1 tylko, jeśli moduły wejdą do badania. Neutralnie pytać o znaczenie i tok odpowiedzi, nie sugerować „poprawnego” rozumienia.
5. **Probing:** po odpowiedzi albo po bloku zastosować neutralne pytania o treść, pamięć, ocenę i dopasowanie kategorii 1–7. Sprawdzić **instrukcję, okres odniesienia, etykiety skali oraz treści pominięte**. Brak kanału oznacza **problem zastosowalności**, nie odpowiedź neutralną.
6. **Zamknięcie:** ocenić obciążenie, powtarzalność i brakujące aspekty doświadczenia; debriefing według zatwierdzonego protokołu.

### Neutralny skrypt dla uczestnika (EN)

> “We are checking how these questions work, not testing you. Please think about the robot interaction you have just completed. As you answer, tell me what each statement means to you and how you choose your response. There are no right or wrong answers. If a statement does not apply, please tell me rather than choosing the middle option.”

Neutralne pytania: “What does this statement mean to you?”, “What part of the interaction were you thinking about?”, “How did you choose between these options?”, “What made this difficult to answer?”, “What important experience did we miss?”. Nie pytać w sposób sugerujący emocję, świadomy umysł ani intencję robota.

## Priorytetowe sondy treściowe

| ID v3 | Potencjalny mechanizm nieporozumienia |
| --- | --- |
| EAR 1–4, 11 | deklarowane odczucia vs domniemana fizjologia; przewidywalność vs kontrola |
| EAR 6–10 | komfort, dyskomfort, zbliżenie, unikanie i niesamowitość mają różne znaczenia |
| SEI 12–16 | kanały ruchu/głosu/gestów/mimiki, spójność kilku kanałów; **SEI 16** przy jednym kanale |
| SEI 19–23 | sens sygnału vs przypisywanie intencji; wysiłek interpretacji i „sztuczność” |
| SAP 26/28/30/32 | przyczyny zachowania, zaskoczenie i narzucona zależność przewidywalność → kontrola |
| MP 34–37 | metafory systemu vs atribucja „stanu”, przekonań i doświadczenia |
| RAR 38–45 | wpływ nieokreślony, ułatwiona regulacja i pogorszenie emocji |
| M1–M3/F1 | odróżnienie strategii, skutku i oczekiwanego wpływu przyszłych interakcji |

**SEI 16:** przy jednym kanale odnotować brak możliwości oceny zgodności **różnych** kanałów. Definitywna reguła kwalifikowalności pozycji jest jeszcze do zatwierdzenia. Oddzielić: brak kanału, niewidoczny/niesłyszalny sygnał, niezrozumienie i brak odpowiedzi.

## Rejestr i decyzje

W pustym formularzu notować osobno: zastosowalność (yes/no/unclear), odpowiedź 1–7, parafrazę uczestnika, obserwację i ewentualną propozycję korekty. Kody problemu:

- **C** niezrozumiałość, **R** trudność przypomnienia, **J** kryterium oceny, **S** dopasowanie odpowiedzi 1–7, **D** inny konstrukt, **A** brak zastosowania, **T** okres odniesienia. Wiele kodów oddzielać średnikiem.
- Nasilenie **0** brak; **1** drobny; **2** istotny; **3** uniemożliwiający interpretację. Ocena dotyczy **wpływu problemu**, nie arbitralnego odsetka uczestników.

**Runda 1:** przygotować listę problemów i propozycje zmian. **Runda 2:** zweryfikować poprawione pozycje, instrukcje oraz możliwe nowe nieporozumienia. Raportować liczbę zastosowalnych odpowiedzi dla każdego ID, jakościowe motywy, ograniczenia i odpersonalizowane przykłady. Zmiana zatwierdzonego brzmienia wymaga **kolejnej wersji banku**, nie edycji CSV v3. Bramka do pilotażu pozostaje w [protokole trafności treściowej](content-validity.md).

**Nie przedstawiać przygotowanego arkusza jako przeprowadzonych wywiadów ani ocen empirycznych.**
