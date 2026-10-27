# Kwestionariusz DERA-HRI

**Aktualny bank źródłowy:** [v3.0 EN](../instruments/dera_hri_v3.csv), **45 pozycji rdzenia + 4 modułów**, odpowiedzi 1–7. Archiwalne banki [v2.1](../instruments/dera_hri_v2_1.csv) i [v2](../instruments/dera_hri_v2.csv) pozostają bez zmian. Tekst angielski v3 nie jest zwalidowaną adaptacją wcześniejszej wersji polskiej.

## Administracja (propozycja v3)

Uczestnik odnosi wszystkie odpowiedzi do **jednej zakończonej interakcji** (zalecane bezpośrednio, orientacyjnie 5–10 minut po sesji i przed debriefingiem). Siedmiopunktowa skala zgody, od 1 „Strongly disagree” do 7 „Strongly agree”, z etykietą każdej kategorii. Dane sesji: wersja formularza i język, robot, zadanie, tryb sterowania, czas, dostępne kanały ekspresji, opóźnienie do ankiety, brakujące/niezastosowane pytania.

| Moduł | ID źródłowe v3 | Reguła źródłowa |
| --- | --- | --- |
| EAR-D | 1–11 | wszystkie |
| SEI-D | 12–23 | 12–15 zależne od ruchu/głosu/gestów/mimiki |
| SAP-D | 24–33 | wszystkie |
| MP-D | 34–37 | wszystkie |
| RAR-D | 38–45 | wszystkie |
| RM | M1–M3 | strategie, raportowanie osobno |
| FII | F1 | intencja przyszłej interakcji, osobno |

**SEI 16** w źródle umieszczono wśród pytań obowiązkowych, lecz pyta o zgodność **różnych kanałów**. Jeśli dostępny był jeden kanał, odpowiedź jest strukturalnie niemożliwa: oznaczenie `multichannel_review` w CSV sygnalizuje wymaganą decyzję. Nie imputować „4” za brak kanału.

## Skoring: **NIEZATWIERDZONY**

W dokumencie v3 proponuje się średnie odpowiedzi z każdej podskali, zerowe odwracanie, tolerancję do 20% zwykłych braków, progi 1–2,33 / 2,34–4,66 / 4,67–7 oraz reguły wykluczeń (m.in. wypełnienie w czasie poniżej 3 minut). **To propozycje autora dokumentu, bez walidacji; nie implementować ich automatycznie.**

Istotne sprzeczności:
- **EAR-D 6–9:** komfort, dyskomfort, podejście i unikanie mają różne znaki, nie wyznaczają jednorodnego „nasilenia reaktywności”.
- **SEI-D 19 i 22:** niejasność i utrudnienie interpretacji mają przeciwny kierunek do czytelności; 20 (zmiana interpretacji) także nie jest jednoznacznie ujemna.
- **SAP-D 28 i 30:** zaskoczenie/nieprzewidywalność nie rosną w tym samym kierunku co przewidywalność.
- **RAR-D 38 oraz 42–44:** 38 nie określa walencji, 42–44 opisują destabilizację i stres, a 39–41/45 poprawę regulacji.
- **SEI-D 12–16:** różna liczba kanałów zmienia zawartość pomiaru; średnie z różnych zestawów pozycji nie są z definicji porównywalne.
- Nie istnieją normy ani klinicznie uzasadnione progi wyników; „wysoki RAR” nie ma ustalonej interpretacji.

Kolumna `source_reverse=false` **odtwarza deklarację v3**, a nie potwierdza, że wyliczenie prostych średnich jest prawidłowe. Ostateczne kierunki, selekcję pozycji, braki danych i reguły wyliczeń należy zatwierdzić po ocenie treściowej i analizie empirycznej.

## Nierozwiązane regresje treściowe v2.1 → v3

Porównanie v3 z wcześniej dostarczoną recenzją v2 pokazuje, że część sformułowań skrytykowanych i poprawionych w kandydacie v2.1 **wróciła w angielskim banku v3**:

- **EAR 11:** jednocześnie „przewidywalne” i „pod kontrolą” (dwa konstrukty w jednym pytaniu); w v2.1 rozdzielono te pojęcia.
- **SEI 19 i 22:** ponownie „what the robot meant” (mentalizacja) i „artificiality” (ocena estetyczno-postawowa) zamiast samej czytelności sygnałów.
- **SAP 26 i 32:** „without reason” zakłada interpretację przyczyn zachowania, a „Thanks to predictability” narzuca zależność przyczynową w treści pozycji; v2.1 proponowała bardziej neutralne odpowiedniki.

Wymagana jest **ponowna ocena treściowa tych sześciu pozycji**; zachować bank źródłowy v3 bez zmian do czasu decyzji i wersjonowanej rewizji. [Przegląd decyzji](https://github.com/MatPomGit/arc-dera-hri/issues/1).

## Zgodność z manuskryptem v3

Przesłany szkic artykułu `kwestionariusz-dera-hri_v3.docx` powtarza poprawną liczbę **45 pozycji głównych**, ale nie zawiera pełnego tekstu kwestionariusza, mimo deklaracji w części „Data Availability”. Jedynym aktualnym kompletnym bankiem jest [v3 CSV](../instruments/dera_hri_v3.csv). W szkicu zaproponowano ponadto próg „minimum 6” wypełnionych pozycji SEI-D; **nie rozwiązuje on** problemu strukturalnego braku kanału lub interpretacji SEI 16. Traktować go jako niezatwierdzoną regułę źródłową.

## Wersjonowanie

Numeracja **v3 jest nowa**; ID v2/v2.1 nie mogą być używane wymiennie. Źródło podaje mapowanie w dodatku B; mapę tę należy niezależnie zweryfikować przed analizą międzywersyjną. Dane powinny zawierać wersję, język oraz dokładny identyfikator pozycji. **Nie scalać odpowiedzi z różnie sformułowanych wersji bez oceny równoważności.**
