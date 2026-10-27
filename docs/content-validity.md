# Badanie trafności treściowej DERA-HRI v3

**Status:** projekt operacyjny na podstawie `dera-hri-protocol-v3.docx` (protokół źródłowy 1.0, luty 2026). **Nie potwierdzono zgody etycznej, rekrutacji ani wyników.** Badanie ma poprzedzać pilotaż i właściwą walidację czynnikową; nie stanowi samo w sobie potwierdzenia pięcioczynnikowego modelu.

## Przed uruchomieniem

- Zamrozić [bank v3](../instruments/dera_hri_v3.csv): **45 pozycji głównych** (EAR 11, SEI 12, SAP 10, MP 4, RAR 8). M1–M3/F1 oceniać osobno tylko, jeśli włączono moduły. Źródłowe „44 items” jest błędem.
- Uzgodnić język ankiety, scenariusz HRI, dostępne kanały SEI, definicje pięciu domen i zakres adult population. Uwzględnić [problemy treści v3](instrument.md#nierozwiązane-regresje-treściowe-v21--v3).
- Uzyskać właściwą opinię/zgodę lub udokumentowane zwolnienie etyczne, informację dla uczestników, zgodę na nagrywanie, zasady ochrony i okresu przechowywania danych. Status „Ready for Implementation” w źródle nie jest taką zgodą.
- Wygenerować **kompletne** arkusze dla wszystkich ID z CSV. Aneksy D/E w źródle to niekompletne przykłady, a nie 45 gotowych kart.

## Etap 1. Panel ekspercki (propozycja: 12–15 osób)

Reprezentacja: HRI/robotyka (4–5), badania emocji (3–4), psychometria (2–3), zastosowania HRI (2–3). Liczby to cele rekrutacyjne, nie twarde warunki dopuszczenia; szczególnie rejestrować rzeczywistą liczbę ocen dla każdej pozycji.

Każdy ekspert ocenia **każdą właściwą pozycję** pod kątem:
- niezbędności: `essential / useful but not essential / not necessary` (CVR);
- trafności względem domeny, jasności i prostoty: trzy odrębne skale **1–4** (CVI lub analogiczne wskaźniki jakości);
- dopasowania do konstruktu, brakujących treści, redundancji, warunków kanałowych i poprawek językowych (komentarze).

**Obliczenia:** `CVR = (ne - N/2)/(N/2)`; `I-CVI = liczba ocen 3–4 / N`, osobno dla kryterium; `S-CVI/Ave = średnia I-CVI`; opcjonalnie `S-CVI/UA = udział pozycji z pełną zgodą`. Raportować dokładne `N`, `ne`, zasady braków i niepewność. Źródło podaje dla CVR przykładowe kryteria **0,56 przy N=12** i **0,49 przy N=15**, oraz dla I-CVI propozycję **≥0,78** i S-CVI/Ave **≥0,90**. Przed badaniem wskazać wybraną wersję tablic, metodę interpretacji i sposób postępowania z oceną jasności/prostoty. **Nie odrzucać pozycji automatycznie** na podstawie jednego wskaźnika.

## Etap 2. Rewizja pozycji

Połączyć wskaźniki, komentarze ekspertów i pokrycie konstruktu. Dla każdego ID zapisać `keep / revise / remove / re-test`, podstawę decyzji i proponowany tekst. Zmiany po zamrożeniu banku tworzą **nową wersję** kwestionariusza; nie zmieniać potajemnie pliku v3.

## Etap 3. Wywiady poznawcze (propozycja: 15–20 osób)

Dwie rundy: pierwsza **10 osób**, druga **5–10** po wprowadzeniu poprawek. Metoda: *think-aloud* oraz neutralne dopytywanie o rozumienie, przypominanie doświadczenia, ocenę i wybór odpowiedzi. Kodować trudności semantyczne, pamięciowe, poznawcze, związane ze skalą i z zakresem konstruktu. Priorytet: EAR 11, SEI 16/19/22, SAP 26/32, kierunek RAR 38–45, MP i faktycznie dostępne kanały.

**Ważna decyzja:** protokół źródłowy dopuszcza wspomnienia interakcji sprzed **6 miesięcy**, ale docelowy formularz mierzy sesję ocenianą **5–10 minut po zakończeniu**. Dla oceny działania pomiaru preferować świeże, porównywalne doświadczenie robota; wywiady o odległym wspomnieniu mogą służyć jedynie wstępnemu badaniu zrozumiałości, z jawnie ograniczoną interpretacją. Kolejna runda powinna sprawdzić, czy rewizja poprawiła rozumienie bez nowych problemów.

## Etap 4. Raport i bramka do pilotażu

W jednym rejestrze pozycji zapisać: ID, wersję, domenę, pierwotne/zmienione brzmienie, `ne/N`, CVR, I-CVI (trzy kryteria), komentarze, problemy wywiadów, decyzję i uzasadnienie. Raport powinien uwzględnić zarówno wyniki pozytywne, jak i negatywne oraz niepewność interpretacji i brakujące domeny.

Bramka: komplet materiałów, rzeczywista ocena treści przez panel i docelową grupę, rozstrzygnięte problemy kanałowe, zatwierdzony zestaw pozycji/administracja oraz protokół pilotażu. **Brak wymogu uzyskania na tym etapie alfa/omega, CFA czy zatwierdzonego skoringu.** Plan przyszłych analiz pozostaje w [validation.md](validation.md).

## Bezpieczeństwo, etyka i koszty

- Udział dobrowolny; oddzielić klucz identyfikacyjny od pseudonimizowanych ocen i transkrypcji. Nagrania, dane osobowe i formularze zgód **nie trafiają do publicznego GitHuba**.
- Korzystać z bezpłatnych środków instytucjonalnych i dobrowolnej współpracy; źródłowe honoraria $200–300 za eksperta i $30–50 za wywiad **nie są zatwierdzonym budżetem**.
- **Nie oferować współautorstwa za samo wypełnienie formularza.** Autorstwo oceniać odrębnie według polityki czasopisma i [ICMJE](https://icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html).
- Plan źródłowy: ~**16–18 tygodni** (4–5 miesięcy). To scenariusz, nie zobowiązanie terminowe; harmonogram dostosować do dostępności ekspertów i wymagań komisji.
