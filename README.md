# ARC-DERA-HRI

**Dynamic Embodied Relational Affect in Human–Robot Interaction**

Projekt opracowania i walidacji samoopisowego narzędzia do oceny doświadczeń afektywnych podczas **konkretnej interakcji człowieka z robotem**. **Status: projekt rozwojowy; brak walidacji i danych empirycznych.**

## Model

Cztery postulowane, współwystępujące domeny:

| System | Konstrukty kandydackie |
| --- | --- |
| EAR-D | Zauważane reakcje cielesne i odczucia afektywne |
| SAP-D | Przewidywanie i poczucie kontroli zachowania robota |
| SEI-D | Interpretacja sygnałów ruchowych, głosowych i kontekstowych |
| RAR-D | Subiektywnie odczuwana regulacja emocji podczas interakcji |

Recenzja dopuszcza **alternatywny model pięcioczynnikowy** z MP-D (przypisywanie umysłu/mentalizacja), ale nie potwierdza jego trafności.

## Instrument

- **[v2.1, propozycja po recenzji](instruments/dera_hri_v2_1.csv):** 48 pozycji (12 na domenę), odpowiedzi 1–7.
- **[v2, wersja historyczna](instruments/dera_hri_v2.csv):** 48 pozycji, zachowana do porównania i śledzenia zmian.
- Skala po pojedynczej, świeżo zakończonej interakcji; brak uzasadnionego wyniku globalnego.
- **Klucz odwrócenia i skoring v2.1 są propozycją źródłową, nie zatwierdzonym algorytmem.** Szczególnie wymagają rewizji EAR-D i pozycje zależne od kanału komunikacji.

## Dokumentacja

- [Model i wariant MP-D](docs/model.md)
- [Instrukcja i wersje kwestionariusza](docs/instrument.md)
- [Plan walidacji i hipotezy](docs/validation.md)
- [Źródła i historia zmian](docs/sources.md)
- [Zasady minimalnego kodu i aktualizacji](AGENTS.md)

## Granice projektu

ARC-DERA-HRI odpowiada za rozwój **instrumentu psychometrycznego**; eksperymentalne badania skutków określonych zachowań humanoida są osobnym nurtem ARC-SAPIENS. Nie utożsamiać samoopisu z pomiarem fizjologicznym ani przekrojowych korelacji z mechanizmami przyczynowymi.

Oprogramowanie tylko wtedy, gdy potrzebne: Python, standard library, PEP 8, KISS, bez duplikowania narzędzi i dokumentacji oraz bez płatnych usług.

**Następna bramka:** ocena trafności treściowej i wywiady poznawcze, następnie decyzja o rewizjach pozycji i zamrożeniu protokołu pilotażowego.
