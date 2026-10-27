# Źródła i wersje

| Dokument autora | Co wnosi | Status |
| --- | --- | --- |
| `Własny kwesionariusz.odt` | wcześniejszy, hierarchiczny E-HRAISE | historyczna koncepcja |
| `DERA-HRI-1.pdf` (07.02.2026) | 4 domeny, 32 pozycje | historyczna v1 |
| `DERA-HRI-1_analysis.md` | wtórna analiza v1 | materiał pomocniczy |
| `Recenzja-DERA-HRI.md` / `Recenzja-DERA-HRI.pdf` (raport z 07.02.2026) | krytyczna ocena **v1** (32 pozycje) i propozycje rewizji/walidacji | **jedna historyczna analiza w dwóch formatach**, nie nowa recenzja v3 |
| `Projekt-DERA-HRI-2.odt` | 4 domeny, 48 pozycji, metody | historyczna v2 |
| `Recenzja-DERA-HRI-2.odt` | językowo zmienione 48 pozycji; MP jako wariant | historyczna v2.1 |
| **`DERA-HRI-3.md`** (wersja autorska 3.0, data podana: luty 2026) | **5 domen, pełny bank EN, moduły M1–M3/F1, plan 7-etapowy** | **aktualna propozycja; bez walidacji** |
| `kwestionariusz-dera-hri_v3.docx` | angielski **szkic artykułu koncepcyjno-metodologicznego**, 45 pozycji opisanych przez zakresy ID, 13 pozycji bibliografii i propozycje progów walidacyjnych | **materiał do rewizji redakcyjnej**, nie nowa wersja instrumentu ani wynik empiryczny |
| `dera-hri-protocol-v3.docx` (protokół 1.0, luty 2026) | projekt oceny treści: panel 12–15 ekspertów, CVR/CVI, 15–20 wywiadów poznawczych, dwie rundy | **źródło roboczego protokołu badań**, nie uzyskana zgoda ani wyniki |
| `opis-kwestionariusza_v3.docx` (v3.0, luty 2026) | **pełny formularz EN** (45 pozycji głównych + M1–M3/F1), instrukcje podskal, administracja, skoring kandydacki i plan walidacji | **zgodny tekst 49 pozycji z CSV; dokument opisowy, bez nowych wyników** |

Wersje źródłowe są **propozycjami projektowymi**, a nie wynikami badań. Nowy bank zapisano w [`instruments/dera_hri_v3.csv`](../instruments/dera_hri_v3.csv); historyczne v2 i v2.1 pozostają nienaruszone. Zmiany treści i języka oraz nowa numeracja nie oznaczają równoważności pomiarowej.

## Ustalenia krytyczne przy integracji v3

1. Dokument kilkukrotnie deklaruje **44 główne pozycje**, ale numeruje **1–45**; tabela końcowa poprawnie sumuje 45, wraz z M1–M3/F1 daje **49**.
2. Stwierdza **0 pozycji odwracanych**, jednak niektóre opisują odwrotne kierunki konstruktów (SEI 19/22, SAP 28/30, RAR 42–44), a niektóre są niejednoznaczne (EAR 6–9, RAR 38). Bez decyzji o operacjonalizacji **średnie nie są interpretowalne**.
3. SEI 16 opisuje zgodność wielu kanałów, chociaż źródło nazywa go obowiązkowym dla wszystkich; wymaga odrębnej reguły obecności kanałów i oceny inwariancji.
4. W opisie zmian wersji błędnie podano **12 odwróconych pozycji v1 i v2**: v1 wymieniała **10**, v2 miała **9**, v2.1 miała **11** oznaczeń odwrócenia.
5. W tekście pojawiają się nieaktualne odniesienia do numerów wcześniejszych wersji (np. sekcja 3.1.2), a określenie „validated item content” jest **nieuprawnione** bez dokumentu walidacyjnego.
6. Propozycje liczebności, progów wykluczeń, średnich, norm opisowych i terminów badań **nie są decyzjami zatwierdzonymi ani wynikami empirycznymi**.
7. Zakres MP-D w czterech pozycjach dotyczy głównie przypisywanej sprawczości/intencjonalności; pełna definicja agency + experience wymaga weryfikacji treściowej.

Dokument źródłowy zawiera bibliografię i mapę pozycji v2→v3, lecz ich poprawność (metadane cytowań, zgodność wordingów i wersji) wymaga niezależnego przeglądu przed wykorzystaniem w manuskrypcie.

## Audyt źródłowy recenzji v1

- Raport dotyczy **czterech systemów v1**, a nie pięciodomenowego banku v3. Wskazuje problemy: retrospektywny pomiar procesów dynamicznych, samoopis reakcji prerefleksyjnych, nieudowodniona rozdzielność czynników, kontrola dominacji i efekty halo/antropomorfizacji.
- Rekomendacje historyczne (rozszerzenie do 48 pozycji, negatywna regulacja, kanały ekspresji, siedem faz walidacji) wpłynęły na rozwój v2–v3. Nie przesądzają o przywróceniu modelu czteroczynnikowego ani odwróconych pozycji, które v3 kwestionuje.
- W raporcie deklaruje się przegląd **1030 publikacji**, ale dołączona bibliografia zawiera kilkanaście skrótowych opisów bez kompletnej identyfikacji; **nie można niezależnie potwierdzić liczebności korpusu ani metody systematycznego przeglądu**.
- Sugerowana hierarchia czasowa (EAR <200 ms, SAP 100–500 ms, SEI 500–2000 ms) jest **hipotezą historyczną bez przedstawionego testu w HRI**; nie stanowi ustalonej kolejności neurofizjologicznej. Wymóg ukończenia pełnych siedmiu faz przed *jakimkolwiek* badaniem nie obejmuje pilotaży prowadzonych właśnie w celu rozwoju i walidacji skali.
- Pliki Markdown i PDF mają odpowiadające sobie sekcje i zasadniczo tę samą treść; nie liczyć ich jako dwóch niezależnych ocen. Wnioski raportu traktować jako ocenę teoretyczno-metodologiczną, nie dodatkowe dane empiryczne.

## Szkic artykułu koncepcyjnego v3

`kwestionariusz-dera-hri_v3.docx` („The DERA-HRI v3 Framework: A Process-Oriented Approach to Measuring Emotional Experience in Human-Robot Interaction”) opisuje ramy teoretyczne, ewolucję v1→v3, proponowane właściwości pomiarowe i zastosowania. Jego wkładem jest **narracja na potrzeby publikacji koncepcyjno-metodologicznej**; nie przedstawia nowej wersji kwestionariusza, wyników eksperckiego panelu ani wyników walidacji.

**Konieczne sprostowania przed zgłoszeniem:**
- Deklaruje, że wszystkie pytania podano w całości („Data Availability”), lecz tekst podaje **zakresy numerów 1–45 i M1–M3/F1**, nie pełne treści pozycji. W manuskrypcie należy dodać kompletny, identyczny z bankiem v3 formularz lub poprawny odsyłacz do wersjonowanego materiału dodatkowego.
- Sformułowania „Results”, „resolves all 18 issues” i „systematically addressed through expert review” opisują **ocenę projektu**, nie zweryfikowane wyniki psychometryczne ani udokumentowany panel ekspertów. Należy przedstawić to jako *proponowane rozwiązania* i podać dowód procesu przeglądu, jeżeli taki istnieje.
- W sekcji metod dokument proponuje **minimalnie 6 odpowiedzi dla SEI-D** oraz stałą regułę średniej; nie rozstrzyga to braku kanałów i porównywalności różnych zestawów wskaźników (zwłaszcza SEI 16).
- Progów CVR ≥0,75 przy n≥5, α/ω ≥0,80, CFA CFI ≥0,95, `ΔR² ≥10%`, dwóch tygodni test–retest i n określanych bez uzasadnienia nie uznaje się za zaakceptowane kryteria psychometryczne.
- **Zweryfikowana korekta bibliografii [3]:** Vagnetti i in., *Instruments for Measuring Psychological Dimensions in Human-Robot Interaction: Systematic Review of Psychometric Properties*, **J Med Internet Res 2024;26:e55597**, DOI [10.2196/55597](https://doi.org/10.2196/55597), a nie „2023” jak w pliku. Bibliografia [2] Fiorini i in., [10.2196/45494](https://doi.org/10.2196/45494), odpowiada publikacji z 2024. Pozostałych pozycji nie uznano automatycznie za zweryfikowane.

Nie scalać tego manuskryptu z przyszłym **artykułem empirycznym o walidacji skali** jako rzekomo ukończonej analizy. Ewentualna odrębność publikacyjna wymaga oceny wkładu i polityki czasopisma.

## Protokół walidacji treściowej, wersja źródłowa 1.0

[Zwięzła procedura wdrożeniowa](content-validity.md) powstała na podstawie `dera-hri-protocol-v3.docx`. Do poprawienia przed rekrutacją:

- W tekście i zaproszeniach występuje **44**, podczas gdy kanoniczny bank v3 liczy **45 pozycji głównych**; istnieją ponadto M1–M3 i F1. Formularz CVR/CVI należy wygenerować dla prawidłowej, zamrożonej listy ID.
- Dokument nazywa schemat „three-phase”, po czym opisuje **cztery** fazy procesu i **siedem** etapów harmonogramu. Ujednolicić nazewnictwo; terminy 4–5 miesięcy są orientacyjne.
- Aneksy D i E zawierają jedynie fragmenty formularzy (`[Continue for all items...]`), dlatego deklaracja `Ready for Implementation` **nie oznacza** gotowych, kompletnych formularzy ani zgody etycznej.
- Wywiady z osobami przypominającymi interakcję sprzed **do sześciu miesięcy** nie są równoważne ankiecie 5–10 minut po sesji. Najpierw zdecydować, czy celem jest rozumienie pytań na podstawie wspomnień, czy proces odpowiedzi po świeżej, ustandaryzowanej ekspozycji.
- Proponowane stawki **200–300 USD za ocenę ekspercką i 30–50 USD za wywiad** nie są przyjęte; projekt obowiązuje zasada bezkosztowa. **Nie proponować współautorstwa jako ekwiwalentu wynagrodzenia**: wymaga niezależnego spełnienia kryteriów wkładu, zatwierdzenia i odpowiedzialności ([ICMJE](https://icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html)).
- CVR i CVI mają różne cele (niezbędność vs trafność/ocena zrozumiałości); progi `I-CVI 0.78`, `S-CVI/Ave 0.90` i tablice CVR zależne od N to **propozycje wymagające metodologicznego uzasadnienia**, nie automatyczny nakaz usuwania elementów unikalnych dla konstruktu.
- Brak dostarczonych ocen ekspertów, wywiadów, protokołu zgody/zwolnienia od komisji etycznej i polityki lokalnego przechowywania nagrań. Wszystkie wyniki tabel w aneksach są **przykładami lub szablonami**.

## Pełny opis kwestionariusza v3 (DOCX)

Z `opis-kwestionariusza_v3.docx` porównano **wszystkie 49 dosłownych brzmień stwierdzeń** z kanonicznym CSV: zgodność 49/49. Unikatową wartością dokumentu są kompletne instrukcje dla uczestników i podskal, wskazówki dotyczące kanałów oraz propozycje analizy podwymiarów; włączono je zwięźle do [specyfikacji instrumentu](instrument.md#pełny-formularz-źródłowy-v3).

**Nie przenosić do obowiązującej metodyki następujących niespójności:**
- W części wstępnej nadal „**44** core items”, choć sekcja 6 i tabela zawierają **45**. Sekcje teoretyczne korzystają z innych numeracji (np. MP 41–44, SEI 25–36, SAP 13–24), sprzecznych z aktualnym bankiem MP **34–37**, SEI **12–23**, SAP **24–33**.
- Tabela ewolucji powtarza **12 pozycji odwracanych w v1 i v2**, sprzecznie z dokumentami historycznymi (odpowiednio 10 i 9 oznaczeń). Stwierdzenie o wcześniej „validated item content” nie ma udokumentowanej podstawy empirycznej.
- Sekcja 9.2.1 **błędnie utożsamia CVR Lawshego z liczbą ocen trafności 3–4**; potrzebne oddzielne pytanie o niezbędność. Dla wieloosobowego panelu `Cohen's κ` nie jest właściwą ogólną miarą zgodności.
- Polecenie wypełnienia wszystkich pytań jest niespójne z celowym pomijaniem niedostępnych kanałów SEI 12–15 (i problemem SEI 16); automatyczne uśrednianie warunkowych pozycji nie gwarantuje równoważności.
- Propozycja **braku odwróceń** i interpretacji prostych średnich ignoruje odmienne kierunki np. RAR 39–41 vs 42–44, SAP 28/30, SEI 19/22. Wskaźniki progowe, przykładowe profile i sugestie kliniczne nie zostały zwalidowane.
- **F1** pyta o przewidywany wpływ regularnych interakcji na samopoczucie, nie o intencję kolejnego spotkania mimo etykiety `Future Interaction Intentions`.

Numeracja i sformułowania w opisach/załącznikach mają niższy priorytet niż zweryfikowana **pełna lista pozycji z sekcji 6**. Propozycje pozostają historycznymi założeniami do badania, nie wynikami.

## Reguła kolejnej aktualizacji

Nowy dokument aktualizuje istniejące syntetyczne opisy; pełny tekst pozycji i identyfikatory przechowuje jedno CSV na wersję. Niezgodności rejestrować, ale **nie poprawiać potajemnie** tekstu źródłowego. Wszelkie korekty kwestionariusza oznaczać kolejną wersją i dokumentować decyzję. Priorytetem pozostaje KISS.
