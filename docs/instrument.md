# Kwestionariusz i administracja

**Bank kandydujący:** [DERA-HRI v3.0 (EN)](https://github.com/MatPomGit/arc-dera-hri/blob/main/instruments/dera_hri_v3.csv). Potwierdzono zgodność 49/49 brzmień ze źródłowym `opis-kwestionariusza_v3.docx`. Historyczne [v2.1](https://github.com/MatPomGit/arc-dera-hri/blob/main/instruments/dera_hri_v2_1.csv) i [v2](https://github.com/MatPomGit/arc-dera-hri/blob/main/instruments/dera_hri_v2.csv) nie są równoważnymi wersjami językowymi v3.

| Domena | Identyfikatory v3 | Pozycje |
| --- | --- | ---: |
| EAR-D | 1–11 | 11 |
| SEI-D | 12–23 | 12 |
| SAP-D | 24–33 | 10 |
| MP-D | 34–37 | 4 |
| RAR-D | 38–45 | 8 |
| Strategie RM | M1–M3 | 3 |
| Oczekiwany wpływ F1 | F1 | 1 |

**Suma: 45 podstawowych + 4 dodatkowe = 49** (nie 44, jak w niektórych wstępach źródeł). M1–M3 i F1 raportować oddzielnie; F1 pyta o **przewidywany wpływ regularnych interakcji na samopoczucie**, a nie deklarowaną chęć kolejnego spotkania.

**Nowy wariant językowy:** [polski dokument Word (DOCX)](https://github.com/MatPomGit/arc-dera-hri/blob/main/instruments/dera_hri_v3_pl.docx) · [kompletny formularz v3.0-PL w MkDocs](questionnaire-pl.md) i [bank PL (CSV)](https://github.com/MatPomGit/arc-dera-hri/blob/main/instruments/dera_hri_v3_pl.csv). Jest to tłumaczenie robocze z tymi samymi 49 ID, a **nie potwierdzona adaptacja psychometryczna**. Wszelkie zbierane dane wymagają oznaczenia języka i identyfikatora wersji; nie scalać wersji EN i PL bez sprawdzenia równoważności.

## Proponowana administracja

Ankieta dotyczy **jednej właśnie zakończonej interakcji**. Wersja źródłowa zaleca podanie formularza **5–10 minut** po sesji, przed debriefingiem, w poufnym otoczeniu. Uczestnik odpowiada na podstawie własnego doświadczenia, nie ogólnych przekonań o robotach.

**Siedem kategorii zgody:** 1 Strongly disagree; 2 Disagree; 3 Somewhat disagree; 4 Neither agree nor disagree; 5 Somewhat agree; 6 Agree; 7 Strongly agree.

Zapis sesji powinien identyfikować wersję i język instrumentu, scenariusz, robota, sterowanie, dostępne kanały, czas i moment wypełnienia. Surowych danych uczestników nie przechowywać w publicznym repozytorium.

## Kanały ekspresji

SEI 12–15 odpowiadają odpowiednio za ruch, głos, gesty i mimikę. Jeśli kanał nie występuje, stosować **`nie dotyczy`**, nie wartość neutralną. **SEI 16** wymaga co najmniej dwóch rozróżnialnych kanałów, mimo że źródło nazywa je bezwarunkowym. Regułę kwalifikowania pozycji i porównywalności wyników trzeba zatwierdzić przed pilotażem.

## Punktowanie: brak zatwierdzonego klucza

Źródła v3 proponują proste średnie i brak odwracania pozycji. Nie ma jednak uzasadnienia dla monotonicznego wyniku w mieszanych kierunkowo domenach:

- **EAR 6–11:** komfort, dyskomfort, podejście, unikanie, niesamowitość i kontrola mają różne znaczenia.
- **SEI 19, 20, 22:** trudność interpretacji, zmiana znaczenia i zakłócenie sztucznością nie są równoważne czytelności.
- **SAP 28, 30:** zaskoczenie/nieprzewidywalność przeczą części innych pozycji.
- **RAR 38, 42–44:** niesprecyzowany wpływ i pogorszenie stanu emocjonalnego nie są tym samym co uspokojenie.

**Nie używać automatycznych średnich, progów „niski/średni/wysoki”, norm klinicznych ani wyniku globalnego**. Limit 20% braków i wykluczanie wypełnień krótszych niż 3 minuty pozostają propozycjami źródłowymi.

## Pozycje wymagające oceny treści

W v3 powróciły sformułowania krytykowane w recenzji v2.1: **EAR 11** łączy przewidywalność z kontrolą; **SEI 19/22** wprowadzają interpretowanie intencji i sztuczność; **SAP 26/32** sugerują przyczyny lub narzucają związek przyczynowy. Ponadto MP-D koncentruje się na przypisywanej sprawczości, nie pełnym rozumieniu *mind perception*.

Do oceny przed pilotażem dostępny jest [formularz ekspercki zawierający całe 49 pozycji](https://github.com/MatPomGit/arc-dera-hri/blob/main/instruments/dera_hri_v3_expert_form.csv) (cztery modułowe są opcjonalne). **Nie modyfikować pozycji w istniejącym pliku**: rewizja wymaga nowego banku i rejestru decyzji. Zobacz [trafność treściową](content-validity.md) i [otwarte Issue #1](https://github.com/MatPomGit/arc-dera-hri/issues/1).
