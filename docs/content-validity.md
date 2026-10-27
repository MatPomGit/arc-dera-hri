# Badanie trafności treściowej

**Status: przygotowany formularz i plan analizy; brak przeprowadzonego panelu, wywiadów i potwierdzenia decyzji etycznej.** Podstawa: `dera-hri-protocol-v3.docx` (protokół 1.0). [Kanoniczny bank v3](https://github.com/MatPomGit/arc-dera-hri/blob/main/instruments/dera_hri_v3.csv) zawiera **45 pozycji głównych**, a nie 44.

## Gotowe materiały panelu (EN)

- [Kompletny formularz ocen v3 (CSV)](https://github.com/MatPomGit/arc-dera-hri/blob/main/instruments/dera_hri_v3_expert_form.csv): 45 pozycji głównych i 4 **opcjonalne**; pełne teksty z banku bez poprawek.
- [Lokalny analizator CVR/CVI](https://github.com/MatPomGit/arc-dera-hri/blob/main/tools/content_validity.py) (Python, standard library) oraz [testy obliczeń](https://github.com/MatPomGit/arc-dera-hri/blob/main/tests/test_content_validity.py). Nie przetwarza danych w chmurze.

**Instrukcja dla oceniającego:** ocenić **każdą z 45 pozycji głównych**; M1–M3 i F1 wyłącznie jeśli badacz włączy moduły. `essentiality`: `essential`, `useful` lub `not_necessary`; `relevance`, `clarity` i `simplicity`: każda 1–4 (1 = niska, 4 = wysoka). `assigned_domain`: sugerowane EAR-D/SEI-D/SAP-D/MP-D/RAR-D, inne lub niejasne; `comment`: uwagi merytoryczne. Pozostawić pola puste, gdy nie można ocenić; nie kodować braku jako 1. Teksty itemów, ID, warunki i podskale są zamrożone.

**Dane prywatne:** każdemu ekspertowi przekazać **oddzielną kopię** CSV z pseudonimem w nazwie (np. `data/E01.csv`). Wypełnionych plików, transkrypcji i danych identyfikujących nie umieszczać w publicznym repo. Po pozyskaniu rzeczywistych ocen:

```bash
python tools/content_validity.py data/E*.csv > data/content_validity_summary.csv
```

Wynik zawiera liczebności, CVR, jednostronne dokładne `p`, I-CVI dla każdej cechy i S-CVI/Ave per domena (na stderr); puste wskaźniki pozostają puste. Analizator **nie usuwa pytań** ani nie tworzy syntetycznych odpowiedzi.

## 1. Przygotowanie

Ustalić uczestników docelowych, język, scenariusz HRI, definicje domen oraz warunki kanałowe. Wymagana jest odpowiednia opinia/zgoda etyczna lub udokumentowane zwolnienie, zgody na ewentualne nagrywanie i plan ochrony danych. Formularze ekspertów muszą zawierać wszystkie właściwe ID i pełne brzmienia pytań: aneksy w źródle są niekompletne.

## 2. Ocena ekspertów

Proponowany panel **12–15 osób**, reprezentujący HRI/robotykę, naukę o emocjach, psychometrię i zastosowania HRI. Każdy ocenia niezbędność pozycji (`essential / useful / unnecessary`) oraz osobno trafność, jasność i prostotę (trzy skale 1–4), z możliwością komentarza.

- **CVR Lawshego:** `(ne - N/2) / (N/2)`, gdzie `ne` to liczba ocen **essential**; nie mylić z odsetkiem ocen trafności 3–4.
- **I-CVI:** proporcja ocen 3–4, osobno dla danej cechy; **S-CVI/Ave:** średnia I-CVI w domenie.
- Rejestrować `N` **oddzielnie dla essentiality i każdej domeny oceny**, zakres konstruktu, uwagi jakościowe i wybraną metodę testu. W źródle pojawiają się orientacyjne granice (I-CVI ≥0,78, S-CVI/Ave ≥0,90); **nie są automatyczną regułą usuwania**.

### Dokładny test dwumianowy jako jawna propozycja analityczna

W źródłowym protokole podano tradycyjne tablice Lawshego (np. CVR 0,56 przy N=12 i 0,49 przy N=15). **Nie wolno ich mieszać z metodą dokładną**, dla której jednostronny test `Binomial(N, 0.5)`, `α=0,05`, daje:

| Liczba pełnych ocen essentiality | Minimalne `ne` przy `p≤0,05` | CVR przy tym `ne` |
| ---: | ---: | ---: |
| 12 | 10 | 0,667 |
| 13 | 10 | 0,538 |
| 14 | 11 | 0,571 |
| 15 | 12 | 0,600 |

To **propozycja jawnej analizy**, nie ustalony warunek włączenia pozycji. Nierówne `N` oraz dane jakościowe wymagają osobnego osądu. Ayre i Scally (2014) opisują wartości krytyczne obliczane z dokładnych prawdopodobieństw dwumianowych; Polit, Beck i Owen (2007) zwracają uwagę na problem zgodności przypadkowej w CVI.

Zgodnie z nowszą perspektywą COSMIN kluczowe są trzy aspekty: **relevance, comprehensiveness, comprehensibility**. [Arkusz kompletności pięciu domen (CSV)](https://github.com/MatPomGit/arc-dera-hri/blob/main/instruments/dera_hri_v3_domain_review.csv) zawiera po jednym wierszu dla EAR-D, SEI-D, SAP-D, MP-D i RAR-D. Ekspert ocenia pokrycie domeny 1–4, wskazuje **brakujące aspekty**, nakładanie się konstrukcji i ograniczenia kontekstu/kanalności. **Nie uśredniać tych ocen razem z item-level I-CVI**; to odrębna jakościowo-ilościowa ocena kompletności. Ocena `clarity` i `simplicity` w formularzu nie zastępuje systematycznej oceny **kompletności treści domen**. Każdy ekspert powinien więc odrębnie skomentować brakujące obszary w każdej domenie, a wywiady poznawcze objąć także instrukcję i odpowiedzi.

Literatura: [Ayre i Scally 2014](https://doi.org/10.1177/0748175613513808), [Polit i in. 2007](https://doi.org/10.1002/nur.20199), [Terwee i in. 2018](https://doi.org/10.1007/s11136-018-1829-0), [Mokkink i in. 2025](https://doi.org/10.1016/j.jclinepi.2025.111879).

## 3. Rewizja i wywiady poznawcze

Przewodnik: [protokół wywiadów poznawczych](cognitive-interviews.md); [pusty arkusz obserwacji 49 pozycji](https://github.com/MatPomGit/arc-dera-hri/blob/main/instruments/dera_hri_v3_cognitive_log.csv). Uzupełniono neutralne sondy, kodowanie trudności, kontrolę warunków SEI i rozróżnienie danych jakościowych od skoringu.

Propozycja **15–20 osób**, dwie rundy: **10**, potem **5–10** po modyfikacjach. Zastosować *think-aloud* i neutralne pytania o zrozumienie, przypomnienie doświadczenia, ocenę i wybór kategorii.

Priorytet: kierunki EAR/RAR, SEI 16 i warunki kanałów, nakładanie się SEI–SAP, mentalizacja MP i [wcześniej krytykowane sformułowania](instrument.md#pozycje-wymagające-oceny-treści).

Wywiady o interakcji sprzed do sześciu miesięcy (propozycja źródłowa) **nie są równoważne** badaniu odpowiedzi po świeżym doświadczeniu. Dla oceny procesu odpowiedzi preferować świeżą sesję lub jawnie ograniczyć cel badania do zrozumiałości tekstu.

## 4. Decyzja o pilotażu

Dla każdego ID zapisać: wersję, tekst, domenę, CVR, I-CVI, komentarze, problemy wywiadów, decyzję `keep/revise/remove/retest` i uzasadnienie. Zachować pokrycie konstruktu; nie skreślać pozycji wyłącznie z powodu jednego progu. Każda realna zmiana brzmienia powoduje **nową wersję instrumentu**.

Do przejścia dalej potrzebne są wykonane oceny, rozstrzygnięte reguły SEI, udokumentowana decyzja o banku i protokół [pilotażu](validation.md). Nie wymaga się jeszcze alfa, omega ani CFA.

**Koszty i autorstwo:** brak zatwierdzonego budżetu; nie zakładać honorariów z pliku źródłowego. Udział w panelu nie uprawnia sam w sobie do współautorstwa. Nagrania i dane osobowe pozostają poza publicznym GitHubem.
