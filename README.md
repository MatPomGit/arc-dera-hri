# ARC-DERA-HRI

**Dynamic Embodied Relational Affect in Human–Robot Interaction**

Rozwój i walidacja kwestionariusza samoopisowego doświadczeń afektywnych po konkretnej interakcji człowieka z robotem. **Status: wersja rozwojowa v3.0; brak danych potwierdzających trafność, rzetelność i strukturę czynnikową.**

Aktualny model proponuje **pięć domen i 45 pozycji głównych**: EAR-D (11), SEI-D (12), SAP-D (10), MP-D (4), RAR-D (8). Dodatkowe pozycje M1–M3 opisują strategie regulacji, a F1 przekonanie o możliwym przyszłym wpływie interakcji. **Łącznie 49 pozycji.** Treść pozycji, skoring i interpretacja wyników nie są jeszcze zatwierdzone psychometrycznie.

## Dokumentacja

- [Strona projektu](docs/index.md) i [model](docs/model.md)
- [Kwestionariusz i administracja](docs/instrument.md)
- [Protokół trafności treściowej](docs/content-validity.md) i [plan walidacji](docs/validation.md)
- [Źródła i wersje](docs/sources.md), [historia zmian](CHANGELOG.md)
- Banki: [v3 (EN)](instruments/dera_hri_v3.csv), [v2.1 (PL)](instruments/dera_hri_v2_1.csv), [v2 (PL)](instruments/dera_hri_v2.csv)

Po włączeniu GitHub Pages dokumentacja będzie dostępna pod adresem **https://matpomgit.github.io/arc-dera-hri/**.

## MkDocs

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs serve
python -m mkdocs build --strict
```

Workflow [publikacji Pages](.github/workflows/pages.yml) buduje dokumentację przy zmianach i wdraża ją z `main`. **Pierwsze uruchomienie:** w `Settings → Pages → Build and deployment` wybierz `GitHub Actions`. Bez tego kroku samo dodanie workflow nie potwierdza działania publicznej strony.

Prace zgodnie z [KISS i zasadami agentów](AGENTS.md). Narzędzie dotyczy pomiaru HRI; odrębne eksperymenty z humanoidami należą do ARC-SAPIENS. Otwarte decyzje metodologiczne: [Issue #1](https://github.com/MatPomGit/arc-dera-hri/issues/1).
