# ARC-DERA-HRI

**Dynamic Embodied Relational Affect in Human–Robot Interaction**

Projekt opracowania i walidacji kwestionariusza samoopisowego doświadczeń afektywnych po **konkretnej interakcji z robotem**. **Status: wersja rozwojowa, bez wyników walidacji empirycznej.**

## Aktualny model: DERA-HRI v3.0 (propozycja)

| Domena | Przedmiot pomiaru | Pozycje |
| --- | --- | ---: |
| EAR-D | Subiektywnie zauważane reakcje cielesne | 11 |
| SEI-D | Interpretacja sygnałów i ekspresji robota | 12 |
| SAP-D | Predykcja zachowania i uczenie się przewidywalności | 10 |
| MP-D | Przypisywanie robotowi stanów umysłowych i intencji | 4 |
| RAR-D | Subiektywna regulacja afektywna w relacji z robotem | 8 |
| **Razem** | **Pięć hipotetycznych domen** | **45** |

Ponadto 3 pozycje o strategiach regulacji (M1–M3) i 1 o oczekiwanych przyszłych interakcjach (F1). **49 pozycji łącznie.** Dokument źródłowy miejscami błędnie podaje 44 pozycje podstawowe.

## Dokumentacja i dane źródłowe

- [Model i ograniczenia](docs/model.md)
- [Administracja, numeracja i wątpliwości dotyczące skoringu](docs/instrument.md)
- [Plan rozwoju i walidacji](docs/validation.md) · [Protokół walidacji treściowej v3](docs/content-validity.md)
- [Pochodzenie wersji, szkic artykułu i audyt cytowań](docs/sources.md)
- [Bank v3 (EN)](instruments/dera_hri_v3.csv) · [v2.1 (PL)](instruments/dera_hri_v2_1.csv) · [v2 (PL)](instruments/dera_hri_v2.csv)
- [Zasady agentów i KISS](AGENTS.md) · [Decyzje do zamknięcia](https://github.com/MatPomGit/arc-dera-hri/issues/1)

**Opis kwestionariusza v3:** `opis-kwestionariusza_v3.docx` zawiera komplet 49 pozycji; zweryfikowano zgodność ich brzmienia z [bankiem CSV](instruments/dera_hri_v3.csv). Nie stanowi nowej wersji skali. Szczegóły i rozbieżności: [instrument](docs/instrument.md#pełny-formularz-źródłowy-v3).

**Manuskrypt v3:** otrzymany `kwestionariusz-dera-hri_v3.docx` jest szkicem **artykułu koncepcyjno-metodologicznego**, nie raportem z walidacji i nie zawiera pełnego banku pytań. Kanoniczny tekst pozycji pozostaje w CSV; [uwagi do manuskryptu](docs/sources.md#szkic-artykułu-koncepcyjnego-v3).

**Ważne:** v3 jest propozycją teoretyczną, nie narzędziem zwalidowanym. Wskazane w źródle średnie, brak odwracania, progi wyników i zasady wykluczeń **nie są zatwierdzonym skoringiem**. Bez wyników eksperckich i empirycznych nie należy tworzyć globalnej ani interpretowalnej skali liczbowej.

Projekt dotyczy pomiaru HRI, a nie odrębnych badań interwencyjnych autonomii humanoida (ARC-SAPIENS). Kod tylko w niezbędnym zakresie: KISS, PEP 8, standard library, bez płatnych usług.
