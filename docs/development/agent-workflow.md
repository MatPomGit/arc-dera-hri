# Procedura autonomicznych agentów

**Wersja:** 1.0.0. Właścicielem badań, decyzji metodologicznych i danych jest projekt ARC-DERA-HRI.

## Rozpoznanie i rezerwacja

Przed edycją przeczytaj `AGENTS.md` w katalogu głównym, `README.md` w katalogu głównym, bieżące Issues, PR, stan `main`, testy i odpowiednie strony MkDocs. Sprawdź istniejące rozwiązania i pracę innych agentów. Wybierz jedno nierozpoczęte zadanie, preferując naprawy, aktualizację istniejącego PR i blokady naukowe przed nowymi funkcjami. Zarezerwuj Issue komentarzem lub istniejącym leasingiem Research Autopilot. Nie twórz kolejki, schedulera ani drugiego backlogu.

Przed użyciem skilla sprawdź jego opis, pochodzenie, wersję, wymagane uprawnienia i wykluczenia; uruchamiaj tylko potrzebne, zweryfikowane narzędzia. Skill nie upoważnia do obejścia polityk repozytorium. Maksymalnie jeden aktywny feature PR na repozytorium i pięć w zarządzanym portfolio, zgodnie z kontrolerem.

## Implementacja i badania

DoR: mierzalny rezultat, zakres, zależności, kryteria akceptacji i prawo do użycia danych. Stosuj KISS, DRY, YAGNI, najmniejsze uprawnienia, Python PEP 8/257/484 oraz zgodność publicznych kontraktów. Nie dodawaj zbędnych zależności ani abstrakcji. W instrumentach nie wolno zmieniać istniejących ID lub treści pozycji bez nowej jawnej wersji. Ani hipoteza, ani opinia eksperta, ani wewnętrzna kontrola CSV nie potwierdzają trafności skali, rzetelności czy struktury czynnikowej.

Dowody zapisuj z pochodzeniem, wersją instrumentu, warunkami, statusem i ograniczeniami. Oddziel projekt, pilotaż, walidację treści, analizę czynnikową i walidację empiryczną. Nie fabricuj wyników ani cytowań. Dane uczestników i prywatne odpowiedzi nie mogą trafić do Issues i publicznych artefaktów. Nie publikuj kluczy narzędzi dydaktycznych w materiałach studentów.

## Testy, PR i zamknięcie

Testuj dokładny SHA, w tym integralność instrumentów i linki. Przy zmianie dokumentacji uruchom `python -m mkdocs build --strict`, gdy narzędzie jest dostępne; brak narzędzia raportuj NOT_RUN/UNAVAILABLE. Odróżniaj PASS, FAIL, BLOCKED i NOT_RUN. Zmieniony HEAD wymaga ponownej odpowiedniej walidacji. Nie obchodź GitHub rules, CI ani wymaganego niezależnego review. Komentarz tego samego konta nie jest automatycznie formalnym zatwierdzeniem.

DoD: zaakceptowane kryteria, dowody testów, dokumentacja i Issue zaktualizowane, PR zintegrowany wyłącznie po spełnieniu bramek, osobno potwierdzone wdrożenie Pages (jeśli dotyczy), usunięte wyłącznie własne scalone gałęzie i worktrees. Zapisz blokadę i następny krok.

## Język i materiały dydaktyczne

Stosuj poprawny polski i zdaniowe nagłówki, bez znaków U+2013 i U+2014 w nowej prozie (z wyjątkiem cytatu i niezmiennych danych). Pytania dla studentów muszą wymagać wiedzy, a nie eliminacji oczywistych dystraktorów; domyślnie cztery wiarygodne propozycje i jednoznaczny klucz, przechowywany osobno.
