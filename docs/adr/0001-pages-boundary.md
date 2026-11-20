# ADR-0001: granice dokumentacji i publikacji

**Status: proposed**  
**Data: 2026-11-20**

## Kontekst

Dotychczasowe źródło MkDocs `docs/` obejmowało zarówno opis instrumentu, jak i procedurę autonomicznych agentów. Budowanie wszystkiego z tego katalogu ujawnia dokumenty przeznaczone wyłącznie do wewnętrznej pracy.

## Propozycja

Przenieść osiem zatwierdzonych opisów naukowych do odrębnego `pages/` i publikować tylko pliki z jawnej listy `config/pages-policy.json`. Procedury agentów i wewnętrzne ADR pozostają poza witryną. Build może być automatycznie testowany, ale publikacja wymaga oddzielnego ręcznego zatwierdzenia.

## Alternatywy i konsekwencje

Usunięcie jednej pozycji z nawigacji nie wystarcza, ponieważ MkDocs może generować także strony spoza `nav`. Użycie całego `docs/` prowadzi do przypadkowego ujawnienia nowych plików. Oddzielne `pages/` wymaga kontroli źródeł, linków i wygenerowanej witryny, ale daje audytowalną granicę publikacji.

ADR pozostaje propozycją do niezależnej recenzji i zatwierdzenia.
