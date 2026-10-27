# ARC-DERA-HRI

**Dynamic Embodied Relational Affect in Human–Robot Interaction**

Projekt opracowania i walidacji narzędzia do badania subiektywnych procesów afektywnych podczas bezpośredniej interakcji człowieka z robotem. **Status: koncepcja i kwestionariusz rozwojowy, bez walidacji empirycznej.**

## Model

DERA-HRI zakłada cztery współwystępujące, potencjalnie powiązane systemy:

| System | Przedmiot pomiaru |
| --- | --- |
| EAR-D | Ucieleśniona reaktywność afektywna |
| SAP-D | Predykcja społeczno-afektywna |
| SEI-D | Ucieleśniona interpretacja semiotyczna |
| RAR-D | Relacyjna regulacja afektywna |

Założenie o dynamice procesów **nie zostało zweryfikowane**. Ankieta po pojedynczej interakcji mierzy deklaracje uczestnika, nie obiektywne sprzężenia zwrotne.

## Aktualny instrument

- **DERA-HRI v2 (propozycja):** 48 pozycji, 12 na system; siedmiopunktowe odpowiedzi od „zdecydowanie się nie zgadzam” do „zdecydowanie się zgadzam”.
- Administracja dotyczy **jednej zakończonej interakcji**; orientacyjnie do 5–10 minut po jej zakończeniu.
- Nie zakłada się globalnego wyniku; podskale i sposób punktowania wymagają potwierdzenia empirycznego.
- Brak danych empirycznych, oszacowań rzetelności i potwierdzonej struktury czynnikowej.

## Dokumentacja

- [Model i ograniczenia](docs/model.md)
- [Instrument, administracja i dane kontrolne](docs/instrument.md)
- [Plan walidacji i decyzje metodologiczne](docs/validation.md)
- [Źródła i historia rewizji](docs/sources.md)
- [Bank pozycji v2, CSV](instruments/dera_hri_v2.csv)
- [Zasady pracy agentów](AGENTS.md)

## Zakres i zasady

Repozytorium dotyczy **budowy narzędzia psychometrycznego**. Eksperymentalne badania efektów autonomii/ekspresji robota jako odrębny artykuł pozostają poza jego zakresem (projekt ARC-SAPIENS).

Kolejne dokumenty źródłowe aktualizują istniejące pliki, zamiast mnożyć dokumentację. Oprogramowanie powstaje dopiero w razie realnej potrzeby: KISS, standardowe biblioteki, PEP 8, testy i reprodukowalność. Brak płatnych usług i domyślnie brak GitHub Actions.

## Następny etap

Ekspercka ocena treści i wywiady poznawcze, rozstrzygnięcie niejednoznaczności pozycji, zamrożenie protokołu pilotażowego i planu walidacji. Zbieranie danych od uczestników wymaga odpowiednich zgód i procedur.
