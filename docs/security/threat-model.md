# Model zagrożeń DERA-HRI

**Status: NOT_ASSESSED.** Nie stwierdza wykonania audytu.

| Obszar | Zagrożenie | Kontrola |
| --- | --- | --- |
| Bank pytań | Niezgodna wersja lub nieautoryzowana zmiana tekstu | Testy ID i brzmienia, nowa wersja instrumentu |
| Odpowiedzi ekspertów i osób badanych | Identyfikacja, niezamierzone ujawnienie | Dane poza Git i Pages, uprawnienia, retencja |
| Analiza CVR/CVI | Błędny wzór, niekompletne oceny | Testy numeryczne, niezależna weryfikacja |
| GitHub Pages | Wyciek promptów, instrukcji agentowych i dokumentów roboczych | Osobne `pages/`, allowlista, audyt HTML |
| CI i zależności | Wykonanie niezaufanego kodu z sekretami | Ograniczone uprawnienia, izolacja i brak kluczy |

Po rozpoczęciu realnych badań opisz źródła danych, podstawę prawną, właściciela ryzyka, skutki, prawdopodobieństwo i dowody kontroli. Nie utożsamiaj testu narzędzia z walidacją konstruktu.
