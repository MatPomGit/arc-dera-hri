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

## Reguła kolejnej aktualizacji

Nowy dokument aktualizuje istniejące syntetyczne opisy; pełny tekst pozycji i identyfikatory przechowuje jedno CSV na wersję. Niezgodności rejestrować, ale **nie poprawiać potajemnie** tekstu źródłowego. Wszelkie korekty kwestionariusza oznaczać kolejną wersją i dokumentować decyzję. Priorytetem pozostaje KISS.
